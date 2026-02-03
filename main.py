from api.proamerica import get_currency_exchange_rates_proamerica
from api.vimenca import get_currency_exchange_rates_vimenca
from api.bhd import get_currency_exchange_rates_bhd
from api.bsc import get_currency_exchange_rates_bsc 
from api.cibao import get_currency_exchange_rates_cibao
from api.popular import get_currency_exchange_rates_popular
from scrapers.banesco import get_currency_exchange_rates_banesco
from scrapers.bdi import get_currency_exchange_rates_bdi
from scrapers.caribe import get_currency_exchange_rates_caribe
from scrapers.reservas import get_currency_exchange_rates_reservas
from common.utils import show_exchange_rates

import logging
 
logging.basicConfig(level=logging.DEBUG)
"""
[INFO]
[DEBUG]
[WARNING]
[ERROR]
[CRITICAL]
"""

def main() -> None:
    logging.info('[INFO] Starting currency exchange rates scrapers')
    get_currency_exchange_rates_bhd() 
    get_currency_exchange_rates_proamerica() 
    get_currency_exchange_rates_cibao() 
    get_currency_exchange_rates_reservas()
    # get_currency_exchange_rates_vimenca()    
    get_currency_exchange_rates_bsc() 
    get_currency_exchange_rates_caribe() 
    # get_currency_exchange_rates_popular() 
    get_currency_exchange_rates_bdi() 
    get_currency_exchange_rates_banesco() 
    show_exchange_rates()
    logging.info('[INFO] Currency exchange rates scrapers finished')

if __name__ == '__main__':
    main()
 