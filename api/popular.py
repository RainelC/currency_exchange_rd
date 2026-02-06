import os
import logging
import requests
import dotenv

from common.utils import process_exchange_rates_data_scraped

dotenv.load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def obtener_token(client_id, client_secret):
    url_token = "https://api.us-east-a.apiconnect.ibmappdomain.cloud/apiportalpopular/bpdsandbox/bpd/Authentication/oauth2/token"
    
    # Datos para el flujo 'application' (Client Credentials)
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'scope_1'
    }
    
    response = requests.post(url_token, data=payload)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(f"Error al obtener token: {response.status_code}")
        return None

def consultar_tasa(token, client_id):
    url_tasa = "https://api.us-east-a.apiconnect.ibmappdomain.cloud/apiportalpopular/bpdsandbox/consultatasa/consultaTasa"
    
    headers = {
        'X-IBM-Client-Id': client_id,
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    
    response = requests.get(url_tasa, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error en la consulta: {response.status_code} - {response.text}"


def get_currency_exchange_rates_popular() -> None:
    token = obtener_token(CLIENT_ID, CLIENT_SECRET)

    if token:
        data = consultar_tasa(token, CLIENT_ID)
        currencies = {}
        for currency in data['monedas']['moneda']:
            {currency.name: currency.text for currency in data}
            currencies[currency['descripcion']] = {
                'sell': currency['venta'],
                'buy': currency['compra']
            }

        process_exchange_rates_data_scraped(data=currencies, company_name='Popular', param_search=['sell', 'buy'], usd_index='Dollar')


"""
{
    "monedas": {
        "moneda": [
            {
                "descripcion": "USD",
                "compra": 58.55,
                "venta": 60.35
            },
            {
                "descripcion": "EUR",
                "compra": 62.30,
                "venta": 65.90
            }
        ],
        "fechaConsulta": "2026-2-5 - 21:38:38"
    }
}
"""