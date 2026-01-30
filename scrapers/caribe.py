from common.utils import process_exchange_rates_data_scraped, scraper

def get_currency_exchange_rates_caribe() -> None:
    # Keywords to search on the web
    search = ['mus_buy_num', 'mus_sell_num', 'meur_buy_num', 'meur_sell_num']
    
    # Data scraped
    data = scraper(search, 'span', 'https://www.bancocaribe.com.do/')
    
    process_exchange_rates_data_scraped(data=data, company_name='Caribe', param_search=['sell', 'buy'] )