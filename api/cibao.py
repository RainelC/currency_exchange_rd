import requests
from common.utils import add_currency

def get_currency_exchange_rates_cibao() -> None:
    #  b'[{"codigoMoneda":"US$","compra":"62.00","nombre":"US$","venta":"64.00"},{"codigoMoneda":"EUR$","compra":"73.00","nombre":"EUR$","venta":"77.50"}]'
    res = requests.get('https://cibao.com.do/api/Coins/GetCoins')
    data = res.json()
    for currency in data:
        currency_name = 'USD' if currency['codigoMoneda'] == "US$" else 'EUR'
        add_currency(
            'Cibao', 
            currency_name, 
            currency['compra'], 
            currency['venta']
        )