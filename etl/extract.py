# etl/extract.py
import pandas as pd

def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        raise Exception(f"Error while extracting data: {str(e)}")


