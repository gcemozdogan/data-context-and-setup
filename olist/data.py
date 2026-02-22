import os
import pandas as pd

class Olist:
    def get_data(self):
        """
        Reads all Olist CSV files from ~/.workintech/olist/data/csv
        and returns a dictionary of DataFrames.
        """
        # Path where CSVs are stored
        csv_path = os.path.expanduser("~/.workintech/olist/data/csv")

        # Load files
        file_names = [f for f in os.listdir(csv_path) if f.endswith('.csv')]
        key_names = [f.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '')
                     for f in file_names]

        data = {}
        for key, file in zip(key_names, file_names):
            data[key] = pd.read_csv(os.path.join(csv_path, file))

        return data

    def ping(self):
        """
        Connectivity test.
        """
        print("pong")
