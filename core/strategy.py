from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class StrategyConfig:
    # === Parametri di base ===
    initial_capital: float
    session_start: int  # es. 930 per 09:30
    session_end: int    # es. 1600 per 16:00

    # === Pattern e filtri ===
    enable_long: bool
    enable_short: bool
    pattern_long: Optional[str] = None
    pattern_exclusion_long: Optional[str] = None
    pattern_vol_long: Optional[str] = None
    pattern_short: Optional[str] = None
    pattern_exclusion_short: Optional[str] = None
    pattern_vol_short: Optional[str] = None

    # === Uscite temporali ===
    bars_exit_long: int = 999999
    bars_exit_short: int = 999999
    exit_eod: bool = False
    exit_eow: bool = False

    # === Risk model ALL-IN con SL/TP in $ ===
    sl_dollars_long: float = 0.0
    tp_dollars_long: float = 0.0
    sl_dollars_short: float = 0.0
    tp_dollars_short: float = 0.0

    # Facoltativo: nome strategia
    name: str = "Strategy"

    def __post_init__(self):
        if self.initial_capital <= 0:
            raise ValueError("initial_capital must be > 0")
        if not (0 <= self.session_start <= 2359 and 0 <= self.session_end <= 2359):
            raise ValueError("session_* must be HHMM in [0000, 2359]")
        if self.session_start > self.session_end:
            raise ValueError("session_start must be <= session_end")
        for v in (self.sl_dollars_long, self.tp_dollars_long,
                  self.sl_dollars_short, self.tp_dollars_short):
            if v < 0:
                raise ValueError("SL/TP dollars must be >= 0")
        if self.bars_exit_long < 1 or self.bars_exit_short < 1:
            raise ValueError("bars_exit_* must be >= 1")

    def to_dict(self) -> dict:
        return asdict(self)
