import requests
from common.utils import add_currency


def get_currency_exchange_rates_proamerica() -> None:
    res = requests.get("https://promerica.com.do/umbraco/Surface/TipoCambio/Run?json=%7B%22operacion%22%3A2%7D")
    data = res.json()["value"]
    for exchange in data:
        if exchange["currency"] == '214': continue
        exchange["currency"]  = 'USD' if exchange["description"] == 'DOLARES US$' else "EUR"
        add_currency(
            'Promerica',
            exchange["currency"],
            exchange["buys"],
            exchange["sales"]
            )