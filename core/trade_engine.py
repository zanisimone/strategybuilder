from typing import Optional
import pandas as pd
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

        # Mappa l'orario intraday alla riga giusta del daily_df
        daily_index = self.get_daily_index_for_intraday_time(self.intraday_df['time'].iloc[i])
        if daily_index is None or daily_index < 5:
            return None  # salto per sicurezza

        # Entry Long
        if self.evaluate_pattern(self.config.pattern_long, PATTERNS_LONG, daily_index, self.daily_df) and \
                not self.evaluate_pattern(self.config.pattern_exclusion_long, PATTERNS_EXCL_LONG, daily_index,
                                          self.daily_df) and \
                self.evaluate_pattern(self.config.pattern_vol_long, PATTERNS_VOL_LONG, i, self.intraday_df):
            return "long"

        # Entry Short
        if self.evaluate_pattern(self.config.pattern_short, PATTERNS_SHORT, daily_index, self.daily_df) and \
                not self.evaluate_pattern(self.config.pattern_exclusion_short, PATTERNS_EXCL_SHORT, daily_index,
                                          self.daily_df) and \
                self.evaluate_pattern(self.config.pattern_vol_short, PATTERNS_VOL_SHORT, i, self.intraday_df):
            return "short"

        return None

    def check_exit_conditions(self, i: int, entry_index: int, entry_price: float, position: str) -> Optional[str]:
        """
        Controlla se esiste una condizione di uscita (TP, SL, N barre, fine giornata, venerdì)
        """
        current_price = self.intraday_df['Close'].iloc[i]
        bars_held = i - entry_index
        time_now = self.intraday_df['time'].iloc[i]

        risk_amount = self.config.initial_capital * self.config.risk_per_trade_pct

        if position == "long":
            sl = entry_price - (self.config.stop_loss_long * risk_amount)
            tp = entry_price + (self.config.take_profit_long * risk_amount)
            max_bars = self.config.bars_exit_long
        else:
            sl = entry_price + (self.config.stop_loss_short * risk_amount)
            tp = entry_price - (self.config.take_profit_short * risk_amount)
            max_bars = self.config.bars_exit_short

        # SL / TP
        if position == "long":
            if current_price <= sl:
                return "stop_loss"
            if current_price >= tp:
                return "take_profit"
        else:
            if current_price >= sl:
                return "stop_loss"
            if current_price <= tp:
                return "take_profit"

        # Time exit
        if bars_held >= max_bars:
            return "time_exit"

        # EOD / EOW
        is_eod = self.config.exit_eod and (
                i + 1 >= len(self.intraday_df) or
                self.intraday_df['time'].iloc[i].date() != self.intraday_df['time'].iloc[i + 1].date()
        )
        if is_eod:
            return "eod"

        is_eow = self.config.exit_eow and time_now.weekday() == 4
        if is_eow:
            return "eow"

        return None

    def run(self) -> pd.DataFrame:
        """
        Esegue la strategia completa su tutto l'intraday_df, con stampa di avanzamento.
        """
        position = None
        entry_price = None
        entry_index = None
        exit_reason = None

        total = len(self.intraday_df)
        progress_step = 4

        for i in range(10, total):
            # Stampa avanzamento percentuale
            if i % (total // progress_step) == 0:
                percent = int(100 * i / total)
                print(f"🚀 Avanzamento: {percent+1}%")

            if position is None:
                signal = self.evaluate_entry_signal(i)
                if signal:
                    position = signal
                    entry_price = self.intraday_df['Close'].iloc[i]
                    entry_index = i
            else:
                exit_reason = self.check_exit_conditions(i, entry_index, entry_price, position)
                if exit_reason:
                    exit_price = self.intraday_df['Close'].iloc[i]
                    self.trades.append({
                        "entry_index": entry_index,
                        "exit_index": i,
                        "entry_time": self.intraday_df['time'].iloc[entry_index],
                        "exit_time": self.intraday_df['time'].iloc[i],
                        "position": position,
                        "entry_price": entry_price,
                        "exit_price": exit_price,
                        "pnl": exit_price - entry_price if position == "long" else entry_price - exit_price,
                        "exit_reason": exit_reason
                    })
                    position = None
                    entry_price = None
                    entry_index = None
                    exit_reason = None

        print("✅ Processo Completato.")
        return pd.DataFrame(self.trades)

