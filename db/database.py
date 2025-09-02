from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///telecom.db")

def save_to_db(df, table_name="billing_data"):
    df.to_sql(table_name, con=engine, if_exists="append", index=False)

def load_data(table_name="billing_data"):
    return pd.read_sql(f"SELECT * FROM {table_name}", con=engine)
