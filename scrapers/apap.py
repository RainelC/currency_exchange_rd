import requests
from bs4 import BeautifulSoup
import re
import logging
from common.utils import process_exchange_rates_data_scraped

logging.basicConfig(level=logging.DEBUG)

def get_currency_exchange_rates_apap():
    search = ['currency-buy-USD', 'currency-sell-USD', 'currency-buy-EUR', 'currency-sell-EUR'] #apap
    url = "https://apap.com.do/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    Session = requests.Session()

    try:
        logging.info(f"Requesting data from {url}")
        response = Session.get(url, headers=headers)

        if response.status_code != 200:
            logging.error(f"Failed to retrieve data: {response.status_code}")
            raise Exception(f"Failed to retrieve data: {response.status_code}")

        logging.info(f"Data retrieved successfully")

        soup = BeautifulSoup(response.text, 'html.parser')
        
        script_tag = soup.find('script', text=re.compile('getRates'))
        
        data = {}
        if(script_tag):
            content = script_tag.string

            for key in search:
                data[key] = re.search(rf'{key}"\)\.html\(addZeroes\(([\d\.]+)', content).group(1)

            process_exchange_rates_data_scraped(data=data, company_name='APAP', param_search=['sell', 'buy'])
    except requests.exceptions.RequestException as e:
        logging.error(f"Error: {e}")    
    