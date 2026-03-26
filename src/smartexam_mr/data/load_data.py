import pandas as pd


def load_raw_data(filepath: str) -> pd.DataFrame:
    """Loads raw dataset from csv."""
    return pd.read_csv(filepath)


def save_processed_data(df: pd.DataFrame, filepath: str) -> None:
    """Saves processed dataframe to csv."""
    df.to_csv(filepath, index=False)
