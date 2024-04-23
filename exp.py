import pandas as pd
from sqlalchemy import create_engine 

def csv_to_mysql(csv_path, table_name, connection_str):

    # Read the CSV file using pandas
    data = pd.read_csv(csv_path)

    # Create a SQLAlchemy engine
    engine = create_engine(connection_str)

    # Write the data to MySQL table
    data.to_sql(table_name, con=engine, if_exists='replace', index=False)

    print(f"CSV data successfully loaded into MySQL table '{table_name}'")

# MySQL connection configuration
username = 'root'
password = 'hrc1905'
host = 'localhost'
database_name = 'college'

# Connection string for MySQL
connection_str = f'mysql://{username}:{password}@{host}/{database_name}'

# Path to the first CSV file and table name
csv_path1 = 'redemption_details.csv'
table_name1 = 'redemption'

# Path to the second CSV file and table name
csv_path2 = 'purchase_details.csv'
table_name2 = 'purchase'

# Load data from the first CSV file into the first table
csv_to_mysql(csv_path1, table_name1, connection_str)

# Load data from the second CSV file into the second table
csv_to_mysql(csv_path2, table_name2, connection_str)