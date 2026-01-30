from common.utils import scraper, process_exchange_rates_data_scraped


def get_currency_exchange_rates_banesco() -> None:
    data_scraped = scraper(['calculator'], 'div', 'https://www.banesco.com.do/', findByclass_=True, getAttrsValues=True)
    data = data_scraped['calculator'] 
 
    search = ['data-currency-usd-rate-buy', 'data-currency-usd-rate-sell', 'data-currency-eur-rate-buy', 'data-currency-eur-rate-sell']
    currencies = {i:data[i] for i in data if i in search}
    process_exchange_rates_data_scraped(data=currencies, company_name= 'Banesco', param_search=['sell', 'buy'])
