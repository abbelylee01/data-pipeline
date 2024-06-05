# etl/load.py
import psycopg2
import logging

# Set up logging
logging.basicConfig(
    filename='etl.log',  # Specify the log file
    level=logging.INFO,  # Set the logging level to INFO or any other level you prefer
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log message format
)


def load_data(data, db_connection):
    try:
         # Log that the connection is established
        conn = psycopg2.connect(db_connection)
        logging.info("Database connection established")
        cursor = conn.cursor()
        
        
        
        # Example: Create a PostgreSQL table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS production.clean_store_transactions (
                STORE_ID TEXT,
                STORE_LOCATION TEXT,
                PRODUCT_CATEGORY TEXT,
                PRODUCT_ID TEXT,
                MRP FLOAT,
                CP FLOAT, 
                DISCOUNT FLOAT,
                SP FLOAT, 
                DATE date    
               
            )
        ''')

        # Load data into the table
        for index, row in data.iterrows():
            cursor.execute('''
                INSERT INTO production.clean_store_transactions (STORE_ID, STORE_LOCATION, PRODUCT_CATEGORY, PRODUCT_ID, MRP, CP, DISCOUNT, SP, DATE)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (row['STORE_ID'], row['STORE_LOCATION'], row['PRODUCT_CATEGORY'], row['PRODUCT_ID'], row['MRP'], row['CP'], row['DISCOUNT'], row['SP'], row['DATE']))
        
        conn.commit()
        cursor.close()
        conn.close()
        # Log that the connection is closed
        logging.info("Database connection closed")
    except Exception as e:
        raise Exception(f"Error while loading data: {str(e)}")






