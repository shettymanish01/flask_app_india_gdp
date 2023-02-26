import requests
import json
import socket
from dotenv import dotenv_values
from .database import Database


secrets = dotenv_values(".env")


def get_host_and_ip():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return str(host),str(ip)

def get_currency_value(currency):
    if currency == 'Indian Rs':
        currency_json=json.loads(requests.get('https://api.currencyfreaks.com/latest?apikey='+secrets["CURRENCYFREAKS_API_KEY"]).text)
        currency_value=currency_json['rates']['INR']
    else:
        currency_value = 1
        
    return currency_value
        
    
def get_gdp_data(currency):
    query = "select * from gdp_in_dollars"
    with Database('gdp_database.db') as db:
        gdp_data = db.query(query)
    
    
    currency_value = get_currency_value(currency)
    return([[item['year'],item['gdp']*float(currency_value)] for item in gdp_data])
