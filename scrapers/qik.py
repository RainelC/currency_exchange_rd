import logging
import re

import requests
from bs4 import BeautifulSoup

from common.utils import process_exchange_rates_data_scraped


def get_currency_exchange_rates_qik():
    url = "https://qik.do/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    }
    page = requests.get(url, headers=headers)

    if page.status_code != 200:
        logging.error({"status_code": page.status_code, "message": page.content})
        return {"status_code": page.status_code, "message": page.content}

    soup = BeautifulSoup(page.content, "html.parser")

    target_h4 = None
    for h4 in soup.find_all("h4"):
        text = h4.get_text()
        if "Vendemos" in text and "Compramos" in text:
            target_h4 = h4
            break

    currency: dict = {}

    if target_h4:
        spans = target_h4.find_all("span")
        # Structure:
        # Vendemos: <span>RD$64.25 x US$1.00</span>
        # Compramos: <span>RD$62.35 x US$1.00</span>
        if len(spans) >= 2:
            # Span 0 corresponds to Selling (Vendemos)
            selling_text = spans[0].get_text().strip()
            # Span 1 corresponds to Buying (Compramos)
            buying_text = spans[1].get_text().strip()

            # Extract the numeric value after RD$
            sell_match = re.search(r"RD\$([\d.]+)", selling_text)
            buy_match = re.search(r"RD\$([\d.]+)", buying_text)

            if sell_match:
                currency["USD-selling"] = float(sell_match.group(1))
            if buy_match:
                currency["USD-buying"] = float(buy_match.group(1))
    process_exchange_rates_data_scraped(
        data=currency, company_name="Qik", param_search=["selling", "buying"]
    )
