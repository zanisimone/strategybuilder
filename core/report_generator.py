import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_report(trades_df: pd.DataFrame):
    if trades_df.empty:
        print("⚠️ Nessun trade da analizzare.")
        return

    print("\n📊 Report Avanzato Strategia\n")

    trades_df = trades_df.copy()
    trades_df["cum_pnl"] = trades_df["pnl"].cumsum()

    # === 1. Equity Line ===
    plt.figure(figsize=(10, 5))
    plt.plot(trades_df["exit_time"], trades_df["cum_pnl"], label="Equity Line", linewidth=2)
    plt.title("Equity Line")
    plt.xlabel("Data")
    plt.ylabel("Profitto cumulato")
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    plt.show()

    # === 2. Metriche base ===
    total_trades = len(trades_df)
    total_profit = trades_df["pnl"].sum()
    avg_trade = trades_df["pnl"].mean()
    wins = trades_df[trades_df["pnl"] > 0]
    losses = trades_df[trades_df["pnl"] < 0]
    win_rate = len(wins) / total_trades * 100 if total_trades else 0
    avg_win = wins["pnl"].mean() if not wins.empty else 0
    avg_loss = losses["pnl"].mean() if not losses.empty else 0
    profit_factor = wins["pnl"].sum() / abs(losses["pnl"].sum()) if not losses.empty else np.inf
    expectancy = (win_rate / 100 * avg_win) + ((100 - win_rate) / 100 * avg_loss)

    # === 3. Metriche avanzate ===
    pnl_series = trades_df["cum_pnl"]
    max_dd = (pnl_series.cummax() - pnl_series).max()
    max_dd_pct = max_dd / pnl_series.cummax().max() * 100 if pnl_series.cummax().max() != 0 else 0

    duration_days = (trades_df["exit_time"].iloc[-1] - trades_df["entry_time"].iloc[0]).days
    years = duration_days / 365.0 if duration_days > 0 else 1
    cagr = (1 + total_profit) ** (1 / years) - 1 if years > 0 else 0

    returns = trades_df["pnl"]
    sharpe = returns.mean() / returns.std() * np.sqrt(252) if returns.std() > 0 else 0
    downside_returns = returns[returns < 0]
    sortino = returns.mean() / downside_returns.std() * np.sqrt(252) if downside_returns.std() > 0 else 0

    win_loss_ratio = avg_win / abs(avg_loss) if avg_loss != 0 else np.inf

    # === 4. Output console ===
    print(f"Totale trade           : {total_trades}")
    print(f"Profitto netto         : {total_profit:.2f}")
    print(f"Average trade          : {avg_trade:.2f}")
    print(f"Win rate               : {win_rate:.2f}%")
    print(f"Win/Loss ratio         : {win_loss_ratio:.2f}")
    print(f"Media vincite          : {avg_win:.2f}")
    print(f"Media perdite          : {avg_loss:.2f}")
    print(f"Expectancy per trade   : {expectancy:.2f}")
    print(f"Max Drawdown           : {max_dd:.2f}")
    print(f"Max Drawdown %         : {max_dd_pct:.2f}%")
    print(f"Profit Factor          : {profit_factor:.2f}")
    print(f"CAGR                   : {cagr*100:.2f}%")
    print(f"Sharpe Ratio (Rf=0)    : {sharpe:.2f}")
    print(f"Sortino Ratio (Rf=0)   : {sortino:.2f}")
