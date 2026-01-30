import logging
import requests
from bs4 import BeautifulSoup
 
##--- Format: {"company_name": {"currency": {'buyingRate': $$.$, 'sellingRate': $$.$}, ...} ---##
currencies_exchange_rates = {}

# Config logging
logging.basicConfig(level=logging.DEBUG)

def scraper(search:list, tag:str, url:str, findByclass_: bool = False, getAttrsValues: bool = False):
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
    
    session.get(url, headers=headers)
    
    page = session.get(url, headers=headers)
    if page.status_code != 200:
        return {'status_code': page.status_code, 'message': page.content}
    soup = BeautifulSoup(page.content, "html.parser")
    soup.find_all('tr')
    result = {}
    for key in search:
        """
        soup.find("div", class_="my-class") revisar si puedo ponerlo así y quitar el if
        # or
        soup.find("input", {"id": "nm"})
        """
        value = soup.find_all(tag, class_=key) if findByclass_ else soup.find_all(tag, id=key)
        if(value != []): 
            result[key] = value[0].attrs if getAttrsValues else value[0].text
 
    return result

def process_exchange_rates_data_scraped(data: dict, company_name: str, param_search: list, usd_index:str = 'us') -> None:
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
        selling = data[currency] if currency.count(param_search[0]) != 0 else selling
        buying = data[currency] if currency.count(param_search[1]) != 0 else buying
        if(selling != 0 and buying != 0):
            add_currency(
                company_name,
                currency_name,
                buying,
                selling
            )
            selling = 0
            buying = 0

def get_currency_exchange_rates_api(url:str): ## fdsafsaf
    res = requests.get(url)
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
    if company_name not in currencies_exchange_rates:
        currencies_exchange_rates[company_name] = {}
 
    currency_list = currencies_exchange_rates[company_name]
    currency_list[currency] = { 'buyingRate': buying_rate, 'sellingRate': selling_rate }
 
def show_exchange_rates() -> None:
    for i in currencies_exchange_rates:
        exchange = currencies_exchange_rates[i]
        USD={}
        EUR={}
 
        for moneda in exchange:
            if moneda == "USD":
                USD=exchange["USD"]
            else:
                EUR=exchange["EUR"]

        print(f"{i}:", end=" ")

        if USD !=  {}:
            print(f"Dolar: Compra: {USD["buyingRate"]} Vende {USD["sellingRate"]}" , end=" ")
        if EUR != {}:
            print(f"Euro: Compra: {EUR["buyingRate"]} Vende {EUR["sellingRate"]}")
