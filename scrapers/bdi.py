from common.utils import scraper, process_exchange_rates_data_scraped

def get_currency_exchange_rates_bdi() -> None:
    # Keywords to search on the web
    search = ['rd-compra', 'rd-venta', 'rd-euro-compra', 'rd-euro-venta']

    # Data scraped 
    data = scraper(search=search, tag='input', url='https://www.bdi.com.do/#', getAttrsValues=True)

    # Get USD values and correct names
    data['rd-us-compra'] = data.pop('rd-compra')['value']
    data['rd-us-venta'] = data.pop('rd-venta')['value']

    # Get EUR values
    data.update({'rd-euro-compra': data['rd-euro-compra']['value']})
    data.update({'rd-euro-venta' : data['rd-euro-venta']['value']})

    process_exchange_rates_data_scraped(data=data, company_name='BDI', param_search=['venta', 'compra'] )
