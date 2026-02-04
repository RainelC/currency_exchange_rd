import logging
import requests
from bs4 import BeautifulSoup
from data.json import CurrencyExchangeRatesJSON 

 
# Config logging
logging.basicConfig(level=logging.DEBUG)

json = CurrencyExchangeRatesJSON()

def scraper(search:list, tag:str, url:str, findByclass_: bool = False, getAttrsValues: bool = False, re:str = None):
    """
    Docstring for scraper
    
    :param search: Description
    :type search: list
    :param tag: Description
    :type tag: str
    :param url: Description
    :type url: str
    :param findByclass_: Description
    :type findByclass_: bool
    :param getAttrsValues: Description
    :type getAttrsValues: bool
    """
    session = requests.Session()
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    page = session.get(url, headers=headers)
    
    if page.status_code != 200:
        return {'status_code': page.status_code, 'message': page.content}
    soup = BeautifulSoup(page.content, "html.parser")
    soup.find_all('tr')
    result = {}
    indentificator = 'id'
    if findByclass_: indentificator = 'class'
    for key in search:
        value = soup.find(tag, {indentificator: key})
        if(value != []): 
            result[key] = value.attrs if getAttrsValues else value.text
 
    return result

def process_exchange_rates_data_scraped(data: dict, company_name: str, param_search: list, usd_index:str = 'us', only_buy: bool = False) -> None:
    """
    Process exchange rates for scraped data.
    
    :param data: Scraped data
    :type data: dict
    :param company_name: Name of company or bank
    :type company_name: str
    :param param_search: A list with the word to be searched for to select the sale and purchase value in this exact order.
    :type param_search: list
    :param usd_index: the keyword containing the USD value in the data
    :type usd_index: str    
    """
    selling = 0
    buying = 0
    for currency in data:
        currency_name = 'USD' if currency.lower().count(usd_index.lower()) != 0  else "EUR"
        if(only_buy):
            buying = data[currency] if currency.lower().count(param_search[0].lower()) != 0 else buying
        else:
            selling = data[currency] if currency.lower().count(param_search[0].lower()) != 0 else selling
            buying = data[currency] if currency.lower().count(param_search[1].lower()) != 0 else buying
        if((selling != 0 and buying != 0) or (buying != 0 and only_buy)):
            add_currency(
                company_name,
                currency_name,
                buying,
                selling
            )
            selling = 0
            buying = 0


##-------------- Manage currency data --------------##

def add_currency(company_name: str, currency: str, buying_rate: float = 0, selling_rate: float = 0) -> None:
    """
    Docstring for add_currency
    
    :param company_name: Description
    :type company_name: str
    :param currency: Description
    :type currency: str
    :param buying_rate: Description
    :type buying_rate: float
    :param selling_rate: Description
    :type selling_rate: float
    """
    json.load_data_json()

    logging.info(f'Adding currency {currency} to {company_name}')
    if company_name not in json.currencies_exchange_rates:
        json.currencies_exchange_rates[company_name] = {}
 
    currency_list = json.currencies_exchange_rates[company_name]
    if currency not in currency_list:
        currency_list[currency] = {}

    if(buying_rate != 0):    
        currency_list[currency]['buyingRate'] = float(buying_rate)
    if(selling_rate != 0):
        currency_list[currency]['sellingRate'] = float(selling_rate)

    json.save_data_json()
    logging.info(f'Currency {currency} added to {company_name}')
 
def show_exchange_rates() -> None:
    json.load_data_json()
    for i in json.currencies_exchange_rates:
        exchange = json.currencies_exchange_rates[i]
        USD={}
        EUR={}
 
        for moneda in exchange:
            if moneda == "USD":
                USD=exchange["USD"]
            else:
                EUR=exchange["EUR"]

        print(f"{i}:", end=" ")

        if USD !=  {}:
           for key in USD:
                print(f"Dolar: {key}: {USD[key]}", end=" ")
        if EUR != {}:
            for key in EUR:
                print(f"Euro: {key}: {EUR[key]}", end=" ")
        print('')

