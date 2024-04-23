Name: Haarit Chavda
Roll no: 23110077

# DCC _ Flask Assignment

## How to setup the local Website and Documentation
 
1) Extract data from the pdfs and store it in form of csv. To do so add the pdf file into the folder and run 'data_extraction.py'. This will create two csv files containing all the data.
2) Now run the python script named 'loaddatasql.py'. This will load the data from csv file to your sql server. Dont forget to change the database name and user credentials for the connection string of sql.
3) Now run app.py with relevant credentials and the website is functional !!


- First create a app object from flask library
- Create a connection to my sql database using MySQL from flask_Mysqldb. For that provide rlevent credentials and database name.
- Create the required routes for the websites using app.route 
- Write the logic for all the queries inside these routes.  TO do so we will require a cursor object for passing the sql queries to the sql server. Write the required queries and pass it to the cursor.
- Pass the data after processing it if required to the html files using render template function from flask
- In html files process this data using jinja templates.
- Also add a form to these html files to give the searching queris to the app. Process these queries in the app.py, pass it to the sql and get relevant data. 
- Again