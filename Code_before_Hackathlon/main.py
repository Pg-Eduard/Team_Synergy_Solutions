from flask import Flask, render_template, request, url_for, redirect, jsonify
import flask_apscheduler as APScheduler
import pandas as pd
from vreme import get_vreme
import scheduler_weather as sw
import json

scheduler = APScheduler.APScheduler()
app = Flask(__name__,static_url_path="/static")


@app.route("/")
def index():
    return render_template("pagina_logare.html")

@app.route("/ro")
def limba_romana():
    return render_template("cod_baza.html")

@app.route("/en")
def liba_engleza():
    return render_template("engleza.html")

@app.route("/sp")
def limba_spaniola():
    return render_template("spaniola.html")

@app.route("/api_vreme")
def api_vreme():
    date_vreme = get_vreme()
    json_data = json.dumps(date_vreme)
    return jsonify(data = json_data) #nou

@scheduler.task('interval', id='check_weather', seconds=10) #nou
def check_weather():
    sw.day_time()
    sw.vreme()


@app.route("/", methods=['GET',"POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get("pass")

    if username == username and password == password:
        print(f"Username: {username}, Password: {password}")
        return render_template("pagina_loga")
    else:
        return "Username și parola sunt necesare", 400
    

@app.route('/logare', methods=['POST'])
def logare():
    # Preluăm datele trimise de formular sub formă de JSON
    user_existent = False
    user_index = 0
    counter = 0
    counter_pass = 0
    data = request.get_json()
    username_web = data.get('username')
    password_web = data.get('password')
    print(username_web,password_web)

    try:
        test = pd.read_excel("static/user_database.xlsx")
        if test.empty:
            #print("Fisierul este gol, se creeaza un dataframe gol")
            database = pd.DataFrame()
        else:
            #print("Date detectate in fisier, se incarca datele")
            database = pd.read_excel("static/user_database.xlsx")
    except:
        #print("eroare in accesarea datelor, se creaza un dataframe gol")
        database = pd.DataFrame()

    database_users = database["user"].tolist()
    database_pass = database["pass"].tolist()

    for users in database_users:
        counter += 1
        print(counter)
        if users == username_web:
            print("user exists")
            user_index = database_users.index(users)
            break
        elif counter >= len(database_users):
            return jsonify(success=False, message="Username-ul este greșit", field="username")
    print(database_pass[user_index])
    
    if password_web != str(database_pass[user_index]):
        print(type(password_web),type(database_pass[user_index]))
        return jsonify(success=False,message="Parola este gresita", field = "pass")

    return jsonify(success=True)

@app.route("/save_users",methods=["POST"])
def createExcel():
    try:
        test_date = pd.read_excel("static/user_database.xlsx")
        if test_date.empty:
            print("Fisierul este gol, se creeaza un dataframe gol")
            login_info = pd.DataFrame()
        else:
            print("Date detectate in fisier, se incarca datele")
            login_info = pd.read_excel("static/user_database.xlsx")
    except:
        print("eroare in accesarea datelor, se creaza un dataframe gol")
        login_info = pd.DataFrame()

    try:
        data = request.get_json()
        username = data.get('username_sign')
        password = data.get("password_sign")

        db_users = login_info['user'].tolist()
        for users in db_users:
            if username == users:
                print("user existent detectat")
                return jsonify(success=False, message="Utilizatorul exista deja",field = "username_sign")

        date_de_adaugat = {
            "user": [username],
            "pass": [password]
        }
        date_noi = pd.DataFrame(date_de_adaugat)

        date_combinate = pd.concat([login_info,date_noi],ignore_index=True)

        date_combinate.to_excel("static/user_database.xlsx",index=False)

        return jsonify(success=True)
    
    except:
        data = request.get_json()
        username = data.get("username_sign")
        password = data.get("password_sign")
        date_de_adaugat = {
            "user": [username],
            "pass": [password]
        }
        date_noi = pd.DataFrame(date_de_adaugat)
        date_noi.to_excel("static/user_database.xlsx",index=False)
        return jsonify(success=True)
    
@app.route("/check_avalability")
def check_avalability():
    max_users = 4
    try:
        check = pd.read_excel("static/user_database.xlsx")
        if check.empty:
            check = pd.DataFrame()
        else:
            print("date detectate")
            check = pd.read_excel("static/user_database.xlsx")
    except:
        print("eroare in accesarea datelor")
        check = pd.DataFrame()

    try:
        no_users = len(check["user"].tolist())

        if no_users >= max_users:
            return jsonify(over_limit=True)
        else:
            return jsonify(over_limit=False)
    except:
        return jsonify(over_limit=False)

if __name__ == "__main__":
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug = True,host = "0.0.0.0")