import sqlite3 as sql
import requests
import json
import socket
from dotenv import dotenv_values


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
    con = sql.connect("gdp_database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from gdp_in_dollars")
   
    gdp_data = cur.fetchall()
    con.close()
    currency_value = get_currency_value(currency)
    return([[item['year'],item['gdp']*float(currency_value)] for item in gdp_data])