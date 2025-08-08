import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def generate_report(trades_df: pd.DataFrame, initial_equity: float):
    if trades_df.empty:
        print("⚠️ Nessun trade da analizzare.")
        return

    df = trades_df.copy()

    # Equity curve: se hai equity_after la uso, altrimenti ricostruisco
    if "equity_after" in df.columns:
        equity_curve = df["equity_after"].astype(float)
    else:
        df["cum_pnl"] = df["pnl"].cumsum()
        equity_curve = initial_capital + df["cum_pnl"]

    # --- Plot Equity Line ---
    plt.figure(figsize=(10, 5))
    plt.plot(df["exit_time"], equity_curve, label="Equity Line", linewidth=2)
    plt.title("Equity Line (All-In, TP/SL in $)")
    plt.xlabel("Data")
    plt.ylabel("Equity")
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

    # --- Metriche principali (in $) ---
    total_trades = len(df)
    final_equity = float(equity_curve.iloc[-1])
    total_profit = final_equity - initial_equity
    avg_trade = df["pnl"].mean()

    wins = df[df["pnl"] > 0]
    losses = df[df["pnl"] < 0]
    win_rate = (len(wins) / total_trades * 100) if total_trades else 0.0
    avg_win = wins["pnl"].mean() if not wins.empty else 0.0
    avg_loss = losses["pnl"].mean() if not losses.empty else 0.0
    denom = -losses["pnl"].sum()
    profit_factor = (wins["pnl"].sum() / denom) if denom > 0 else np.inf
    expectancy = (win_rate / 100.0) * avg_win + (1 - win_rate / 100.0) * avg_loss

    # --- Max Drawdown su equity ---
    ec = equity_curve.values
    roll_max = np.maximum.accumulate(ec)
    drawdowns = roll_max - ec
    max_dd = float(np.max(drawdowns)) if drawdowns.size else 0.0
    peak_equity = float(np.max(roll_max)) if roll_max.size else 1.0
    max_dd_pct = (max_dd / peak_equity * 100.0) if peak_equity > 0 else 0.0

    # --- Timing & CAGR (da equity) ---
    duration_days = (pd.to_datetime(df["exit_time"].iloc[-1]) - pd.to_datetime(df["entry_time"].iloc[0])).days
    years = max(duration_days / 365.0, 1e-9)  # evita divisioni per zero
    cagr = (final_equity / initial_equity) ** (1 / years) - 1 if initial_equity > 0 else 0.0

    # --- Ritorni per-trade (percentuali) per Sharpe/Sortino per-trade annualizzati ---
    # equity_before_i = equity_after_{i-1}, con il primo calcolato da initial_equity
    if "equity_after" in df.columns:
        equity_before = df["equity_after"].shift(1)
        equity_before.iloc[0] = initial_equity
        ret_trade = df["pnl"] / equity_before
    else:
        # Fallback: usa pnl / equity precedente ricostruita dalla curva
        equity_before = pd.Series(equity_curve).shift(1)
        equity_before.iloc[0] = initial_equity
        ret_trade = df["pnl"] / equity_before.values

    ret_trade = ret_trade.replace([np.inf, -np.inf], np.nan).dropna()

    # Annualizzazione per-trade: stima trades_per_year
    trades_per_year = total_trades / years if years > 0 else 0.0
    if len(ret_trade) > 1 and ret_trade.std() > 0 and trades_per_year > 0:
        sharpe = ret_trade.mean() / ret_trade.std() * np.sqrt(trades_per_year)
        downside = ret_trade[ret_trade < 0]
        sortino = ret_trade.mean() / downside.std() * np.sqrt(trades_per_year) if downside.std() > 0 else np.nan
    else:
        sharpe, sortino = np.nan, np.nan

    # --- Win/Loss ratio e expectancy in % ---
    win_loss_ratio = (avg_win / abs(avg_loss)) if avg_loss != 0 else np.inf
    expectancy_pct = ret_trade.mean() * 100 if len(ret_trade) else np.nan

    # --- Output ---
    print("📊 Report Avanzato Strategia (All-In)")
    print(f"Totale trade            : {total_trades}")
    print(f"Initial Equity          : {initial_equity:,.2f}")
    print(f"Final Equity            : {final_equity:,.2f}")
    print(f"Profitto netto          : {total_profit:,.2f}")
    print(f"Average trade ($)       : {avg_trade:,.2f}")
    print(f"Win rate                : {win_rate:.2f}%")
    print(f"Win/Loss ratio          : {win_loss_ratio:.2f}")
    print(f"Media vincite ($)       : {avg_win:,.2f}")
    print(f"Media perdite ($)       : {avg_loss:,.2f}")
    print(f"Expectancy per trade $  : {expectancy:,.2f}")
    print(f"Expectancy per trade %  : {expectancy_pct:.2f}%")
    print(f"Max Drawdown ($)        : {max_dd:,.2f}")
    print(f"Max Drawdown (%)        : {max_dd_pct:.2f}%")
    print(f"Profit Factor           : {profit_factor:.2f}")
    print(f"CAGR                    : {cagr*100:.2f}%")
    print(f"Sharpe (per-trade ann.) : {sharpe:.2f}")
    print(f"Sortino (per-trade ann.): {sortino:.2f}")

