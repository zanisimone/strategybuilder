import numpy as np
import pandas as pd

# === Helper Functions ===
def abs_value(x):
    return abs(x)

def max_list(*args):
    return max(args)

def min_list(*args):
    return min(args)


# === PatternLong ===
def P1(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(1).iloc[i] - daily_df['Close'].shift(1).iloc[i]) < \
           0.1 * (daily_df['High'].shift(1).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P2(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(1).iloc[i] - daily_df['Close'].shift(1).iloc[i]) > \
           0.9 * (daily_df['High'].shift(1).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P3(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) < \
           0.1 * (daily_df['High'].shift(5).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P4(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) > \
           2.5 * (daily_df['High'].shift(5).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P5(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) < \
           0.1 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P6(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) < \
           0.25 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P7(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) < \
           0.5 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P8(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) < \
           0.75 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P9(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) > \
           0.9 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P10(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) > \
           0.25 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P11(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) > \
           0.5 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P12(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) > \
           0.75 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P13(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] > daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*0.5*0.01

def P14(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] > daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*0.75*0.01

def P15(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] > daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*1.0*0.01

def P16(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] > daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*1.5*0.01

def P17(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] > daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*2.0*0.01

def P18(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] > daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*2.5*0.01

def P19(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] > daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*3.0*0.01

def P20(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] < daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*0.5*0.01

def P21(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] < daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*0.75*0.01

def P22(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] < daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*1.0*0.01

def P23(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(1).iloc[i] - daily_df['Close'].shift(1).iloc[i]) < \
           0.5 * (daily_df['High'].shift(1).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P24(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(1).iloc[i] - daily_df['Close'].shift(5).iloc[i]) < \
           0.5 * (daily_df['High'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i])

def P25(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) < \
           0.5 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P26(daily_df: pd.DataFrame, i: int) -> bool:
    return (daily_df['High'].iloc[i] - daily_df['Open'].iloc[i]) > 1.0 * (daily_df['High'].shift(1).iloc[i] - daily_df['Open'].shift(1).iloc[i])

def P27(daily_df: pd.DataFrame, i: int) -> bool:
    return (daily_df['High'].iloc[i] - daily_df['Open'].iloc[i]) > 1.5 * (daily_df['High'].shift(1).iloc[i] - daily_df['Open'].shift(1).iloc[i])

def P28(daily_df: pd.DataFrame, i: int) -> bool:
    return (daily_df['Open'].iloc[i] - daily_df['Low'].iloc[i]) > 1.0 * (daily_df['Open'].shift(1).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P29(daily_df: pd.DataFrame, i: int) -> bool:
    return (daily_df['Open'].iloc[i] - daily_df['Low'].iloc[i]) > 1.5 * (daily_df['Open'].shift(1).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P30(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] > daily_df['Close'].shift(2).iloc[i] and \
           daily_df['Close'].shift(2).iloc[i] > daily_df['Close'].shift(3).iloc[i] and \
           daily_df['Close'].shift(3).iloc[i] > daily_df['Close'].shift(4).iloc[i]

def P31(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] < daily_df['Close'].shift(2).iloc[i] and \
           daily_df['Close'].shift(2).iloc[i] < daily_df['Close'].shift(3).iloc[i] and \
           daily_df['Close'].shift(3).iloc[i] < daily_df['Close'].shift(4).iloc[i]

def P32(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].shift(1).iloc[i] > daily_df['High'].shift(2).iloc[i] and \
           daily_df['Low'].shift(1).iloc[i] > daily_df['Low'].shift(2).iloc[i]

def P33(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].shift(1).iloc[i] < daily_df['High'].shift(2).iloc[i] and \
           daily_df['Low'].shift(1).iloc[i] < daily_df['Low'].shift(2).iloc[i]

def P34(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] > daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*0.75/100

def P35(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] < daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*0.75/100

def P36(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] > daily_df['Close'].shift(2).iloc[i]

def P37(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] < daily_df['Close'].shift(2).iloc[i]

def P38(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] < daily_df['Open'].shift(1).iloc[i]

def P39(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] > daily_df['Open'].shift(1).iloc[i]

def P40(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] < daily_df['Close'].shift(2).iloc[i] - daily_df['Close'].shift(2).iloc[i]*0.5/100

def P41(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] > daily_df['Close'].shift(2).iloc[i] + daily_df['Close'].shift(2).iloc[i]*0.5/100

def P42(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] > daily_df['High'].shift(1).iloc[i]

def P43(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].shift(1).iloc[i] > daily_df['High'].shift(5).iloc[i]

def P44(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Low'].iloc[i] < daily_df['Low'].shift(1).iloc[i]

def P45(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Low'].shift(1).iloc[i] < daily_df['Low'].shift(5).iloc[i]

def P46(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].shift(1).iloc[i] > daily_df['High'].shift(2).iloc[i] and \
           daily_df['High'].shift(1).iloc[i] > daily_df['High'].shift(3).iloc[i] and \
           daily_df['High'].shift(1).iloc[i] > daily_df['High'].shift(4).iloc[i]

def P47(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].shift(1).iloc[i] < daily_df['High'].shift(2).iloc[i] and \
           daily_df['High'].shift(1).iloc[i] < daily_df['High'].shift(3).iloc[i] and \
           daily_df['High'].shift(1).iloc[i] < daily_df['High'].shift(4).iloc[i]

def P48(daily_df: pd.DataFrame, i: int) -> bool:
    return True

def P49(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(1).iloc[i] - daily_df['Close'].shift(1).iloc[i]) >= \
           0.1 * (daily_df['High'].shift(1).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P50(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(1).iloc[i] - daily_df['Close'].shift(1).iloc[i]) <= \
           0.9 * (daily_df['High'].shift(1).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P51(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) >= \
           0.1 * (daily_df['High'].shift(5).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P52(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) <= \
           2.5 * (daily_df['High'].shift(5).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P53(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) >= \
           0.1 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P54(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) >= \
           0.25 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P55(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) >= \
           0.5 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P56(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) >= \
           0.75 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P57(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) <= \
           0.9 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P58(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) <= \
           0.25 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P59(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) <= \
           0.5 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P60(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) <= \
           0.75 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P61(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] <= daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*0.5*0.01

def P62(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] <= daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*0.75*0.01

def P63(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] <= daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*1.0*0.01

def P64(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] <= daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*1.5*0.01

def P65(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] <= daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*2.0*0.01

def P66(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] <= daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*2.5*0.01

def P67(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] <= daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*3.0*0.01

def P68(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] >= daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*0.5*0.01

def P69(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] >= daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*0.75*0.01

def P70(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] >= daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*1.0*0.01

def P71(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(1).iloc[i] - daily_df['Close'].shift(1).iloc[i]) >= \
           0.5 * (daily_df['High'].shift(1).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P72(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(1).iloc[i] - daily_df['Close'].shift(5).iloc[i]) >= \
           0.5 * (daily_df['High'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i])

def P73(daily_df: pd.DataFrame, i: int) -> bool:
    return abs_value(daily_df['Open'].shift(5).iloc[i] - daily_df['Close'].shift(1).iloc[i]) >= \
           0.5 * (max_list(
                daily_df['High'].shift(1).iloc[i],
                daily_df['High'].shift(2).iloc[i],
                daily_df['High'].shift(3).iloc[i],
                daily_df['High'].shift(4).iloc[i],
                daily_df['High'].shift(5).iloc[i]) -
                min_list(
                daily_df['Low'].shift(1).iloc[i],
                daily_df['Low'].shift(2).iloc[i],
                daily_df['Low'].shift(3).iloc[i],
                daily_df['Low'].shift(4).iloc[i],
                daily_df['Low'].shift(5).iloc[i]))

def P74(daily_df: pd.DataFrame, i: int) -> bool:
    return (daily_df['High'].iloc[i] - daily_df['Open'].iloc[i]) <= 1.0 * (daily_df['High'].shift(1).iloc[i] - daily_df['Open'].shift(1).iloc[i])

def P75(daily_df: pd.DataFrame, i: int) -> bool:
    return (daily_df['High'].iloc[i] - daily_df['Open'].iloc[i]) <= 1.5 * (daily_df['High'].shift(1).iloc[i] - daily_df['Open'].shift(1).iloc[i])

def P76(daily_df: pd.DataFrame, i: int) -> bool:
    return (daily_df['High'].iloc[i] - daily_df['Open'].iloc[i]) <= 1.0 * (daily_df['High'].shift(1).iloc[i] - daily_df['Open'].shift(1).iloc[i])

def P77(daily_df: pd.DataFrame, i: int) -> bool:
    return (daily_df['High'].iloc[i] - daily_df['Open'].iloc[i]) <= 1.5 * (daily_df['High'].shift(1).iloc[i] - daily_df['Open'].shift(1).iloc[i])

def P78(daily_df: pd.DataFrame, i: int) -> bool:
    return (daily_df['Open'].iloc[i] - daily_df['Low'].iloc[i]) <= 1.0 * (daily_df['Open'].shift(1).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P79(daily_df: pd.DataFrame, i: int) -> bool:
    return (daily_df['Open'].iloc[i] - daily_df['Low'].iloc[i]) <= 1.5 * (daily_df['Open'].shift(1).iloc[i] - daily_df['Low'].shift(1).iloc[i])

def P80(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] <= daily_df['Close'].shift(2).iloc[i] or \
           daily_df['Close'].shift(2).iloc[i] <= daily_df['Close'].shift(3).iloc[i] or \
           daily_df['Close'].shift(3).iloc[i] <= daily_df['Close'].shift(4).iloc[i]

def P81(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] >= daily_df['Close'].shift(2).iloc[i] or \
           daily_df['Close'].shift(2).iloc[i] >= daily_df['Close'].shift(3).iloc[i] or \
           daily_df['Close'].shift(3).iloc[i] >= daily_df['Close'].shift(4).iloc[i]

def P82(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].shift(1).iloc[i] <= daily_df['High'].shift(2).iloc[i] or \
           daily_df['Low'].shift(1).iloc[i] <= daily_df['Low'].shift(2).iloc[i]

def P83(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].shift(1).iloc[i] >= daily_df['High'].shift(2).iloc[i] or \
           daily_df['Low'].shift(1).iloc[i] >= daily_df['Low'].shift(2).iloc[i]

def P84(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] <= daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*0.75/100

def P85(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] >= daily_df['Low'].iloc[i] + daily_df['Low'].iloc[i]*0.75/100

def P86(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] <= daily_df['Close'].shift(2).iloc[i]

def P87(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] >= daily_df['Close'].shift(2).iloc[i]

def P88(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] >= daily_df['Open'].shift(1).iloc[i]

def P89(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] <= daily_df['Open'].shift(1).iloc[i]

def P90(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] >= daily_df['Close'].shift(2).iloc[i] + daily_df['Close'].shift(2).iloc[i]*0.5/100

def P91(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Close'].shift(1).iloc[i] <= daily_df['Close'].shift(2).iloc[i] - daily_df['Close'].shift(2).iloc[i]*0.5/100

def P92(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].iloc[i] <= daily_df['High'].shift(1).iloc[i]

def P93(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['High'].shift(1).iloc[i] <= daily_df['High'].shift(5).iloc[i]

def P94(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Low'].iloc[i] >= daily_df['Low'].shift(1).iloc[i]

def P95(daily_df: pd.DataFrame, i: int) -> bool:
    return daily_df['Low'].shift(1).iloc[i] >= daily_df['Low'].shift(5).iloc[i]


# === PatternShort ===
def PS1(daily_df: pd.DataFrame, i: int) -> bool:
    return P1(daily_df, i)  

def PS2(daily_df: pd.DataFrame, i: int) -> bool:
    return P2(daily_df, i)  

def PS3(daily_df: pd.DataFrame, i: int) -> bool:
    return P3(daily_df, i)

def PS4(daily_df: pd.DataFrame, i: int) -> bool:
    return P4(daily_df, i)

def PS5(daily_df: pd.DataFrame, i: int) -> bool:
    return P5(daily_df, i)

def PS6(daily_df: pd.DataFrame, i: int) -> bool:
    return P6(daily_df, i)

def PS7(daily_df: pd.DataFrame, i: int) -> bool:
    return P7(daily_df, i)

def PS8(daily_df: pd.DataFrame, i: int) -> bool:
    return P8(daily_df, i)

def PS9(daily_df: pd.DataFrame, i: int) -> bool:
    return P9(daily_df, i)

def PS10(daily_df: pd.DataFrame, i: int) -> bool:
    return P10(daily_df, i)

def PS11(daily_df: pd.DataFrame, i: int) -> bool:
    return P11(daily_df, i)

def PS12(daily_df: pd.DataFrame, i: int) -> bool:
    return P12(daily_df, i)

def PS13(daily_df: pd.DataFrame, i: int) -> bool:
    return P13(daily_df, i)

def PS14(daily_df: pd.DataFrame, i: int) -> bool:
    return P14(daily_df, i)

def PS15(daily_df: pd.DataFrame, i: int) -> bool:
    return P15(daily_df, i)

def PS16(daily_df: pd.DataFrame, i: int) -> bool:
    return P16(daily_df, i)

def PS17(daily_df: pd.DataFrame, i: int) -> bool:
    return P17(daily_df, i)

def PS18(daily_df: pd.DataFrame, i: int) -> bool:
    return P18(daily_df, i)

def PS19(daily_df: pd.DataFrame, i: int) -> bool:
    return P19(daily_df, i)

def PS20(daily_df: pd.DataFrame, i: int) -> bool:
    return P20(daily_df, i)

def PS21(daily_df: pd.DataFrame, i: int) -> bool:
    return P21(daily_df, i)

def PS22(daily_df: pd.DataFrame, i: int) -> bool:
    return P22(daily_df, i)

def PS23(daily_df: pd.DataFrame, i: int) -> bool:
    return P23(daily_df, i)

def PS24(daily_df: pd.DataFrame, i: int) -> bool:
    return P24(daily_df, i)

def PS25(daily_df: pd.DataFrame, i: int) -> bool:
    return P25(daily_df, i)

def PS26(daily_df: pd.DataFrame, i: int) -> bool:
    return P26(daily_df, i)

def PS27(daily_df: pd.DataFrame, i: int) -> bool:
    return P27(daily_df, i)

def PS28(daily_df: pd.DataFrame, i: int) -> bool:
    return P28(daily_df, i)

def PS29(daily_df: pd.DataFrame, i: int) -> bool:
    return P29(daily_df, i)

def PS30(daily_df: pd.DataFrame, i: int) -> bool:
    return P30(daily_df, i)

def PS31(daily_df: pd.DataFrame, i: int) -> bool:
    return P31(daily_df, i)

def PS32(daily_df: pd.DataFrame, i: int) -> bool:
    return P32(daily_df, i)

def PS33(daily_df: pd.DataFrame, i: int) -> bool:
    return P33(daily_df, i)

def PS34(daily_df: pd.DataFrame, i: int) -> bool:
    return P34(daily_df, i)

def PS35(daily_df: pd.DataFrame, i: int) -> bool:
    return P35(daily_df, i)

def PS36(daily_df: pd.DataFrame, i: int) -> bool:
    return P36(daily_df, i)

def PS37(daily_df: pd.DataFrame, i: int) -> bool:
    return P37(daily_df, i)

def PS38(daily_df: pd.DataFrame, i: int) -> bool:
    return P38(daily_df, i)

def PS39(daily_df: pd.DataFrame, i: int) -> bool:
    return P39(daily_df, i)

def PS40(daily_df: pd.DataFrame, i: int) -> bool:
    return P40(daily_df, i)

def PS41(daily_df: pd.DataFrame, i: int) -> bool:
    return P41(daily_df, i)

def PS42(daily_df: pd.DataFrame, i: int) -> bool:
    return P42(daily_df, i)

def PS43(daily_df: pd.DataFrame, i: int) -> bool:
    return P43(daily_df, i)

def PS44(daily_df: pd.DataFrame, i: int) -> bool:
    return P44(daily_df, i)

def PS45(daily_df: pd.DataFrame, i: int) -> bool:
    return P45(daily_df, i)

def PS46(daily_df: pd.DataFrame, i: int) -> bool:
    return P46(daily_df, i)

def PS47(daily_df: pd.DataFrame, i: int) -> bool:
    return P47(daily_df, i)

def PS48(daily_df: pd.DataFrame, i: int) -> bool:
    return P48(daily_df, i)

def PS49(daily_df: pd.DataFrame, i: int) -> bool:
    return P49(daily_df, i)

def PS50(daily_df: pd.DataFrame, i: int) -> bool:
    return P50(daily_df, i)

def PS51(daily_df: pd.DataFrame, i: int) -> bool:
    return P51(daily_df, i)

def PS52(daily_df: pd.DataFrame, i: int) -> bool:
    return P52(daily_df, i)

def PS53(daily_df: pd.DataFrame, i: int) -> bool:
    return P53(daily_df, i)

def PS54(daily_df: pd.DataFrame, i: int) -> bool:
    return P54(daily_df, i)

def PS55(daily_df: pd.DataFrame, i: int) -> bool:
    return P55(daily_df, i)

def PS56(daily_df: pd.DataFrame, i: int) -> bool:
    return P56(daily_df, i)

def PS57(daily_df: pd.DataFrame, i: int) -> bool:
    return P57(daily_df, i)

def PS58(daily_df: pd.DataFrame, i: int) -> bool:
    return P58(daily_df, i)

def PS59(daily_df: pd.DataFrame, i: int) -> bool:
    return P59(daily_df, i)

def PS60(daily_df: pd.DataFrame, i: int) -> bool:
    return P60(daily_df, i)

def PS61(daily_df: pd.DataFrame, i: int) -> bool:
    return P61(daily_df, i)

def PS62(daily_df: pd.DataFrame, i: int) -> bool:
    return P62(daily_df, i)

def PS63(daily_df: pd.DataFrame, i: int) -> bool:
    return P63(daily_df, i)

def PS64(daily_df: pd.DataFrame, i: int) -> bool:
    return P64(daily_df, i)

def PS65(daily_df: pd.DataFrame, i: int) -> bool:
    return P65(daily_df, i)

def PS66(daily_df: pd.DataFrame, i: int) -> bool:
    return P66(daily_df, i)

def PS67(daily_df: pd.DataFrame, i: int) -> bool:
    return P67(daily_df, i)

def PS68(daily_df: pd.DataFrame, i: int) -> bool:
    return P68(daily_df, i)

def PS69(daily_df: pd.DataFrame, i: int) -> bool:
    return P69(daily_df, i)

def PS70(daily_df: pd.DataFrame, i: int) -> bool:
    return P70(daily_df, i)

def PS71(daily_df: pd.DataFrame, i: int) -> bool:
    return P71(daily_df, i)

def PS72(daily_df: pd.DataFrame, i: int) -> bool:
    return P72(daily_df, i)

def PS73(daily_df: pd.DataFrame, i: int) -> bool:
    return P73(daily_df, i)

def PS74(daily_df: pd.DataFrame, i: int) -> bool:
    return P74(daily_df, i)

def PS75(daily_df: pd.DataFrame, i: int) -> bool:
    return P75(daily_df, i)

def PS76(daily_df: pd.DataFrame, i: int) -> bool:
    return P76(daily_df, i)

def PS77(daily_df: pd.DataFrame, i: int) -> bool:
    return P77(daily_df, i)

def PS78(daily_df: pd.DataFrame, i: int) -> bool:
    return P78(daily_df, i)

def PS79(daily_df: pd.DataFrame, i: int) -> bool:
    return P79(daily_df, i)

def PS80(daily_df: pd.DataFrame, i: int) -> bool:
    return P80(daily_df, i)

def PS81(daily_df: pd.DataFrame, i: int) -> bool:
    return P81(daily_df, i)

def PS82(daily_df: pd.DataFrame, i: int) -> bool:
    return P82(daily_df, i)

def PS83(daily_df: pd.DataFrame, i: int) -> bool:
    return P83(daily_df, i)

def PS84(daily_df: pd.DataFrame, i: int) -> bool:
    return P84(daily_df, i)

def PS85(daily_df: pd.DataFrame, i: int) -> bool:
    return P85(daily_df, i)

def PS86(daily_df: pd.DataFrame, i: int) -> bool:
    return P86(daily_df, i)

def PS87(daily_df: pd.DataFrame, i: int) -> bool:
    return P87(daily_df, i)

def PS88(daily_df: pd.DataFrame, i: int) -> bool:
    return P88(daily_df, i)

def PS89(daily_df: pd.DataFrame, i: int) -> bool:
    return P89(daily_df, i)

def PS90(daily_df: pd.DataFrame, i: int) -> bool:
    return P90(daily_df, i)

def PS91(daily_df: pd.DataFrame, i: int) -> bool:
    return P91(daily_df, i)

def PS92(daily_df: pd.DataFrame, i: int) -> bool:
    return P92(daily_df, i)

def PS93(daily_df: pd.DataFrame, i: int) -> bool:
    return P93(daily_df, i)

def PS94(daily_df: pd.DataFrame, i: int) -> bool:
    return P94(daily_df, i)

def PS95(daily_df: pd.DataFrame, i: int) -> bool:
    return P95(daily_df, i)


# === PatternEsclusioneLong ===
def EL1(daily_df: pd.DataFrame, i: int) -> bool:
    return P1(daily_df, i)

def EL2(daily_df: pd.DataFrame, i: int) -> bool:
    return P2(daily_df, i)

def EL3(daily_df: pd.DataFrame, i: int) -> bool:
    return P3(daily_df, i)

def EL4(daily_df: pd.DataFrame, i: int) -> bool:
    return P4(daily_df, i)

def EL5(daily_df: pd.DataFrame, i: int) -> bool:
    return P5(daily_df, i)

def EL6(daily_df: pd.DataFrame, i: int) -> bool:
    return P6(daily_df, i)

def EL7(daily_df: pd.DataFrame, i: int) -> bool:
    return P7(daily_df, i)

def EL8(daily_df: pd.DataFrame, i: int) -> bool:
    return P8(daily_df, i)

def EL9(daily_df: pd.DataFrame, i: int) -> bool:
    return P9(daily_df, i)

def EL10(daily_df: pd.DataFrame, i: int) -> bool:
    return P10(daily_df, i)

def EL11(daily_df: pd.DataFrame, i: int) -> bool:
    return P11(daily_df, i)

def EL12(daily_df: pd.DataFrame, i: int) -> bool:
    return P12(daily_df, i)

def EL13(daily_df: pd.DataFrame, i: int) -> bool:
    return P13(daily_df, i)

def EL14(daily_df: pd.DataFrame, i: int) -> bool:
    return P14(daily_df, i)

def EL15(daily_df: pd.DataFrame, i: int) -> bool:
    return P15(daily_df, i)

def EL16(daily_df: pd.DataFrame, i: int) -> bool:
    return P16(daily_df, i)

def EL17(daily_df: pd.DataFrame, i: int) -> bool:
    return P17(daily_df, i)

def EL18(daily_df: pd.DataFrame, i: int) -> bool:
    return P18(daily_df, i)

def EL19(daily_df: pd.DataFrame, i: int) -> bool:
    return P19(daily_df, i)

def EL20(daily_df: pd.DataFrame, i: int) -> bool:
    return P20(daily_df, i)

def EL21(daily_df: pd.DataFrame, i: int) -> bool:
    return P21(daily_df, i)

def EL22(daily_df: pd.DataFrame, i: int) -> bool:
    return P22(daily_df, i)

def EL23(daily_df: pd.DataFrame, i: int) -> bool:
    return P23(daily_df, i)

def EL24(daily_df: pd.DataFrame, i: int) -> bool:
    return P24(daily_df, i)

def EL25(daily_df: pd.DataFrame, i: int) -> bool:
    return P25(daily_df, i)

def EL26(daily_df: pd.DataFrame, i: int) -> bool:
    return P26(daily_df, i)

def EL27(daily_df: pd.DataFrame, i: int) -> bool:
    return P27(daily_df, i)

def EL28(daily_df: pd.DataFrame, i: int) -> bool:
    return P28(daily_df, i)

def EL29(daily_df: pd.DataFrame, i: int) -> bool:
    return P29(daily_df, i)

def EL30(daily_df: pd.DataFrame, i: int) -> bool:
    return P30(daily_df, i)

def EL31(daily_df: pd.DataFrame, i: int) -> bool:
    return P31(daily_df, i)

def EL32(daily_df: pd.DataFrame, i: int) -> bool:
    return P32(daily_df, i)

def EL33(daily_df: pd.DataFrame, i: int) -> bool:
    return P33(daily_df, i)

def EL34(daily_df: pd.DataFrame, i: int) -> bool:
    return P34(daily_df, i)

def EL35(daily_df: pd.DataFrame, i: int) -> bool:
    return P35(daily_df, i)

def EL36(daily_df: pd.DataFrame, i: int) -> bool:
    return P36(daily_df, i)

def EL37(daily_df: pd.DataFrame, i: int) -> bool:
    return P37(daily_df, i)

def EL38(daily_df: pd.DataFrame, i: int) -> bool:
    return P38(daily_df, i)

def EL39(daily_df: pd.DataFrame, i: int) -> bool:
    return P39(daily_df, i)

def EL40(daily_df: pd.DataFrame, i: int) -> bool:
    return P40(daily_df, i)

def EL41(daily_df: pd.DataFrame, i: int) -> bool:
    return P41(daily_df, i)

def EL42(daily_df: pd.DataFrame, i: int) -> bool:
    return P42(daily_df, i)

def EL43(daily_df: pd.DataFrame, i: int) -> bool:
    return P43(daily_df, i)

def EL44(daily_df: pd.DataFrame, i: int) -> bool:
    return P44(daily_df, i)

def EL45(daily_df: pd.DataFrame, i: int) -> bool:
    return P45(daily_df, i)

def EL46(daily_df: pd.DataFrame, i: int) -> bool:
    return P46(daily_df, i)

def EL47(daily_df: pd.DataFrame, i: int) -> bool:
    return P47(daily_df, i)

def EL48(daily_df: pd.DataFrame, i: int) -> bool:
    return P48(daily_df, i)

def EL49(daily_df: pd.DataFrame, i: int) -> bool:
    return P49(daily_df, i)

def EL50(daily_df: pd.DataFrame, i: int) -> bool:
    return P50(daily_df, i)

def EL51(daily_df: pd.DataFrame, i: int) -> bool:
    return P51(daily_df, i)

def EL52(daily_df: pd.DataFrame, i: int) -> bool:
    return P52(daily_df, i)

def EL53(daily_df: pd.DataFrame, i: int) -> bool:
    return P53(daily_df, i)

def EL54(daily_df: pd.DataFrame, i: int) -> bool:
    return P54(daily_df, i)

def EL55(daily_df: pd.DataFrame, i: int) -> bool:
    return P55(daily_df, i)

def EL56(daily_df: pd.DataFrame, i: int) -> bool:
    return P56(daily_df, i)

def EL57(daily_df: pd.DataFrame, i: int) -> bool:
    return P57(daily_df, i)

def EL58(daily_df: pd.DataFrame, i: int) -> bool:
    return P58(daily_df, i)

def EL59(daily_df: pd.DataFrame, i: int) -> bool:
    return P59(daily_df, i)

def EL60(daily_df: pd.DataFrame, i: int) -> bool:
    return P60(daily_df, i)

def EL61(daily_df: pd.DataFrame, i: int) -> bool:
    return P61(daily_df, i)

def EL62(daily_df: pd.DataFrame, i: int) -> bool:
    return P62(daily_df, i)

def EL63(daily_df: pd.DataFrame, i: int) -> bool:
    return P63(daily_df, i)

def EL64(daily_df: pd.DataFrame, i: int) -> bool:
    return P64(daily_df, i)

def EL65(daily_df: pd.DataFrame, i: int) -> bool:
    return P65(daily_df, i)

def EL66(daily_df: pd.DataFrame, i: int) -> bool:
    return P66(daily_df, i)

def EL67(daily_df: pd.DataFrame, i: int) -> bool:
    return P67(daily_df, i)

def EL68(daily_df: pd.DataFrame, i: int) -> bool:
    return P68(daily_df, i)

def EL69(daily_df: pd.DataFrame, i: int) -> bool:
    return P69(daily_df, i)

def EL70(daily_df: pd.DataFrame, i: int) -> bool:
    return P70(daily_df, i)

def EL71(daily_df: pd.DataFrame, i: int) -> bool:
    return P71(daily_df, i)

def EL72(daily_df: pd.DataFrame, i: int) -> bool:
    return P72(daily_df, i)

def EL73(daily_df: pd.DataFrame, i: int) -> bool:
    return P73(daily_df, i)

def EL74(daily_df: pd.DataFrame, i: int) -> bool:
    return P74(daily_df, i)

def EL75(daily_df: pd.DataFrame, i: int) -> bool:
    return P75(daily_df, i)

def EL76(daily_df: pd.DataFrame, i: int) -> bool:
    return P76(daily_df, i)

def EL77(daily_df: pd.DataFrame, i: int) -> bool:
    return P77(daily_df, i)

def EL78(daily_df: pd.DataFrame, i: int) -> bool:
    return P78(daily_df, i)

def EL79(daily_df: pd.DataFrame, i: int) -> bool:
    return P79(daily_df, i)

def EL80(daily_df: pd.DataFrame, i: int) -> bool:
    return P80(daily_df, i)

def EL81(daily_df: pd.DataFrame, i: int) -> bool:
    return P81(daily_df, i)

def EL82(daily_df: pd.DataFrame, i: int) -> bool:
    return P82(daily_df, i)

def EL83(daily_df: pd.DataFrame, i: int) -> bool:
    return P83(daily_df, i)

def EL84(daily_df: pd.DataFrame, i: int) -> bool:
    return P84(daily_df, i)

def EL85(daily_df: pd.DataFrame, i: int) -> bool:
    return P85(daily_df, i)

def EL86(daily_df: pd.DataFrame, i: int) -> bool:
    return P86(daily_df, i)

def EL87(daily_df: pd.DataFrame, i: int) -> bool:
    return P87(daily_df, i)

def EL88(daily_df: pd.DataFrame, i: int) -> bool:
    return P88(daily_df, i)

def EL89(daily_df: pd.DataFrame, i: int) -> bool:
    return P89(daily_df, i)

def EL90(daily_df: pd.DataFrame, i: int) -> bool:
    return P90(daily_df, i)

def EL91(daily_df: pd.DataFrame, i: int) -> bool:
    return P91(daily_df, i)

def EL92(daily_df: pd.DataFrame, i: int) -> bool:
    return P92(daily_df, i)

def EL93(daily_df: pd.DataFrame, i: int) -> bool:
    return P93(daily_df, i)

def EL94(daily_df: pd.DataFrame, i: int) -> bool:
    return P94(daily_df, i)

def EL95(daily_df: pd.DataFrame, i: int) -> bool:
    return P95(daily_df, i)


# === PatternEsclusioneShort ===
def ES1(daily_df: pd.DataFrame, i: int) -> bool:
    return PS1(daily_df, i)

def ES2(daily_df: pd.DataFrame, i: int) -> bool:
    return PS2(daily_df, i)

def ES3(daily_df: pd.DataFrame, i: int) -> bool:
    return PS3(daily_df, i)

def ES4(daily_df: pd.DataFrame, i: int) -> bool:
    return PS4(daily_df, i)

def ES5(daily_df: pd.DataFrame, i: int) -> bool:
    return PS5(daily_df, i)

def ES6(daily_df: pd.DataFrame, i: int) -> bool:
    return PS6(daily_df, i)

def ES7(daily_df: pd.DataFrame, i: int) -> bool:
    return PS7(daily_df, i)

def ES8(daily_df: pd.DataFrame, i: int) -> bool:
    return PS8(daily_df, i)

def ES9(daily_df: pd.DataFrame, i: int) -> bool:
    return PS9(daily_df, i)

def ES10(daily_df: pd.DataFrame, i: int) -> bool:
    return PS10(daily_df, i)

def ES11(daily_df: pd.DataFrame, i: int) -> bool:
    return PS11(daily_df, i)

def ES12(daily_df: pd.DataFrame, i: int) -> bool:
    return PS12(daily_df, i)

def ES13(daily_df: pd.DataFrame, i: int) -> bool:
    return PS13(daily_df, i)

def ES14(daily_df: pd.DataFrame, i: int) -> bool:
    return PS14(daily_df, i)

def ES15(daily_df: pd.DataFrame, i: int) -> bool:
    return PS15(daily_df, i)

def ES16(daily_df: pd.DataFrame, i: int) -> bool:
    return PS16(daily_df, i)

def ES17(daily_df: pd.DataFrame, i: int) -> bool:
    return PS17(daily_df, i)

def ES18(daily_df: pd.DataFrame, i: int) -> bool:
    return PS18(daily_df, i)

def ES19(daily_df: pd.DataFrame, i: int) -> bool:
    return PS19(daily_df, i)

def ES20(daily_df: pd.DataFrame, i: int) -> bool:
    return PS20(daily_df, i)

def ES21(daily_df: pd.DataFrame, i: int) -> bool:
    return PS21(daily_df, i)

def ES22(daily_df: pd.DataFrame, i: int) -> bool:
    return PS22(daily_df, i)

def ES23(daily_df: pd.DataFrame, i: int) -> bool:
    return PS23(daily_df, i)

def ES24(daily_df: pd.DataFrame, i: int) -> bool:
    return PS24(daily_df, i)

def ES25(daily_df: pd.DataFrame, i: int) -> bool:
    return PS25(daily_df, i)

def ES26(daily_df: pd.DataFrame, i: int) -> bool:
    return PS26(daily_df, i)

def ES27(daily_df: pd.DataFrame, i: int) -> bool:
    return PS27(daily_df, i)

def ES28(daily_df: pd.DataFrame, i: int) -> bool:
    return PS28(daily_df, i)

def ES29(daily_df: pd.DataFrame, i: int) -> bool:
    return PS29(daily_df, i)

def ES30(daily_df: pd.DataFrame, i: int) -> bool:
    return PS30(daily_df, i)

def ES31(daily_df: pd.DataFrame, i: int) -> bool:
    return PS31(daily_df, i)

def ES32(daily_df: pd.DataFrame, i: int) -> bool:
    return PS32(daily_df, i)

def ES33(daily_df: pd.DataFrame, i: int) -> bool:
    return PS33(daily_df, i)

def ES34(daily_df: pd.DataFrame, i: int) -> bool:
    return PS34(daily_df, i)

def ES35(daily_df: pd.DataFrame, i: int) -> bool:
    return PS35(daily_df, i)

def ES36(daily_df: pd.DataFrame, i: int) -> bool:
    return PS36(daily_df, i)

def ES37(daily_df: pd.DataFrame, i: int) -> bool:
    return PS37(daily_df, i)

def ES38(daily_df: pd.DataFrame, i: int) -> bool:
    return PS38(daily_df, i)

def ES39(daily_df: pd.DataFrame, i: int) -> bool:
    return PS39(daily_df, i)

def ES40(daily_df: pd.DataFrame, i: int) -> bool:
    return PS40(daily_df, i)

def ES41(daily_df: pd.DataFrame, i: int) -> bool:
    return PS41(daily_df, i)

def ES42(daily_df: pd.DataFrame, i: int) -> bool:
    return PS42(daily_df, i)

def ES43(daily_df: pd.DataFrame, i: int) -> bool:
    return PS43(daily_df, i)

def ES44(daily_df: pd.DataFrame, i: int) -> bool:
    return PS44(daily_df, i)

def ES45(daily_df: pd.DataFrame, i: int) -> bool:
    return PS45(daily_df, i)

def ES46(daily_df: pd.DataFrame, i: int) -> bool:
    return PS46(daily_df, i)

def ES47(daily_df: pd.DataFrame, i: int) -> bool:
    return PS47(daily_df, i)

def ES48(daily_df: pd.DataFrame, i: int) -> bool:
    return PS48(daily_df, i)

def ES49(daily_df: pd.DataFrame, i: int) -> bool:
    return PS49(daily_df, i)

def ES50(daily_df: pd.DataFrame, i: int) -> bool:
    return PS50(daily_df, i)

def ES51(daily_df: pd.DataFrame, i: int) -> bool:
    return PS51(daily_df, i)

def ES52(daily_df: pd.DataFrame, i: int) -> bool:
    return PS52(daily_df, i)

def ES53(daily_df: pd.DataFrame, i: int) -> bool:
    return PS53(daily_df, i)

def ES54(daily_df: pd.DataFrame, i: int) -> bool:
    return PS54(daily_df, i)

def ES55(daily_df: pd.DataFrame, i: int) -> bool:
    return PS55(daily_df, i)

def ES56(daily_df: pd.DataFrame, i: int) -> bool:
    return PS56(daily_df, i)

def ES57(daily_df: pd.DataFrame, i: int) -> bool:
    return PS57(daily_df, i)

def ES58(daily_df: pd.DataFrame, i: int) -> bool:
    return PS58(daily_df, i)

def ES59(daily_df: pd.DataFrame, i: int) -> bool:
    return PS59(daily_df, i)

def ES60(daily_df: pd.DataFrame, i: int) -> bool:
    return PS60(daily_df, i)

def ES61(daily_df: pd.DataFrame, i: int) -> bool:
    return PS61(daily_df, i)

def ES62(daily_df: pd.DataFrame, i: int) -> bool:
    return PS62(daily_df, i)

def ES63(daily_df: pd.DataFrame, i: int) -> bool:
    return PS63(daily_df, i)

def ES64(daily_df: pd.DataFrame, i: int) -> bool:
    return PS64(daily_df, i)

def ES65(daily_df: pd.DataFrame, i: int) -> bool:
    return PS65(daily_df, i)

def ES66(daily_df: pd.DataFrame, i: int) -> bool:
    return PS66(daily_df, i)

def ES67(daily_df: pd.DataFrame, i: int) -> bool:
    return PS67(daily_df, i)

def ES68(daily_df: pd.DataFrame, i: int) -> bool:
    return PS68(daily_df, i)

def ES69(daily_df: pd.DataFrame, i: int) -> bool:
    return PS69(daily_df, i)

def ES70(daily_df: pd.DataFrame, i: int) -> bool:
    return PS70(daily_df, i)

def ES71(daily_df: pd.DataFrame, i: int) -> bool:
    return PS71(daily_df, i)

def ES72(daily_df: pd.DataFrame, i: int) -> bool:
    return PS72(daily_df, i)

def ES73(daily_df: pd.DataFrame, i: int) -> bool:
    return PS73(daily_df, i)

def ES74(daily_df: pd.DataFrame, i: int) -> bool:
    return PS74(daily_df, i)

def ES75(daily_df: pd.DataFrame, i: int) -> bool:
    return PS75(daily_df, i)

def ES76(daily_df: pd.DataFrame, i: int) -> bool:
    return PS76(daily_df, i)

def ES77(daily_df: pd.DataFrame, i: int) -> bool:
    return PS77(daily_df, i)

def ES78(daily_df: pd.DataFrame, i: int) -> bool:
    return PS78(daily_df, i)

def ES79(daily_df: pd.DataFrame, i: int) -> bool:
    return PS79(daily_df, i)

def ES80(daily_df: pd.DataFrame, i: int) -> bool:
    return PS80(daily_df, i)

def ES81(daily_df: pd.DataFrame, i: int) -> bool:
    return PS81(daily_df, i)

def ES82(daily_df: pd.DataFrame, i: int) -> bool:
    return PS82(daily_df, i)

def ES83(daily_df: pd.DataFrame, i: int) -> bool:
    return PS83(daily_df, i)

def ES84(daily_df: pd.DataFrame, i: int) -> bool:
    return PS84(daily_df, i)

def ES85(daily_df: pd.DataFrame, i: int) -> bool:
    return PS85(daily_df, i)

def ES86(daily_df: pd.DataFrame, i: int) -> bool:
    return PS86(daily_df, i)

def ES87(daily_df: pd.DataFrame, i: int) -> bool:
    return PS87(daily_df, i)

def ES88(daily_df: pd.DataFrame, i: int) -> bool:
    return PS88(daily_df, i)

def ES89(daily_df: pd.DataFrame, i: int) -> bool:
    return PS89(daily_df, i)

def ES90(daily_df: pd.DataFrame, i: int) -> bool:
    return PS90(daily_df, i)

def ES91(daily_df: pd.DataFrame, i: int) -> bool:
    return PS91(daily_df, i)

def ES92(daily_df: pd.DataFrame, i: int) -> bool:
    return PS92(daily_df, i)

def ES93(daily_df: pd.DataFrame, i: int) -> bool:
    return PS93(daily_df, i)

def ES94(daily_df: pd.DataFrame, i: int) -> bool:
    return PS94(daily_df, i)

def ES95(daily_df: pd.DataFrame, i: int) -> bool:
    return PS95(daily_df, i)


# === VolatilityLongPattern ===
def V1(intraday_df: pd.DataFrame, i: int) -> bool:
    return abs_value(intraday_df['Open'].iloc[i-1] - intraday_df['Close'].iloc[i-1]) < \
           0.1 * (intraday_df['High'].iloc[i-1] - intraday_df['Low'].iloc[i-1])

def V2(intraday_df: pd.DataFrame, i: int) -> bool:
    return abs_value(intraday_df['Open'].iloc[i-5] - intraday_df['Close'].iloc[i-1]) > \
           2.5 * (intraday_df['High'].iloc[i-5] - intraday_df['Low'].iloc[i-1])

def V3(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > \
           0.75 * (intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1])

def V4(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > ((intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1]) * 1)

def V5(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > ((intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1]) * 1.5)

def V6(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > ((intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1]) * 2)

def V7(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > ((intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1]) * 2.5)

def V8(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > ((intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1]) * 3)

def V9(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) < (intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1])

def V10(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > intraday_df['Close'].iloc[i-2] > \
           intraday_df['Close'].iloc[i-3] > intraday_df['Close'].iloc[i-4]

def V11(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > intraday_df['Close'].iloc[i-2] > \
           intraday_df['Close'].iloc[i-3] > intraday_df['Close'].iloc[i-4] > \
           intraday_df['Close'].iloc[i-5]

def V12(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i-1] > intraday_df['High'].iloc[i-2] and \
           intraday_df['Low'].iloc[i-1] > intraday_df['Low'].iloc[i-2]

def V13(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > intraday_df['Close'].iloc[i-2]

def V14(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > intraday_df['Open'].iloc[i-1]

def V15(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > (intraday_df['Close'].iloc[i-2] + intraday_df['Close'].iloc[i-2] * 0.5 * 0.01)

def V16(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > (intraday_df['Close'].iloc[i-2] + intraday_df['Close'].iloc[i-2] * 1 * 0.01)

def V17(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > (intraday_df['Close'].iloc[i-2] + intraday_df['Close'].iloc[i-2] * 1.5 * 0.01)

def V18(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > (intraday_df['Close'].iloc[i-2] + intraday_df['Close'].iloc[i-2] * 2 * 0.01)

def V19(intraday_df: pd.DataFrame, i: int) -> bool:  # verifica a campione (CloseS(1) > (CloseS(2) + CloseS(2) * 2.5 * 0.01)) 
    return intraday_df['Close'].iloc[i-1] > (intraday_df['Close'].iloc[i-2] + intraday_df['Close'].iloc[i-2] * 2.5 * 0.01)

def V20(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > (intraday_df['Close'].iloc[i-2] + intraday_df['Close'].iloc[i-2] * 3 * 0.01)

def V21(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i] > intraday_df['High'].iloc[i-1]

def V22(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i] > (intraday_df['High'].iloc[i-1] + intraday_df['High'].iloc[i-1] * 0.25 * 0.01)

def V23(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i] > (intraday_df['High'].iloc[i-1] + intraday_df['High'].iloc[i-1] * 0.5 * 0.01)

def V24(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i] > (intraday_df['High'].iloc[i-1] + intraday_df['High'].iloc[i-1] * 0.75 * 0.01)

def V25(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i] > (intraday_df['High'].iloc[i-1] + intraday_df['High'].iloc[i-1] * 1 * 0.01)

def V26(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i] > (intraday_df['High'].iloc[i-1] + intraday_df['High'].iloc[i-1] * 1.5 * 0.01)

def V27(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Low'].iloc[i] > intraday_df['Low'].iloc[i-1]

def V28(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Low'].iloc[i] > (intraday_df['Low'].iloc[i-1] + intraday_df['Low'].iloc[i-1] * 0.5 * 0.01)



# === VolatilityShortPattern ===
def VS1(intraday_df: pd.DataFrame, i: int) -> bool:
    return abs_value(intraday_df['Open'].iloc[i-1] - intraday_df['Close'].iloc[i-1]) > \
           0.9 * (intraday_df['High'].iloc[i-1] - intraday_df['Low'].iloc[i-1])

def VS2(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > \
           0.5 * (intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1])

def VS3(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > \
           0.75 * (intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1])

def VS4(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > ((intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1]) * 1)

def VS5(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > ((intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1]) * 1.5)

def VS6(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > ((intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1]) * 2)

def VS7(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > ((intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1]) * 2.5)

def VS8(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) > ((intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1]) * 3)

def VS9(intraday_df: pd.DataFrame, i: int) -> bool:
    return (intraday_df['High'].iloc[i] - intraday_df['Open'].iloc[i]) < (intraday_df['High'].iloc[i-1] - intraday_df['Open'].iloc[i-1])

def VS10(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > intraday_df['Close'].iloc[i-2] > \
           intraday_df['Close'].iloc[i-3] > intraday_df['Close'].iloc[i-4]

def VS11(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > intraday_df['Close'].iloc[i-2] > \
           intraday_df['Close'].iloc[i-3] > intraday_df['Close'].iloc[i-4] > \
           intraday_df['Close'].iloc[i-5]

def VS12(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i-1] > intraday_df['High'].iloc[i-2] and \
           intraday_df['Low'].iloc[i-1] > intraday_df['Low'].iloc[i-2]

def VS13(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > intraday_df['Close'].iloc[i-2]

def VS14(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > intraday_df['Open'].iloc[i-1]

def VS15(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > (intraday_df['Close'].iloc[i-2] + intraday_df['Close'].iloc[i-2] * 0.5 * 0.01)

def VS16(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > (intraday_df['Close'].iloc[i-2] + intraday_df['Close'].iloc[i-2] * 1 * 0.01)

def VS17(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > (intraday_df['Close'].iloc[i-2] + intraday_df['Close'].iloc[i-2] * 1.5 * 0.01)

def VS18(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > (intraday_df['Close'].iloc[i-2] + intraday_df['Close'].iloc[i-2] * 2 * 0.01)

def VS19(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > (intraday_df['Close'].iloc[i-2] + intraday_df['Close'].iloc[i-2] * 2.5 * 0.01)

def VS20(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Close'].iloc[i-1] > (intraday_df['Close'].iloc[i-2] + intraday_df['Close'].iloc[i-2] * 3 * 0.01)

def VS21(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i] > intraday_df['High'].iloc[i-1]

def VS22(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i] > (intraday_df['High'].iloc[i-1] + intraday_df['High'].iloc[i-1] * 0.25 * 0.01)

def VS23(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i] > (intraday_df['High'].iloc[i-1] + intraday_df['High'].iloc[i-1] * 0.5 * 0.01)

def VS24(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i] > (intraday_df['High'].iloc[i-1] + intraday_df['High'].iloc[i-1] * 0.75 * 0.01)

def VS25(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i] > (intraday_df['High'].iloc[i-1] + intraday_df['High'].iloc[i-1] * 1 * 0.01)

def VS26(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['High'].iloc[i] > (intraday_df['High'].iloc[i-1] + intraday_df['High'].iloc[i-1] * 1.5 * 0.01)

def VS27(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Low'].iloc[i] > intraday_df['Low'].iloc[i-1]

def VS28(intraday_df: pd.DataFrame, i: int) -> bool:
    return intraday_df['Low'].iloc[i] > (intraday_df['Low'].iloc[i-1] + intraday_df['Low'].iloc[i-1] * 0.5 * 0.01)


PATTERNS_LONG = {"P1": P1, "P2": P2, "P3": P3, "P4": P4, "P5": P5, "P6": P6, "P7": P7, "P8": P8, "P9": P9, "P10": P10, "P11": P11, "P12": P12, "P13": P13, "P14": P14, "P15": P15, "P16": P16, "P17": P17, "P18": P18, "P19": P19, "P20": P20, "P21": P21, "P22": P22, "P23": P23, "P24": P24, "P25": P25, "P26": P26, "P27": P27, "P28": P28, "P29": P29, "P30": P30, "P31": P31, "P32": P32, "P33": P33, "P34": P34, "P35": P35, "P36": P36, "P37": P37, "P38": P38, "P39": P39, "P40": P40, "P41": P41, "P42": P42, "P43": P43, "P44": P44, "P45": P45, "P46": P46, "P47": P47, "P48": P48, "P49": P49, "P50": P50, "P51": P51, "P52": P52, "P53": P53, "P54": P54, "P55": P55, "P56": P56, "P57": P57, "P58": P58, "P59": P59, "P60": P60, "P61": P61, "P62": P62, "P63": P63, "P64": P64, "P65": P65, "P66": P66, "P67": P67, "P68": P68, "P69": P69, "P70": P70, "P71": P71, "P72": P72, "P73": P73, "P74": P74, "P75": P75, "P76": P76, "P77": P77, "P78": P78, "P79": P79, "P80": P80, "P81": P81, "P82": P82, "P83": P83, "P84": P84, "P85": P85, "P86": P86, "P87": P87, "P88": P88, "P89": P89, "P90": P90, "P91": P91, "P92": P92, "P93": P93, "P94": P94, "P95": P95}
PATTERNS_SHORT = {"PS1": PS1, "PS2": PS2, "PS3": PS3, "PS4": PS4, "PS5": PS5, "PS6": PS6, "PS7": PS7, "PS8": PS8, "PS9": PS9, "PS10": PS10, "PS11": PS11, "PS12": PS12, "PS13": PS13, "PS14": PS14, "PS15": PS15, "PS16": PS16, "PS17": PS17, "PS18": PS18, "PS19": PS19, "PS20": PS20, "PS21": PS21, "PS22": PS22, "PS23": PS23, "PS24": PS24, "PS25": PS25, "PS26": PS26, "PS27": PS27, "PS28": PS28, "PS29": PS29, "PS30": PS30, "PS31": PS31, "PS32": PS32, "PS33": PS33, "PS34": PS34, "PS35": PS35, "PS36": PS36, "PS37": PS37, "PS38": PS38, "PS39": PS39, "PS40": PS40, "PS41": PS41, "PS42": PS42, "PS43": PS43, "PS44": PS44, "PS45": PS45, "PS46": PS46, "PS47": PS47, "PS48": PS48, "PS49": PS49, "PS50": PS50, "PS51": PS51, "PS52": PS52, "PS53": PS53, "PS54": PS54, "PS55": PS55, "PS56": PS56, "PS57": PS57, "PS58": PS58, "PS59": PS59, "PS60": PS60, "PS61": PS61, "PS62": PS62, "PS63": PS63, "PS64": PS64, "PS65": PS65, "PS66": PS66, "PS67": PS67, "PS68": PS68, "PS69": PS69, "PS70": PS70, "PS71": PS71, "PS72": PS72, "PS73": PS73, "PS74": PS74, "PS75": PS75, "PS76": PS76, "PS77": PS77, "PS78": PS78, "PS79": PS79, "PS80": PS80, "PS81": PS81, "PS82": PS82, "PS83": PS83, "PS84": PS84, "PS85": PS85, "PS86": PS86, "PS87": PS87, "PS88": PS88, "PS89": PS89, "PS90": PS90, "PS91": PS91, "PS92": PS92, "PS93": PS93, "PS94": PS94, "PS95": PS95}
PATTERNS_EXCL_LONG = {"EL1": EL1, "EL2": EL2, "EL3": EL3, "EL4": EL4, "EL5": EL5, "EL6": EL6, "EL7": EL7, "EL8": EL8, "EL9": EL9, "EL10": EL10, "EL11": EL11, "EL12": EL12, "EL13": EL13, "EL14": EL14, "EL15": EL15, "EL16": EL16, "EL17": EL17, "EL18": EL18, "EL19": EL19, "EL20": EL20, "EL21": EL21, "EL22": EL22, "EL23": EL23, "EL24": EL24, "EL25": EL25, "EL26": EL26, "EL27": EL27, "EL28": EL28, "EL29": EL29, "EL30": EL30, "EL31": EL31, "EL32": EL32, "EL33": EL33, "EL34": EL34, "EL35": EL35, "EL36": EL36, "EL37": EL37, "EL38": EL38, "EL39": EL39, "EL40": EL40, "EL41": EL41, "EL42": EL42, "EL43": EL43, "EL44": EL44, "EL45": EL45, "EL46": EL46, "EL47": EL47, "EL48": EL48, "EL49": EL49, "EL50": EL50, "EL51": EL51, "EL52": EL52, "EL53": EL53, "EL54": EL54, "EL55": EL55, "EL56": EL56, "EL57": EL57, "EL58": EL58, "EL59": EL59, "EL60": EL60, "EL61": EL61, "EL62": EL62, "EL63": EL63, "EL64": EL64, "EL65": EL65, "EL66": EL66, "EL67": EL67, "EL68": EL68, "EL69": EL69, "EL70": EL70, "EL71": EL71, "EL72": EL72, "EL73": EL73, "EL74": EL74, "EL75": EL75, "EL76": EL76, "EL77": EL77, "EL78": EL78, "EL79": EL79, "EL80": EL80, "EL81": EL81, "EL82": EL82, "EL83": EL83, "EL84": EL84, "EL85": EL85, "EL86": EL86, "EL87": EL87, "EL88": EL88, "EL89": EL89, "EL90": EL90, "EL91": EL91, "EL92": EL92, "EL93": EL93, "EL94": EL94, "EL95": EL95}
PATTERNS_EXCL_SHORT = {"ES1": ES1, "ES2": ES2, "ES3": ES3, "ES4": ES4, "ES5": ES5, "ES6": ES6, "ES7": ES7, "ES8": ES8, "ES9": ES9, "ES10": ES10, "ES11": ES11, "ES12": ES12, "ES13": ES13, "ES14": ES14, "ES15": ES15, "ES16": ES16, "ES17": ES17, "ES18": ES18, "ES19": ES19, "ES20": ES20, "ES21": ES21, "ES22": ES22, "ES23": ES23, "ES24": ES24, "ES25": ES25, "ES26": ES26, "ES27": ES27, "ES28": ES28, "ES29": ES29, "ES30": ES30, "ES31": ES31, "ES32": ES32, "ES33": ES33, "ES34": ES34, "ES35": ES35, "ES36": ES36, "ES37": ES37, "ES38": ES38, "ES39": ES39, "ES40": ES40, "ES41": ES41, "ES42": ES42, "ES43": ES43, "ES44": ES44, "ES45": ES45, "ES46": ES46, "ES47": ES47, "ES48": ES48, "ES49": ES49, "ES50": ES50, "ES51": ES51, "ES52": ES52, "ES53": ES53, "ES54": ES54, "ES55": ES55, "ES56": ES56, "ES57": ES57, "ES58": ES58, "ES59": ES59, "ES60": ES60, "ES61": ES61, "ES62": ES62, "ES63": ES63, "ES64": ES64, "ES65": ES65, "ES66": ES66, "ES67": ES67, "ES68": ES68, "ES69": ES69, "ES70": ES70, "ES71": ES71, "ES72": ES72, "ES73": ES73, "ES74": ES74, "ES75": ES75, "ES76": ES76, "ES77": ES77, "ES78": ES78, "ES79": ES79, "ES80": ES80, "ES81": ES81, "ES82": ES82, "ES83": ES83, "ES84": ES84, "ES85": ES85, "ES86": ES86, "ES87": ES87, "ES88": ES88, "ES89": ES89, "ES90": ES90, "ES91": ES91, "ES92": ES92, "ES93": ES93, "ES94": ES94, "ES95": ES95}
PATTERNS_VOL_LONG = {"V1": V1, "V2": V2, "V3": V3, "V4": V4, "V5": V5, "V6": V6, "V7": V7, "V8": V8, "V9": V9, "V10": V10, "V11": V11, "V12": V12, "V13": V13, "V14": V14, "V15": V15, "V16": V16, "V17": V17, "V18": V18, "V19": V19, "V20": V20, "V21": V21, "V22": V22, "V23": V23, "V24": V24, "V25": V25, "V26": V26, "V27": V27, "V28": V28}
PATTERNS_VOL_SHORT = {"VS1": VS1, "VS2": VS2, "VS3": VS3, "VS4": VS4, "VS5": VS5, "VS6": VS6, "VS7": VS7, "VS8": VS8, "VS9": VS9, "VS10": VS10, "VS11": VS11, "VS12": VS12, "VS13": VS13, "VS14": VS14, "VS15": VS15, "VS16": VS16, "VS17": VS17, "VS18": VS18, "VS19": VS19, "VS20": VS20, "VS21": VS21, "VS22": VS22, "VS23": VS23, "VS24": VS24, "VS25": VS25, "VS26": VS26, "VS27": VS27, "VS28": VS28}
