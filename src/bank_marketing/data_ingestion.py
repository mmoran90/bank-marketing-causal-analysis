# import packages
from pathlib import Path
import zipfile
import pandas as pd

# function to extract and load data
def extract_and_load(data_dir: Path) -> pd.DataFrame:
    raw_dir = data_dir / "raw"
    zip_path = raw_dir / "bank-additional.zip"
    csv_path = raw_dir / "bank-additional" / "bank-additional-full.csv"

    if not csv_path.exists():
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(raw_dir)

    return pd.read_csv(csv_path, sep=";")