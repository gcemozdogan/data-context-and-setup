from pathlib import Path
import pandas as pd


class Olist:
    """
    The Olist class provides methods to interact with Olist's e-commerce data.

    Methods:
        get_data():
            Loads and returns a dictionary where keys are dataset names (e.g., 'sellers', 'orders')
            and values are pandas DataFrames loaded from corresponding CSV files.

        ping():
            Prints "pong" to confirm the method is callable.
    """
    def get_data(self):
        """
        Reads all CSV files from ~/.workintech/olist/data/csv
        and returns them as a dictionary of DataFrames.
        """
        # Define the path to the csv folder
        csv_path = os.path.expanduser("~/.workintech/olist/data/csv")

        # List all files in the directory ending with .csv
        file_names = [f for f in os.listdir(csv_path) if f.endswith('.csv')]

        # Create descriptive keys by removing 'olist_' prefix and '_dataset.csv' suffix
        key_names = [f.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '')
                     for f in file_names]

        # Load each CSV into a DataFrame and store in a dictionary
        data = {}
        for key, file in zip(key_names, file_names):
            full_path = os.path.join(csv_path, file)
            data[key] = pd.read_csv(full_path)

        return data

    def ping(self):
        """
        Standard connectivity test.
        """
        print("pong")
