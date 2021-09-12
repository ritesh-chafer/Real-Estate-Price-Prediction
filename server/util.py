import pickle

__locations = None
__data_columns = None
__model = None

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loadinf saved artifacts...start")
    global __locations
    global __data_columns

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

