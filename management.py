from flask import Flask, request, jsonify
import json
from spartan import Spartan

all_spartans_db = {}
spartans_counter = 0




def display_db():
    global all_spartans_db
    global spartans_counter
    temp_db = {}
    try:
        with open("spartans_db.json", "r") as db_file:
            temp_db = json.load(db_file)
    except FileNotFoundError as file_not_found_error:
        print(file_not_found_error)
    return temp_db


# Function used to load DB from JSON file
def load_db_from_file():
    global all_spartans_db
    global spartans_counter
    temp_db = {}
    try:
        with open("spartans_db.json", "r") as db_file:
            temp_db = json.load(db_file)
    except FileNotFoundError as file_not_found_error:
        print(file_not_found_error)

    # Convert dictionary data to Employee object
    for key_id in temp_db:
        spartan_id = temp_db[key_id]["ids"]
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

