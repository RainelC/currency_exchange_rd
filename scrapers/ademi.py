import logging

import requests
from bs4 import BeautifulSoup

from common.utils import process_exchange_rates_data_scraped


def get_currency_exchange_rates_ademi():
    url = "https://bancoademi.com.do/#popmake-6122"

    page = requests.get(url)

    if page.status_code != 200:
        logging.error({"status_code": page.status_code, "message": page.content})
        return {"status_code": page.status_code, "message": page.content}

    soup = BeautifulSoup(page.content, "html.parser")

    table = soup.find("table")

    trs = table.find_all("tr")
    currency: dict = {}
    for c in trs:
        text: str = c.text
        if text.lower().count("us") != 0 or text.lower().count("euro") != 0:
            currency_name = c.contents[1].text
            buying = c.contents[2].text.replace("DOP", "")
            selling = c.contents[3].text.replace("DOP", "")
            currency[f"{currency_name}-buying"] = float(buying)
            currency[f"{currency_name}-selling"] = float(selling)
    process_exchange_rates_data_scraped(
        data=currency, company_name="Ademi", param_search=["selling", "buying"]
    )
