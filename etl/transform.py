# etl/transform.py
import re

def transform_data(data):
    try:
        # Convert column names to uppercase
        data.columns = map(str.upper, data.columns)

        # Remove dollar sign from specified columns
        columns_to_clean = ['MRP', 'CP', 'DISCOUNT', 'SP']
        for col in columns_to_clean:
            data[col] = data[col].str.replace('$', '', regex=False).astype(float)

        # Remove special symbols from specified columns
        columns_to_remove_special_symbols = ['STORE_LOCATION', 'PRODUCT_ID']
        for col in columns_to_remove_special_symbols:
            data[col] = data[col].apply(lambda x: re.sub(r'[^\w\s]', '', x))

        return data
    except Exception as e:
        raise Exception(f"Error while transforming data: {str(e)}")
