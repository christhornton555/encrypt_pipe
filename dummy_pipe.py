# A dummy pipeline to load and encrypt data

import pandas as pd

def read_data(filename='dummy_data.csv'):
    try:
        df = pd.read_csv(filename)
        print("Data loaded successfully:")
        print(df)
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

if __name__ == "__main__":
    read_data()
