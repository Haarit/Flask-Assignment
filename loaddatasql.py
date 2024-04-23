import pandas as pd
from sqlalchemy import create_engine

username = 'root'
password = 'hrc1905'
host = 'localhost' 
port = 3306 
database = 'flask'


connection_string = f'mysql+mysqldb://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(connection_string, echo=False)



df = pd.read_csv("purchase_details.csv")
table_name = 'purchase_details'
df.to_sql(name=table_name, con=engine, index=False, if_exists='replace')
print("Dataframe is written to MySQL database successfully.")



df = pd.read_csv("redemption_details.csv")
table_name = 'redemption_details'
df.to_sql(name=table_name, con=engine, index=False, if_exists='replace')
print("Dataframe is written to MySQL database successfully.")
