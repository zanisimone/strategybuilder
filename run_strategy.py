import pandas as pd
from core.strategy import StrategyConfig
from core.trade_engine import TradeEngine
from data.data_loader import load_data
from core.report_generator import generate_report

file_path = "data/@NQ_60_Minutes.txt"
intraday_df, daily_df = load_data(file_path)

config = StrategyConfig(
    # Base
    initial_capital=1000000.0,
    session_start=0,      # 00:00
    session_end=2300,     # 23:00


    # Pattern e filtri
    enable_long=True,
    pattern_long="P13",
    pattern_exclusion_long="EL2",
    pattern_vol_long="V4",

    enable_short=False,
    pattern_short="PS3",
    pattern_exclusion_short="ES4",
    pattern_vol_short="VS1",


    # Uscite temporali
    exit_eod=True,
    exit_eow=True,
    bars_exit_long=100,
    bars_exit_short=100,


    # risk model ALL-IN (PnL $)
    sl_dollars_long=1000.0,
    tp_dollars_long=3000.0,
    sl_dollars_short=200.0,
    tp_dollars_short=300.0,


    # Facoltativi
    name="BreakoutReversalTest"
    # commission_per_share=0.0,
    # slippage_per_share=0.0,
)

engine = TradeEngine(config, daily_df=daily_df, intraday_df=intraday_df)
results = engine.run()

generate_report(results, initial_equity=config.initial_capital)

print(f"\n✅ Esecuzione completata — {len(results)} trade generati.\n")

results.to_csv("results/trades_output.csv", index=False)
