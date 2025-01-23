import json
import pickle
import numpy as np
__locations = None
__data_columns = None
__model= None



def get_estimate(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1

    a = np.zeros(len(__data_columns))
    a[0] = sqft
    a[1] = bath
    a[2] = bhk
    if loc_index >= 0:
        a[loc_index] = 1


    return round(__model.predict([a])[0],2)


def get_location():
    return __locations

def load_saved():
    global __locations
    global __data_columns
    global __model
    with open("./useful/columns_json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations= __data_columns[3:]

    with open("./useful/banglore_price_model",'rb') as f:
        __model = pickle.load(f)


if __name__ == '__main__':
    load_saved()
    print(get_location())
    print(get_estimate('1st phase jp nagar',1000,2,2))