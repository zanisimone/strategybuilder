from dataclasses import dataclass
from typing import List

@dataclass
class StrategyConfig:
    asset: str

    # Pattern Long
    pattern_long: str
    pattern_exclusion_long: str
    pattern_vol_long: str

    # Pattern Short
    pattern_short: str
    pattern_exclusion_short: str
    pattern_vol_short: str

    # Orari di operatività (formato HHMM, es. 930 = 09:30)
    session_start: int
    session_end: int

    # Flag uscita fine giornata e settimana
    exit_eod: bool
    exit_eow: bool

    # Parametri long — moltiplicatori del rischio per trade (es: 2.0 = 2x rischio)
    stop_loss_long: float  # esempio: 1.0 = 1x rischio
    take_profit_long: float
    bars_exit_long: int

    # Parametri short — moltiplicatori del rischio per trade
    stop_loss_short: float
    take_profit_short: float
    bars_exit_short: int

    initial_capital: float = 100000.0         # Capitale iniziale
    risk_per_trade_pct: float = 0.01          # % rischio per trade (es. 0.01 = 1%)

    # Facoltativo: nome strategia
    name: str = "Strategy"

    def to_dict(self) -> dict:
        return self.__dict__
