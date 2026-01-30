import requests
from common.utils import add_currency


def get_currency_exchange_rates_bhd() -> None:
    """
    Get currency exchange rates from BHD API.
    """
    res = requests.get("https://backend.bhd.com.do/api/modal-cambio-rate?populate=deep")
    data = res.json()
    exchange_rates = data["data"]["attributes"]["exchangeRates"]
    for exchange in exchange_rates:
        add_currency(
            "BHD",
            exchange["currency"],
            exchange["buyingRate"],
            exchange["sellingRate"]
        )