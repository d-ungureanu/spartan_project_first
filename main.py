#!C:\Users\mic\AppData\Local\Programs\Python\Python310\python.exe
from flask import Flask, request
import management
from spartan import Spartan

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return f"HOMEPAGE"


@app.route("/spartan/add", methods=["POST"])
def spartan_add():
    spartan_data = request.json

    if len(spartan_data["first_name"]) > 1:
        s_fn = spartan_data["first_name"]
    else:
        return "ERROR: first name should have at least 2 characters."

    if len(spartan_data["last_name"]) > 1:
        s_ln = spartan_data["last_name"]
    else:
        return "ERROR: last name should have at least 2 characters."

    if int(spartan_data["birth_day"]) in range(1, 32):
        s_bd = spartan_data["birth_day"]
    else:
        return "ERROR: Day of birth should be a number between 1 and 31."

    if int(spartan_data["birth_month"]) in range(1, 13):
        s_bm = spartan_data["birth_month"]
    else:
        return "ERROR: Month of birth should be a number between 1 and 12."

    if int(spartan_data["birth_year"]) in range(1900, 2005):
        s_by = spartan_data["birth_year"]
    else:
        return "ERROR: Year of birth should be a number between 1900 and 2004."

    if len(spartan_data["course"]) > 2:
        s_co = spartan_data["course"]
    else:
        return "ERROR: Course name should have at least 3 characters."

    if len(spartan_data["stream"]) > 2:
        s_st = spartan_data["stream"]
    else:
        return "ERROR: Stream's name should have at least 3 characters."

    if management.check_id_in_db(spartan_data["ids"]):
        return "ID already in database."
    else:
        s_id = spartan_data["ids"]
    temp_spartan = Spartan(s_id, s_fn, s_ln, s_bd, s_bm, s_by, s_co, s_st)
    management.add_to_db(temp_spartan)
    management.save_db_as_json()
    return "Entry saved."


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
