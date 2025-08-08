from typing import Optional
import pandas as pd
from typing import Optional


from core.pattern_library import (
    PATTERNS_LONG,
    PATTERNS_SHORT,
    PATTERNS_EXCL_LONG,
    PATTERNS_EXCL_SHORT,
    PATTERNS_VOL_LONG,
    PATTERNS_VOL_SHORT,
)
from core.strategy import StrategyConfig


class TradeEngine:
    def __init__(self, config: StrategyConfig, daily_df: pd.DataFrame, intraday_df: pd.DataFrame):
        self.config = config
        self.daily_df = daily_df.reset_index(drop=True)
        self.intraday_df = intraday_df.reset_index(drop=True)
        self.trades = []

    def evaluate_time_window(self, time_str: str) -> bool:
        """
        Controlla se l'orario (formato 'HH:MM') rientra nella sessione operativa
        """
        hour, minute = map(int, time_str.split(":"))
        time_val = hour * 100 + minute
        return self.config.session_start <= time_val <= self.config.session_end

    def get_daily_index_for_intraday_time(self, t: pd.Timestamp) -> int:
        """
        Restituisce l'indice del daily_df corrispondente alla data di t
        """
        date_only = t.date()
        idx = self.daily_df[self.daily_df['time'].dt.date == date_only].index
        return idx[0] if not idx.empty else None

    def evaluate_pattern(self, pattern_name: str, pattern_dict: dict, i: int, df: pd.DataFrame) -> bool:
        """
        Valuta un singolo pattern su un dato DataFrame
        """
        if not pattern_name:
            return True
        return pattern_dict[pattern_name](df, i)

    def evaluate_entry_signal(self, i: int) -> Optional[str]:
        time_str = self.intraday_df['time'].iloc[i].strftime("%H:%M")
        if not self.evaluate_time_window(time_str):
            return None

        daily_index = self.get_daily_index_for_intraday_time(self.intraday_df['time'].iloc[i])
        if daily_index is None or daily_index < 5:
            return None

        if self.config.enable_long:
            if self.evaluate_pattern(self.config.pattern_long, PATTERNS_LONG, daily_index, self.daily_df) and \
                    not self.evaluate_pattern(self.config.pattern_exclusion_long, PATTERNS_EXCL_LONG, daily_index,
                                              self.daily_df) and \
                    self.evaluate_pattern(self.config.pattern_vol_long, PATTERNS_VOL_LONG, i, self.intraday_df):
                return "long"

        if self.config.enable_short:
            if self.evaluate_pattern(self.config.pattern_short, PATTERNS_SHORT, daily_index, self.daily_df) and \
                    not self.evaluate_pattern(self.config.pattern_exclusion_short, PATTERNS_EXCL_SHORT, daily_index,
                                              self.daily_df) and \
                    self.evaluate_pattern(self.config.pattern_vol_short, PATTERNS_VOL_SHORT, i, self.intraday_df):
                return "short"

        return None

    def check_exit_conditions_allin(
            self,
            i: int,
            entry_index: int,
            entry_price: float,
            position: str,
            size: int
    ) -> Optional[str]:
        """
        Exit conditions per risk model ALL-IN con SL/TP in $ di PnL flottante.
        """
        df = self.intraday_df
        current_price = float(df['Close'].iloc[i])
        bars_held = i - entry_index
        time_now = df['time'].iloc[i]

        if position == "long":
            current_pnl = (current_price - entry_price) * size
            sl_dollars = float(self.config.sl_dollars_long)
            tp_dollars = float(self.config.tp_dollars_long)
            max_bars = int(self.config.bars_exit_long)
        else:
            current_pnl = (entry_price - current_price) * size
            sl_dollars = float(self.config.sl_dollars_short)
            tp_dollars = float(self.config.tp_dollars_short)
            max_bars = int(self.config.bars_exit_short)

        # SL / TP in dollari
        if current_pnl <= -sl_dollars:
            return "stop_loss"
        if current_pnl >= tp_dollars:
            return "take_profit"

        # Uscita per tempo (numero barre)
        if bars_held >= max_bars:
            return "time_exit"

        # Fine giornata (ultima barra del giorno o ultima barra del dataset)
        is_eod = self.config.exit_eod and (
                i + 1 >= len(df) or df['time'].iloc[i].date() != df['time'].iloc[i + 1].date()
        )
        if is_eod:
            return "eod"

        # Venerdì (EOW)
        is_eow = self.config.exit_eow and time_now.weekday() == 4
        if is_eow:
            return "eow"

        return None

    def run(self) -> pd.DataFrame:
        """
        Esegue la strategia su tutto l'intraday_df con risk model ALL-IN:
        - size = floor(equity / entry_price)
        - TP/SL in dollari di PnL flottante
        - equity aggiornata dopo ogni trade
        """
        position = None
        entry_price = None
        entry_index = None
        exit_reason = None
        size = None

        # Equity dinamica
        equity = float(self.config.initial_capital)

        total = len(self.intraday_df)
        progress_step = 4

        for i in range(10, total):
            # progress bar semplice
            step = max(1, total // progress_step)
            if i % step == 0:
                percent = int(100 * i / max(1, total - 1))
                print(f"🚀 Avanzamento: {min(percent + 1, 100)}%")

            if position is None:
                # Tentativo di ingresso
                signal = self.evaluate_entry_signal(i)
                if signal:
                    entry_price = float(self.intraday_df['Close'].iloc[i])
                    # size all-in
                    size = int(self.config.initial_capital // entry_price)
                    if size <= 0:
                        # non posso aprire posizione
                        entry_price = None
                        size = None
                        continue

                    position = signal
                    entry_index = i

            else:
                # Gestione uscita con PnL flottante in $
                exit_reason = self.check_exit_conditions_allin(
                    i=i,
                    entry_index=entry_index,
                    entry_price=entry_price,
                    position=position,
                    size=size
                )

                if exit_reason:
                    exit_price = float(self.intraday_df['Close'].iloc[i])

                    if position == "long":
                        pnl = (exit_price - entry_price) * size
                    else:
                        pnl = (entry_price - exit_price) * size


                    self.trades.append({
                        "entry_index": entry_index,
                        "exit_index": i,
                        "entry_time": self.intraday_df['time'].iloc[entry_index],
                        "exit_time": self.intraday_df['time'].iloc[i],
                        "position": position,
                        "entry_price": entry_price,
                        "exit_price": exit_price,
                        "pnl": pnl,
                        "size": size,
                        "equity_after": self.config.initial_capital + sum(p['pnl'] for p in self.trades),
                        "exit_reason": exit_reason
                    })

                    # reset stato
                    position = None
                    entry_price = None
                    entry_index = None
                    exit_reason = None
                    size = None

        print("✅ Processo Completato.")
        return pd.DataFrame(self.trades)


