import pandas as pd
from sqlalchemy import create_engine
import glob, os

# ========== CONFIG ==========
DB_USER = "postgres"
DB_PASS = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "NEA"

DATA_PATH = "data/raw/*.csv"
TABLE_NAME = "electricity_consumption"



def extract_data():
    all_files = glob.glob(DATA_PATH)
    df_list = [pd.read_csv(file) for file in all_files]
    df = pd.concat(df_list, ignore_index=True)
    print(f" Extracted {len(all_files)} files, total {len(df)} records.")
    return df


def transform_data(df):
    df.columns = df.columns.str.lower().str.strip()
    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values(["province", "date"])
    df["consumption_change_%"] = df.groupby("province")["consumption_mwh"].pct_change() * 100

    df["consumption_mwh"].fillna(df["consumption_mwh"].mean(), inplace=True)
    df["peak_load_mw"].fillna(df["peak_load_mw"].mean(), inplace=True)
    df["outages"].fillna(0, inplace=True)

    print("Transformed data with new features.")
    return df


def load_data(df):
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into '{TABLE_NAME}' table in '{DB_NAME}' database.")


def main():
    df = extract_data()
    df = transform_data(df)
    load_data(df)
    print("ETL pipeline completed successfully!")


if __name__ == "__main__":
    main()
