
import pandas as pd
from pathlib import Path

def load_bug_data(data_folder="data"):
    data_path = Path(data_folder)

    csv_files = list(data_path.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError("No CSV files found in data folder.")

    all_data = []

    for file in csv_files:
        try:
            df = pd.read_csv(file)

            df.columns = [c.strip() for c in df.columns]

            if "Reported Date" in df.columns:
                df["Reported Date"] = pd.to_datetime(
                    df["Reported Date"],
                    errors="coerce"
                )

            df["Source File"] = file.name

            all_data.append(df)

        except Exception as e:
            print(f"Error loading {file.name}: {e}")

    final_df = pd.concat(all_data, ignore_index=True)

    return final_df
