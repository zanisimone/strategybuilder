import pandas as pd
import os

def load_data(file_path: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Carica dati intraday da un file .txt con colonne Date, Time, Open, High, Low, Close, Volume
    Restituisce:
    - intraday_df: dati orari originali
    - daily_df: aggregazione OHLC per giorno
    """

    # === Step 1: Caricamento ===
    df = pd.read_csv(file_path, sep=",", engine="python")
    df.columns = df.columns.str.strip().str.replace("<", "").str.replace(">", "")

    # === Step 2: Parsing datetime ===
    df["time"] = pd.to_datetime(df["Date"] + " " + df["Time"], format="%d/%m/%Y %H:%M:%S")
    df = df.sort_values("time").reset_index(drop=True)

    # === Step 3: Intraday DF ===
    intraday_df = df[["time", "Open", "High", "Low", "Close", "Volume"]].copy()

    # === Step 4: Daily DF (aggregato per giorno) ===
    df["date"] = df["time"].dt.date

    daily_df = df.groupby("date").agg({
        "Open": "first",
        "High": "max",
        "Low": "min",
        "Close": "last"
    }).reset_index()

    daily_df["time"] = pd.to_datetime(daily_df["date"])
    daily_df = daily_df.drop(columns=["date"])
    daily_df = daily_df[["time", "Open", "High", "Low", "Close"]]

    return intraday_df, daily_df
