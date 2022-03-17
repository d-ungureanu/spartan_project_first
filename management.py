import json
from spartan import Spartan

all_spartans_db = {}
spartans_counter = 0


def spartan_info(spartan_id_to_display):
    global all_spartans_db
    load_db_from_file()
    temp_spartans_db = {}
    for sparta_id in all_spartans_db:
        spartan_object = all_spartans_db[sparta_id]
        spartans_dict = vars(spartan_object)
        temp_spartans_db[sparta_id] = spartans_dict
        int_id = int(spartan_id_to_display)
    if int_id in temp_spartans_db:
        return temp_spartans_db[int_id]
    else:
        return f"ID: {int_id} was not found in the database."


def add_to_db(spartan):
    global all_spartans_db
    all_spartans_db[spartan.get_sparta_id()] = spartan
    return "entry saved"


def check_id_in_db(id_to_check):
    global all_spartans_db
    load_db_from_file()
    return id_to_check in all_spartans_db.keys()


def display_db():
    global all_spartans_db
    global spartans_counter
    temp_db = {}
    try:
        with open("data.json", "r") as db_file:
            temp_db = json.load(db_file)
    except FileNotFoundError as file_not_found_error:
        print(file_not_found_error)
    return temp_db


def delete_from_db(id_to_delete):
    global all_spartans_db
    if id_to_delete in all_spartans_db.keys():
        del all_spartans_db[id_to_delete]
        return f"Deleted entry with ID: {all_spartans_db.keys()}"
    else:
        return f"ID: {id_to_delete} not in database."


def save_db_as_json():
    global all_spartans_db
    temp_all_spartans_db = {}

    # Convert spartan object to dictionary
    for spartan_id in all_spartans_db:
        spartan_object = all_spartans_db[spartan_id]
        spartan_dict = vars(spartan_object)
        temp_all_spartans_db[spartan_id] = spartan_dict
    with open("data.json", "w") as db_file:
        json.dump(temp_all_spartans_db, db_file)

    print("Saving data to data.json")


# Function used to load DB from JSON file
def load_db_from_file():
    global all_spartans_db
    global spartans_counter
    temp_db = {}
    try:
        with open("data.json", "r") as db_file:
            temp_db = json.load(db_file)
    except FileNotFoundError as file_not_found_error:
        print(file_not_found_error)

    # Convert dictionary data to Employee object
    for key_id in temp_db:
        spartan_id = temp_db[key_id]["sparta_id"]
        spartan_fn = temp_db[key_id]["first_name"]
        spartan_ln = temp_db[key_id]["last_name"]
        spartan_bd = temp_db[key_id]["birth_day"]
        spartan_bm = temp_db[key_id]["birth_month"]
        spartan_by = temp_db[key_id]["birth_year"]
        spartan_cou = temp_db[key_id]["course"]
        spartan_stm = temp_db[key_id]["stream"]

        temp_spartan = Spartan(spartan_id, spartan_fn, spartan_ln, spartan_bd, spartan_bm, spartan_by, spartan_cou,
                               spartan_stm)
        all_spartans_db[spartan_id] = temp_spartan

    # Counter set at database size, to avoid ID overlapping
    spartans_counter = len(all_spartans_db)
