import fitz
import csv
import pandas as pd

filename = 'purchase_details'

document = fitz.open(f"{filename}.pdf") 
all_dfs = [] 


# redemption
columns=['Sr No.','Reference No (URN)','Journal Date','Date of Purchase','Date of Expiry','Name of Purchaser','Prefix','Bond Number','Denominations','Issue Branch Code','Issue Teller','Status']



# redemption
# columns=['Sr No.','Date of Encashment','Name of Political Party','Account No. of Political Party','Prefix','Bond Number','Denomination','Pay Branch Code','Pay Teller']

for i in range(len(document)):
    page = document[i]  
    tables = page.find_tables()  
    # print(tables)

    if tables:  
        table_data = tables[0].extract()  
        df = pd.DataFrame(table_data[1:], columns=columns)  
        # print(table_data)
        # print(df)
        all_dfs.append(df)  


concated = pd.concat(all_dfs, ignore_index=True)

concated.to_csv(f"{filename}.csv", index=False)

with open(f"{filename}.csv", "a", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    for row in table_data:
        csv_writer.writerow(row)