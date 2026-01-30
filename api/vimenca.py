import requests
from common.utils import add_currency
import logging

        
def get_currency_exchange_rates_vimenca() -> None:
    logging.info('')
    res = requests.get('https://devops.bancovimenca.com/api-proxy.php/api-proxy.php')
    if res.status_code != 200: 
        logging.error(f'Failed to fetch data from API with status code {res.status_code} and message: {res.content}')
        return res.content

    data = res.json()['data']
    for currency in data:
        currency_name = currency['coinName']
        if (currency_name != 'DOLAR EE.UU' and currency_name != 'EURO'): continue

        currency_name = 'USD' if currency_name == 'DOLAR EE.UU' else 'EUR'

        add_currency(
            'Vimenca',
            currency_name,
            currency['purchaseValue'],
            currency['saleValue']
        )
        