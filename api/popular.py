import requests
import logging
from bs4 import BeautifulSoup
from common.utils import process_exchange_rates_data_scraped

def get_currency_exchange_rates_popular() -> None:
    # Keywords to search on the xml
    search = ['DollarBuyRate', 'DollarSellRate', 'EuroBuyRate', 'EuroSellRate']

    logging.info('Fetching data from https://popularenlinea.com/_api')
    res = requests.get("https://popularenlinea.com/_api/web/lists/getbytitle('Rates')/items")

    if res.status_code != 200:
        logging.error(f'status_code: {res.status_code}, message: {res.content}')
        return {'status_code': res.status_code, 'message': res.content}
    
    logging.info('Data fetched')
    soup = BeautifulSoup(res.content, 'lxml-xml')
    
    content = soup.find('content')
    data = content.find_all(search)
    currencies = {currency.name: currency.text for currency in data}
    process_exchange_rates_data_scraped(data=currencies, company_name='Popular', param_search=['Sell', 'Buy'], usd_index='Dollar')
