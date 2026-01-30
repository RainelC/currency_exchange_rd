import os
from dotenv import load_dotenv
from cloudflare import Cloudflare
from .sql import sql as query

# query = """
# CREATE TABLE IF NOT EXISTS exchange_rates (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     company_name TEXT NOT NULL,
#     currency TEXT NOT NULL,
#     buying_rate REAL NOT NULL,
#     selling_rate REAL NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );
# """

load_dotenv()

API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
if not API_TOKEN: raise ValueError("CLOUDFLARE_API_TOKEN enviroment variable not set")

client = Cloudflare()

CLOUDFLARE_USER_ID = os.getenv('CLOUDFLARE_USER_ID')
CLOUDFLARE_DB_ID = os.getenv('CLOUDFLARE_DB_ID')


try:
    result = client.d1.database(
        CLOUDFLARE_USER_ID, 
        CLOUDFLARE_DB_ID,
        sql=query
    )
    print(result)
except Exception as e:
    print(e)


def add_currency(company_name: str, currency: str, buying_rate: float, selling_rate: float) -> None:
    try:
        result = client.d1.database(
            CLOUDFLARE_USER_ID, 
            CLOUDFLARE_DB_ID,
            sql=query.add_currency
        )
        print(result)
    except Exception as e:
        print(e)


def get_currency_exchange_rates(company_name: str, currency: str) -> None:
    try:
        result = client.d1.database(
            CLOUDFLARE_USER_ID, 
            CLOUDFLARE_DB_ID,
            sql=query.get_currency_exchange_rates
        )
        print(result)
    except Exception as e:
        print(e)