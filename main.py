#!C:\Users\mic\AppData\Local\Programs\Python\Python310\python.exe
from flask import Flask, request
import management
from spartan import Spartan

app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    homepage_content = """HOMEPAGE
    
    
1-  method: GET, route: / This is the landing page (Home page). 
    It should return a welcome message along with a simple tutorial clarifying how APIs can be used

2-  method: POST, route: /spartan/add 
    This API should allow the user to add new spartan to the system by passing a JSON object.

3-  method: GET, route: /spartan/<spartan_id> 
    Get certain employee using the spartan_id. 
    An error message should be returned if the spartan_id doesn't exist in the system. 
    The data should be returned as string

4-  method: POST, route: /spartan/remove?id=sparta_id 
    This API should allow the user to remove a spartan from the system by passing the sparta_id in the query_string

5- method: GET, route: /spartan 
This API should return the spartan list as one JSON object."""
    return homepage_content


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

    if management.check_id_in_db(spartan_data["sparta_id"]):
        return "ID already in database."
    else:
        s_id = spartan_data["sparta_id"]
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
    id_var = int(request.args.get("id"))
    management.load_db_from_file()
    management.delete_from_db(id_var)

    management.save_db_as_json()

    return f"Entry with ID: {id_var} deleted from database."


@app.route("/spartan", methods=["GET"])
def list_spartans():
    spartans_db = management.display_db()
    return spartans_db


if __name__ == '__main__':
    app.run(debug=True)
