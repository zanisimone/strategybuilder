import pandas as pd
import numpy as np
from core.trade_engine import TradeEngine
from core.strategy import StrategyConfig
from typing import Any, Union
from joblib import Parallel, delayed
import copy


# === MAPPATURE PER PATTERN ENUMERATI ===

PATTERN_ENUM_MAPS = {
    "pattern_long": {
    0: "P1", 1: "P2", 2: "P3", 3: "P4", 4: "P5", 5: "P6", 6: "P7", 7: "P8", 8: "P9", 9: "P10",
    10: "P11", 11: "P12", 12: "P13", 13: "P14", 14: "P15", 15: "P16", 16: "P17", 17: "P18", 18: "P19", 19: "P20",
    20: "P21", 21: "P22", 22: "P23", 23: "P24", 24: "P25", 25: "P26", 26: "P27", 27: "P28", 28: "P29", 29: "P30",
    30: "P31", 31: "P32", 32: "P33", 33: "P34", 34: "P35", 35: "P36", 36: "P37", 37: "P38", 38: "P39", 39: "P40",
    40: "P41", 41: "P42", 42: "P43", 43: "P44", 44: "P45", 45: "P46", 46: "P47", 47: "P48", 48: "P49", 49: "P50",
    50: "P51", 51: "P52", 52: "P53", 53: "P54", 54: "P55", 55: "P56", 56: "P57", 57: "P58", 58: "P59", 59: "P60",
    60: "P61", 61: "P62", 62: "P63", 63: "P64", 64: "P65", 65: "P66", 66: "P67", 67: "P68", 68: "P69", 69: "P70",
    70: "P71", 71: "P72", 72: "P73", 73: "P74", 74: "P75", 75: "P76", 76: "P77", 77: "P78", 78: "P79", 79: "P80",
    80: "P81", 81: "P82", 82: "P83", 83: "P84", 84: "P85", 85: "P86", 86: "P87", 87: "P88", 88: "P89", 89: "P90",
    90: "P91", 91: "P92", 92: "P93", 93: "P94", 94: "P95"
    },

    "pattern_exclusion_long": {
        0: "EL1", 1: "EL2", 2: "EL3", 3: "EL4", 4: "EL5", 5: "EL6", 6: "EL7", 7: "EL8", 8: "EL9", 9: "EL10",
        10: "EL11", 11: "EL12", 12: "EL13", 13: "EL14", 14: "EL15", 15: "EL16", 16: "EL17", 17: "EL18", 18: "EL19",
        19: "EL20",
        20: "EL21", 21: "EL22", 22: "EL23", 23: "EL24", 24: "EL25", 25: "EL26", 26: "EL27", 27: "EL28", 28: "EL29",
        29: "EL30",
        30: "EL31", 31: "EL32", 32: "EL33", 33: "EL34", 34: "EL35", 35: "EL36", 36: "EL37", 37: "EL38", 38: "EL39",
        39: "EL40",
        40: "EL41", 41: "EL42", 42: "EL43", 43: "EL44", 44: "EL45", 45: "EL46", 46: "EL47", 47: "EL48", 48: "EL49",
        49: "EL50",
        50: "EL51", 51: "EL52", 52: "EL53", 53: "EL54", 54: "EL55", 55: "EL56", 56: "EL57", 57: "EL58", 58: "EL59",
        59: "EL60",
        60: "EL61", 61: "EL62", 62: "EL63", 63: "EL64", 64: "EL65", 65: "EL66", 66: "EL67", 67: "EL68", 68: "EL69",
        69: "EL70",
        70: "EL71", 71: "EL72", 72: "EL73", 73: "EL74", 74: "EL75", 75: "EL76", 76: "EL77", 77: "EL78", 78: "EL79",
        79: "EL80",
        80: "EL81", 81: "EL82", 82: "EL83", 83: "EL84", 84: "EL85", 85: "EL86", 86: "EL87", 87: "EL88", 88: "EL89",
        89: "EL90",
        90: "EL91", 91: "EL92", 92: "EL93", 93: "EL94", 94: "EL95"
    },

    "pattern_vol_long": {
    0: "V1", 1: "V2", 2: "V3", 3: "V4", 4: "V5", 5: "V6", 6: "V7", 7: "V8", 8: "V9", 9: "V10",
    10: "V11", 11: "V12", 12: "V13", 13: "V14", 14: "V15", 15: "V16", 16: "V17", 17: "V18", 18: "V19", 19: "V20",
    20: "V21", 21: "V22", 22: "V23", 23: "V24", 24: "V25", 25: "V26", 26: "V27"
    },

    "pattern_short": {
    0: "PS1", 1: "PS2", 2: "PS3", 3: "PS4", 4: "PS5", 5: "PS6", 6: "PS7", 7: "PS8", 8: "PS9", 9: "PS10",
    10: "PS11", 11: "PS12", 12: "PS13", 13: "PS14", 14: "PS15", 15: "PS16", 16: "PS17", 17: "PS18", 18: "PS19", 19: "PS20",
    20: "PS21", 21: "PS22", 22: "PS23", 23: "PS24", 24: "PS25", 25: "PS26", 26: "PS27", 27: "PS28", 28: "PS29", 29: "PS30",
    30: "PS31", 31: "PS32", 32: "PS33", 33: "PS34", 34: "PS35", 35: "PS36", 36: "PS37", 37: "PS38", 38: "PS39", 39: "PS40",
    40: "PS41", 41: "PS42", 42: "PS43", 43: "PS44", 44: "PS45", 45: "PS46", 46: "PS47", 47: "PS48", 48: "PS49", 49: "PS50",
    50: "PS51", 51: "PS52", 52: "PS53", 53: "PS54", 54: "PS55", 55: "PS56", 56: "PS57", 57: "PS58", 58: "PS59", 59: "PS60",
    60: "PS61", 61: "PS62", 62: "PS63", 63: "PS64", 64: "PS65", 65: "PS66", 66: "PS67", 67: "PS68", 68: "PS69", 69: "PS70",
    70: "PS71", 71: "PS72", 72: "PS73", 73: "PS74", 74: "PS75", 75: "PS76", 76: "PS77", 77: "PS78", 78: "PS79", 79: "PS80",
    80: "PS81", 81: "PS82", 82: "PS83", 83: "PS84", 84: "PS85", 85: "PS86", 86: "PS87", 87: "PS88", 88: "PS89", 89: "PS90",
    90: "PS91", 91: "PS92", 92: "PS93", 93: "PS94", 94: "PS95"
    },

    "pattern_exclusion_short": {
    0: "ES1", 1: "ES2", 2: "ES3", 3: "ES4", 4: "ES5", 5: "ES6", 6: "ES7", 7: "ES8", 8: "ES9", 9: "ES10",
    10: "ES11", 11: "ES12", 12: "ES13", 13: "ES14", 14: "ES15", 15: "ES16", 16: "ES17", 17: "ES18", 18: "ES19", 19: "ES20",
    20: "ES21", 21: "ES22", 22: "ES23", 23: "ES24", 24: "ES25", 25: "ES26", 26: "ES27", 27: "ES28", 28: "ES29", 29: "ES30",
    30: "ES31", 31: "ES32", 32: "ES33", 33: "ES34", 34: "ES35", 35: "ES36", 36: "ES37", 37: "ES38", 38: "ES39", 39: "ES40",
    40: "ES41", 41: "ES42", 42: "ES43", 43: "ES44", 44: "ES45", 45: "ES46", 46: "ES47", 47: "ES48", 48: "ES49", 49: "ES50",
    50: "ES51", 51: "ES52", 52: "ES53", 53: "ES54", 54: "ES55", 55: "ES56", 56: "ES57", 57: "ES58", 58: "ES59", 59: "ES60",
    60: "ES61", 61: "ES62", 62: "ES63", 63: "ES64", 64: "ES65", 65: "ES66", 66: "ES67", 67: "ES68", 68: "ES69", 69: "ES70",
    70: "ES71", 71: "ES72", 72: "ES73", 73: "ES74", 74: "ES75", 75: "ES76", 76: "ES77", 77: "ES78", 78: "ES79", 79: "ES80",
    80: "ES81", 81: "ES82", 82: "ES83", 83: "ES84", 84: "ES85", 85: "ES86", 86: "ES87", 87: "ES88", 88: "ES89", 89: "ES90",
    90: "ES91", 91: "ES92", 92: "ES93", 93: "ES94", 94: "ES95"
    },

    "pattern_vol_short": {
    0: "VS1", 1: "VS2", 2: "VS3", 3: "VS4", 4: "VS5", 5: "VS6", 6: "VS7", 7: "VS8", 8: "VS9", 9: "VS10",
    10: "VS11", 11: "VS12", 12: "VS13", 13: "VS14", 14: "VS15", 15: "VS16", 16: "VS17", 17: "VS18", 18: "VS19", 19: "VS20",
    20: "VS21", 21: "VS22", 22: "VS23", 23: "VS24", 24: "VS25", 25: "VS26", 26: "VS27"
    }

}


def optimize_parameter(
    config: StrategyConfig,
    param_name: str,
    values: Union[list[Any], None] = None,
    start: float = None,
    end: float = None,
    step: float = None,
    daily_df: pd.DataFrame = None,
    intraday_df: pd.DataFrame = None,
    pattern_mapping: dict[int, str] = None
) -> pd.DataFrame:
    if values is None:
        if any(v is None for v in [start, end, step]):
            raise ValueError("Specifica 'values' oppure 'start', 'end', 'step'")

        if pattern_mapping is None and param_name in PATTERN_ENUM_MAPS:
            pattern_mapping = PATTERN_ENUM_MAPS[param_name]

        if pattern_mapping:
            indices = list(range(int(start), int(end) + 1, int(step)))
            values = [pattern_mapping[i] for i in indices if i in pattern_mapping]
        else:
            values = np.arange(start, end + step, step).round(6)

    total_values = len(values)
    print(f"\n🔍 Ottimizzazione parametro: {param_name} su {total_values} valori (in parallelo)")

    def evaluate_config(val, idx):
        print(f"🔄 {idx + 1}/{total_values} ({100 * (idx + 1) // total_values}%) – valore: {val}")
        config_copy = copy.deepcopy(config)
        setattr(config_copy, param_name, val)

        engine = TradeEngine(config_copy, daily_df, intraday_df)
        trades = engine.run()

        if not trades.empty and "pnl" in trades.columns:
            net_profit = trades["pnl"].sum()
            avg_trade = trades["pnl"].mean()
            win_rate = len(trades[trades["pnl"] > 0]) / len(trades) * 100
            max_dd = (trades["pnl"].cumsum().cummax() - trades["pnl"].cumsum()).max()
            total_trades = len(trades)
        else:
            net_profit = 0
            avg_trade = 0
            win_rate = 0
            max_dd = 0
            total_trades = 0

        return {
            param_name: val,
            "NetProfit": net_profit,
            "AvgTrade": avg_trade,
            "WinRate": win_rate,
            "MaxDrawdown": max_dd,
            "Trades": total_trades
        }

    results = Parallel(n_jobs=-1)(
        delayed(evaluate_config)(val, idx) for idx, val in enumerate(values)
    )

    return pd.DataFrame(results)


def generate_text_report(df: pd.DataFrame, param_name: str, output_path: str = "results"):
    import os
    os.makedirs(output_path, exist_ok=True)

    if df.empty:
        print("⚠️ Nessun risultato da analizzare.")
        return

    best = df.sort_values("NetProfit", ascending=False).iloc[0]
    report_lines = []

    report_lines.append(f"# 🔍 Report Ottimizzazione — Parametro: {param_name}\n")
    report_lines.append(f"**Totale configurazioni testate**: {len(df)}")
    report_lines.append(f"**Miglior valore**: {best[param_name]}\n")

    report_lines.append("## 📈 Metriche Migliore Configurazione:")
    report_lines.append(f"- Net Profit        : {best['NetProfit']:.2f}")
    report_lines.append(f"- Average Trade     : {best['AvgTrade']:.2f}")
    report_lines.append(f"- Win Rate          : {best['WinRate']:.2f}%")
    report_lines.append(f"- Max Drawdown      : {best['MaxDrawdown']:.2f}")
    if best['NetProfit'] != 0:
        report_lines.append(f"- Max Drawdown %    : {100 * best['MaxDrawdown'] / abs(best['NetProfit']):.2f}%")
    report_lines.append(f"- Profit Factor     : {best['NetProfit'] / abs(best['MaxDrawdown']) if best['MaxDrawdown'] != 0 else 'Inf'}")
    report_lines.append(f"- Expectancy        : {best['AvgTrade']:.2f}")
    if best['WinRate'] > 0 and best['WinRate'] < 100:
        win_ratio = best['WinRate'] / (100 - best['WinRate'])
        report_lines.append(f"- Win/Loss Ratio    : {win_ratio:.2f}")

    report_lines.append("\n## 🧾 Tutti i risultati (primi 10):")
    for i, row in df.sort_values("NetProfit", ascending=False).head(10).iterrows():
        report_lines.append(f"- {param_name} = {row[param_name]} → NetProfit = {row['NetProfit']:.2f}, Trades = {int(row['Trades'])}")

    # Salvataggio
    file_path = os.path.join(output_path, f"report_optimization_{param_name}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print(f"📄 Report testuale salvato in: {file_path}")

