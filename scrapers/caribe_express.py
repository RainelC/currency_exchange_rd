import logging
import requests
from bs4 import BeautifulSoup
from common.utils import scraper, process_exchange_rates_data_scraped

def get_currency_exchange_rates_caribe_express():
    logging.info('Scraping Caribe Express')
    page = requests.get('https://caribeexpress.com.do/')

    if page.status_code != 200:
        logging.error({'status_code': page.status_code, 'message': page.content})
        return {'status_code': page.status_code, 'message': page.content}

    logging.info('Scraping Caribe Express finished')
    soup = BeautifulSoup(page.content, "html.parser")

    data = soup.find_all(class_='plan plan one-third column')
    logging.info('Processing exchange rates for Caribe Express')
    currency={}
    for c in data:
        text:str = c.text 
        if(text.lower().count('dolares americanos') != 0 or text.lower().count('euro') != 0):
            text = text.strip().replace('$', '').replace('\r', '').strip() 
            text = text.split('\n')
            textList = [tet.strip() for tet in text if tet.strip() != '']
            currency[f'{textList[0]}-{textList[2]}'] = textList[1]

    process_exchange_rates_data_scraped(data=currency, company_name='Caribe Express', param_search=['Compra'], usd_index='Dolar', only_buy=True)
    logging.info('Exchange rates processed for Caribe Express')
