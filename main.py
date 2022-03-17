#!C:\Users\mic\AppData\Local\Programs\Python\Python310\python.exe
from flask import Flask, request
import management

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return f"HOMEPAGE"


@app.route("/spartan/add", methods=["POST"])
def spartan_add():
    spartan_data = request.json
    s_fn = spartan_data["first_name"]
    s_ln = spartan_data["last_name"]
    s_bd = spartan_data["birth_day"]
    s_bm = spartan_data["birth_month"]
    s_by = spartan_data["birth_year"]
    s_co = spartan_data["course"]
    s_st = spartan_data["stream"]
    s_id = spartan_data["ids"]
    return f"ID: {s_id}\nfirst name: {s_fn}\nlast name: {s_ln}\nDOB: {s_bd}/{s_bm}/{s_by}\ncourse: {s_co}\nstream: {s_st}"


@app.route("/spartan/<spartan_id>", methods=["GET"])
def spartan_getter(spartan_id):
    data = management.spartan_info(spartan_id)
    return data


@app.route("/spartan/remove", methods=["POST"])
def remove_spartan():
    id_var = request.args.get("id")
    return f"Remove spartan with ID: {id_var}."


@app.route("/spartan", methods=["GET"])
def list_spartans():
    spartans_db = management.display_db()
    return spartans_db


if __name__ == '__main__':
    app.run(debug=True)
