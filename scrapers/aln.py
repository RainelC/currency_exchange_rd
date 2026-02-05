import logging
import requests
from bs4 import BeautifulSoup
from common.utils import process_exchange_rates_data_scraped

def get_currency_exchange_rates_aln():
    logging.info('Getting currency exchange rates for ALN')
    page = requests.get('https://asociacionlanacional.com.do/')

    if page.status_code != 200:
        logging.error({'status_code': page.status_code, 'message': page.content})
        return {'status_code': page.status_code, 'message': page.content}

    logging.info('Scraping ALN finished')
    soup = BeautifulSoup(page.content, "html.parser")

    tasas_modal = soup.find(id="tasasModal")
    data = {}
    logging.info('Processing exchange rates for ALN')
    if tasas_modal:
        for h5 in tasas_modal.find_all('h5'):
            if 'Compra USD' in h5.text:
                data['compra-usd'] = h5.find('span').text
            elif 'Venta USD' in h5.text:
                data['venta-usd'] = h5.find('span').text
    else:
        logging.error("Tasas container not found")
        return {'status_code': 404, 'message': 'Tasas container not found'}

    process_exchange_rates_data_scraped(data=data, company_name='Asociacion La Nacional', param_search=['venta', 'compra'])
    logging.info('Exchange rates processed for ALN')
