from core.strategy import StrategyConfig
from core.optimizer import optimize_parameter, generate_text_report, PATTERN_ENUM_MAPS
from data.data_loader import load_data

file_path = "data/@NQ_60_Minutes.txt"
intraday_df, daily_df = load_data(file_path)

parametro = "pattern_long"  # Cambia qui: es. pattern_long, pattern_short, ecc.

start = 11
end = 13
step = 1

config = StrategyConfig(
    asset="NQ",
    enable_long=True,
    enable_short=True,
    pattern_long="P1",
    pattern_exclusion_long="EL1",
    pattern_vol_long="V1",
    pattern_short="PS1",
    pattern_exclusion_short="ES1",
    pattern_vol_short="VS1",
    session_start=930,
    session_end=1700,
    exit_eod=True,
    exit_eow=True,
    stop_loss_long=1.0,
    take_profit_long=3.0,
    bars_exit_long=10,
    stop_loss_short=1.0,
    take_profit_short=3.0,
    bars_exit_short=10,
    initial_capital=100000.0,
    risk_per_trade_pct=0.01,
)

results = optimize_parameter(
    config=config,
    param_name=parametro,
    start=start,
    end=end,
    step=step,
    daily_df=daily_df,
    intraday_df=intraday_df
)

print(f"\n📊 Risultati ottimizzazione su {parametro}:")
print(results)

results.to_csv(f"results/optimization_{parametro}.csv", index=False)
generate_text_report(results, parametro)
