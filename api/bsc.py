import requests
from common import add_currency

def get_currency_exchange_rates_bsc() -> None:
    query = """
    query GetCoins {
      coins {
        name
        price {
          buy
          sell
        }
      }
    }
    """
    
    headers = {
        'content-type': 'application/json'
    }
    res = requests.post(url='https://www.bsc.com.do/graphql', json={"query": query}, headers=headers)
    if res.status_code != 200: return res.content

    data = res.json()['data']
    for currency in data['coins']:
        currency_name = currency['name'].lstrip()
        if (currency_name != 'Dolar' and currency_name != 'Euro'): continue

        currency_name = 'USD' if currency_name == 'Dolar' else 'EUR'

        add_currency(
            'Santa Cruz',
            currency_name,
            currency['price']['buy'],
            currency['price']['sell']
        )
