from flask import Flask, redirect, url_for, request, Response, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hrc1905'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/', methods = ["POST", "GET"])
def main_page():
    return render_template("index.html")

@app.route('/purchase_details', methods = ["POST", "GET"])
def purchase_page():
    return render_template("purchase.html")

@app.route('/redemption_details', methods = ["POST", "GET"])
def redemption_page():
    return render_template("redemption.html")

@app.route('/purchase_query', methods = ["POST", "GET"])
def purchase_query_page():

    # print(request.form["options"])

    cursor = mysql.connection.cursor()
    column_name = request.form["options"]  # Make sure this is safe to use directly in SQL!
    value = request.form["box"]
    query = f"select * from purchase_details where `{column_name}` = %s"  # Use format to insert the column name
    cursor.execute(query, (value,))

    data = cursor.fetchall()
    print(data)

    cursor.close()

    return render_template("purchase.html", a_1_data = data) 


@app.route('/redemption_query', methods = ["POST", "GET"])
def redemption_query_page():
    print(request.form["options"])

    cursor = mysql.connection.cursor()
    column_name = request.form["options"]  # Make sure this is safe to use directly in SQL!
    value = request.form["box"]
    query = f"select * from redemption_details where `{column_name}` = %s"  # Use format to insert the column name
    cursor.execute(query, (value,))
    data = cursor.fetchall()
    print(data)

    cursor.close()

    return render_template("redemption.html", a_1_data = data) 

@app.route("/Q2_2", methods=["POST", "GET"])
def Q2_2():
    try:
        cursor = mysql.connection.cursor()
        query = "select  distinct `Name of Purchaser` from purchase_details order by `Name of Purchaser` asc"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Database error", 500

    if request.method=="POST":
        cursor = mysql.connection.cursor()
        value = request.form["names"]
        query = "select `Date of Purchase`,`Name of Purchaser`,`Bond Number`,`Denominations` from purchase_details where `Name of Purchaser` = %s"
        cursor.execute(query,(value,))
        data2=cursor.fetchall()
        cursor.close()


        # print("Total No. of bonds", len(data2))
        # print(data2)
        logs = dict()
        total = dict()
        for i in data2:
            money = int(i[3].replace(",",""))
            # print(money)
            year = i[0][-4:]
            if year not in logs.keys():
                logs[year]=1
                total[year]=money
            else:
                logs[year]+=1
                total[year]+=money

            number = list(logs.values())
            years = list(logs.keys())
            amount = list(total.values())


        return render_template("Q2_2.html", data=data,data2=data2,year=years,amount=amount,number=number)
    

    return render_template("Q2_2.html", data=data)


@app.route("/Q2_3", methods=["POST", "GET"])
def Q2_3():
    try:
        cursor = mysql.connection.cursor()
        query = "select  distinct `Name of Political Party` from redemption_details order by `Name of Political Party` asc"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Database error", 500

    if request.method=="POST":
        cursor = mysql.connection.cursor()
        value = request.form["names"]
        query = "select * from redemption_details where `Name of Political Party` = %s"
        cursor.execute(query,(value,))
        data2=cursor.fetchall()
        cursor.close()


        # print("Total No. of bonds", len(data2))
        # print(data2)
        logs = dict()
        total = dict()
        for i in data2:
            money = int(i[6].replace(",",""))
            # print(money)
            year = i[1][-4:]
            if year not in logs.keys():
                logs[year]=1
                total[year]=money
            else:
                logs[year]+=1
                total[year]+=money

            number = list(logs.values())
            years = list(logs.keys())
            amount = list(total.values())
            # print(logs)
    


        return render_template("Q2_3.html", data=data,year=years,amount=amount,number=number)
    

    return render_template("Q2_3.html", data=data)



@app.route("/Q2_4", methods=["POST", "GET"])
def Q2_4():
    try:
        cursor = mysql.connection.cursor()
        query = "select  distinct `Name of Political Party` from redemption_details order by `Name of Political Party` asc"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Database error", 500
    

    if request.method=="POST":

        cursor = mysql.connection.cursor()
        value = request.form["names"]
        query = "select `Name of Purchaser`,`Denominations` from purchase_details where `Bond Number` in (select `Bond Number` from redemption_details where `Name of Political Party`= %s)"
        cursor.execute(query,(value,))
        data1 = cursor.fetchall()
        cursor.close()
        print(data1)

        data_dict=dict()

        for i in data1:
            if i[0] not in data_dict.keys():
                data_dict[i[0]]=int(i[1].replace(",",""))
            else:
                data_dict[i[0]]+=int(i[1].replace(",",""))

        total = sum(data_dict.values())
        labels = list(data_dict.keys())
        data_pie = list(data_dict.values())
        return render_template("Q2_4.html",data=data,data_dict=data_dict,total=total,labels=labels,data_pie=data_pie)
    
    return render_template("Q2_4.html", data=data)



@app.route("/Q2_5", methods=["POST", "GET"])
def Q2_5():
    try:
        cursor = mysql.connection.cursor()
        query = "select  distinct `Name of Purchaser` from purchase_details order by `Name of Purchaser` asc"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Database error", 500
    

    if request.method=="POST":

        cursor = mysql.connection.cursor()
        value = request.form["names"]
        query = "select `Name of Political Party`,`Denomination` from redemption_details where `Bond Number` in (select `Bond Number` from purchase_details where `Name of Purchaser`= %s)"
        cursor.execute(query,(value,))
        data1 = cursor.fetchall()
        cursor.close()
        # print(data1)

        data_dict=dict()

        for i in data1:
            # print(i[1])
            if i[0] not in data_dict.keys():
                data_dict[i[0]]=int(i[1].replace(",",""))
            else:
                data_dict[i[0]]+=int(i[1].replace(",",""))

        total = sum(data_dict.values())
        labels = list(data_dict.keys())
        data_pie = list(data_dict.values())
        return render_template("Q2_5.html",data=data,data_dict=data_dict,total=total,labels=labels,data_pie=data_pie)
    
    return render_template("Q2_5.html", data=data)


@app.route("/Q2_6",methods=["POST","GET"])
def Q2_6():
    cursor = mysql.connection.cursor()
    query = "select `Name of Political Party`,`Denomination` from redemption_details"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    # print(data)
    data_dict = dict()
    for i in data:
        try:
            if i[0] not in data_dict.keys():
                data_dict[i[0]]=int(i[1].replace(",",""))
            else:
                data_dict[i[0]]+=int(i[1].replace(",",""))
        except Exception as e:
            print(e)

    labels = list(data_dict.keys())
    data_pie = list(data_dict.values())
    print(data_dict)

    return render_template("Q2_6.html",data=data,labels=labels,data_pie=data_pie)




@app.route("/exploring1",methods=["GET","POST"])
def exploring():
    
    try:
        cursor = mysql.connection.cursor()
        query = "select  distinct `Name of Political Party` from redemption_details order by `Name of Political Party` asc"
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Database error", 500
    

    if request.method=="POST":

        cursor = mysql.connection.cursor()
        value = request.form["names"]
        query = "select `Date of Encashment`,`Name of Political Party`,`Denomination` from redemption_details where `Name of Political Party` = %s "
        cursor.execute(query,(value,))
        data1 = cursor.fetchall()
        cursor.close()
        print(data1)


        data_dict = dict()
        for i in data1:
            try:
                if i[0] not in data_dict.keys():
                    data_dict[i[0]]=int(i[2].replace(",",""))
                else:
                    data_dict[i[0]]+=int(i[2].replace(",",""))
            except Exception as e:
                print(e)

        labels = list(data_dict.keys())
        data_graph = list(data_dict.values())

        return render_template("exploring1.html",data=data,labels=labels,data_graph=data_graph)

    return render_template("exploring1.html",data=data)


if __name__ == '__main__':
   app.run(host="0.0.0.0", port="80", debug = True) 