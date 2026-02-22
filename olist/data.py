import os
import pandas as pd
from pathlib import Path

class Olist:
    def get_data(self):
        """
        Reads all Olist CSV files from the local directory and
        returns a dictionary of DataFrames with cleaned keys.
        """
        # Define the path to the CSV folder using pathlib
        csv_path = Path.home() / ".workintech" / "olist" / "data" / "csv"

        # Dictionary to store the DataFrames
        data = {}

        # Iterate through the directory and process each .csv file
        for file_path in csv_path.iterdir():
            if file_path.suffix == '.csv':
                # Clean the filename to create a consistent key name
                # Example: 'olist_orders_dataset.csv' -> 'orders'
                key = file_path.name.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '')

                # Load the CSV into a DataFrame
                data[key] = pd.read_csv(file_path)

        return data

    def ping(self):
        """
        Standard connectivity test.
        """
        print("pong")
