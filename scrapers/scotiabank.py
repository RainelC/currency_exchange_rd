import requests
from bs4 import BeautifulSoup 
from common.utils import process_exchange_rates_data_scraped
import logging

def get_currency_exchange_rates_scotiabank():
    url = "https://do.scotiabank.com/banca-personal/tarifas/tasas-de-cambio.html"

    page = requests.get(url)

    if page.status_code != 200:
        logging.error({'status_code': page.status_code, 'message': page.content})
        return {'status_code': page.status_code, 'message': page.content}

    soup = BeautifulSoup(page.content, "html.parser")

    table = soup.find('table')

    trs = table.find_all('tr')
    currency={}
    for c in trs:
        text:str = c.text 
        if((text.lower().count('us') !=  0 and text.lower().count('sucursales') != 0) or text.lower().count('euro') != 0):
            text = text.strip().replace('\xa0', '').replace('\n', ' ').strip() 
            text = text.replace('Europa', '').split(' ')
            textList = [tet.strip() for tet in text if tet.strip() != '']
            currency[f'{textList[0]}-compra'] = textList[-2]
            currency[f'{textList[0]}-venta'] = textList[-1]

    process_exchange_rates_data_scraped(data=currency, company_name='Scotiabank', param_search=['venta', 'compra'])
    logging.info('Exchange rates processed for Scotiabank')