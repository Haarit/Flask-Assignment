Name: Haarit Chavda
Roll no: 23110077

# DCC _ Flask Assignment

## How to setup the local Website
 

### How to use the python scripts 
1) Extract data from the pdfs and store it in form of csv. To do so add the pdf file into the folder and run 'data_extraction.py'. This will create two csv files containing all the data.
2) Now run the python script named 'loaddatasql.py'. This will load the data from csv file to your sql server. Dont forget to change the database name and user credentials for the connection string of sql.
3) Now run app.py with relevant credentials and the website is functional !!


### Brief on how to setup the website from scratch
1. Begin by initializing an application object using the Flask library.
2. Establish a connection to a MySQL database using Flask-MySQLdb, providing the necessary credentials and database name.
3. Define routes for the website using the 'app.route' decorator.
4. Implement the logic for handling queries inside these routes. This involves creating a cursor object to execute SQL queries against the database.
5. Use the 'render_template' function from Flask to pass processed data, if needed, to HTML files.
6. Utilize Jinja templates within the HTML files to process and display the data.
7. Include forms in these HTML files to allow users to submit search queries to the application. Process these queries in the 'app.py' file, execute them against the database, and retrieve relevant data.
8. Once again, pass this data to the appropriate template using the 'render_template' function.
9. Organize static files, such as CSS for styling, in a folder named "static". Within this folder, create subfolders for CSS and scripts. Place CSS files in the CSS subfolder. Link these files to the corresponding HTML files using Jinja templating to ensure proper paths are used.
10. Finally, execute the 'app.py' file to launch the website.




## Documentation

### Introduction
- This website provides searching facility on the electoral database given by State Bank of India. 
### Technologies Used
- SQL, Flask, Jinja, Javascript, HTML5 and CSS are used to make this website.
### Library Requirements
- flask, flask_mysqldb, fitz, csv, pandas and sqlalchemy.



# Images of Website
## Homepage
Website Images/Home_Page.png
