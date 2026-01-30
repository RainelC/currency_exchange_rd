from common.utils import scraper, process_exchange_rates_data_scraped

def get_currency_exchange_rates_reservas() -> None:
    # Keywords to search on the web
    search = ['tasacambio-compraUS', 'tasacambio-ventaUS', 'tasacambio-compraEU', 'tasacambio-ventaEU']
    # Data scraped
    data = scraper(search, 'td', 'https://www.banreservas.com/', True)
    
    process_exchange_rates_data_scraped(data=data, company_name='Reservas', param_search=['venta', 'compra'] )
