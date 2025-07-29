import pandas as pd
from core.strategy import StrategyConfig
from core.trade_engine import TradeEngine
from data.data_loader import load_data
from core.report_generator import generate_report

# === STEP 1: Carica i dati dal file ===
file_path = "data/@NQ_60_Minutes.txt"
intraday_df, daily_df = load_data(file_path)

# === STEP 2: Crea la configurazione della strategia ===
config = StrategyConfig(
    asset="NQ_FUTURE_TEST",
    pattern_long="P1",
    pattern_exclusion_long="EL2",
    pattern_vol_long="V1",

    pattern_short="PS3",
    pattern_exclusion_short="ES4",
    pattern_vol_short="VS1",

    session_start=930,      # 09:30
    session_end=1700,       # 17:00

    exit_eod=True,
    exit_eow=True,

    stop_loss_long=1.0,      # punti fissi, non %
    take_profit_long=3.0,
    bars_exit_long=10,

    stop_loss_short=1.0,
    take_profit_short=3.0,
    bars_exit_short=10,

    name="BreakoutReversalTest"
)

# === STEP 3: Esegui la strategia ===
engine = TradeEngine(config, daily_df=daily_df, intraday_df=intraday_df)
results = engine.run()

# Genera il report
generate_report(results)

# === STEP 4: Visualizza e salva i risultati ===
print(f"\n✅ Esecuzione completata — {len(results)} trade generati.\n")

# Salvataggio opzionale
results.to_csv("results/trades_output.csv", index=False)
