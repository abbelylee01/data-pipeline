# main.py
import yaml
import logging
import sys
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

# Set up logging
logging.basicConfig(filename='etl.log', level=logging.INFO)

def main():
    try:
        # Load configuration from config.yaml
        with open('config/config.yaml', 'r') as config_file:
            config = yaml.safe_load(config_file)

        # Extract data
        data = extract_data(config['input_file_path'])
        logging.info("Data extraction successful....")

        # Transform data
        transformed_data = transform_data(data)
        logging.info("Data transformation successful.")

        # Load data
        load_data(transformed_data, config['db_connection'])
        logging.info("Data loading successful.")

    except Exception as e:
        logging.error(f"ETL process failed: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()

