import requests
import json
API_URL = "https://randomuser.me/api/" 


def LoadData():
    """
    Load data from the API and return it as a list of dictionaries.
    """
    response = requests.get(API_URL)
    
    return data = response.json()['results'][0]

def TransformData(data): 
    """
    Transform the data into a format suitable for Kafka.
    """
    transformed_data = {
        "name": data['name']['first'] + " " + data['name']['last'],
        "email": data['email'],
        "street": data['location']['street']['number'] + " " + data['timezone']['description'],
        "city": data['location']['city'],
        "login": data['login']['username'] + " " + data['login']['password'],
        "phone": data['phone'],
        "cell": data['cell'] }
    return transformed_data
    
    