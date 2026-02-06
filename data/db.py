import os
from dotenv import load_dotenv
from cloudflare import Cloudflare, BadRequestError
from .sql.add import add_company_query, add_currency_exchange_query
from .sql.create import company_table, currency_exchange_table
from .sql.get import get_companies_query
load_dotenv()

API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
if not API_TOKEN: raise ValueError("CLOUDFLARE_API_TOKEN enviroment variable not set")

client = Cloudflare(
    api_token= os.getenv('CLOUDFLARE_API_TOKEN')
)

CLOUDFLARE_USER_ID = os.getenv('CLOUDFLARE_USER_ID')
CLOUDFLARE_DB_ID = os.getenv('CLOUDFLARE_DB_ID')


def add_currency_exchange(company_id: str, currency_name: str, currency_prefix:str, buying_rate: float, selling_rate: float) -> None:
    try:
        page = client.d1.database.query(
            account_id=CLOUDFLARE_USER_ID,
            database_id=CLOUDFLARE_DB_ID,
            sql=add_currency_exchange_query(company_id, currency_name, currency_prefix, buying_rate, selling_rate)
        )
        result = page.result[0]
        if(result.success):
            print(result.results)
    except Exception as e:
        print(e)


def add_company(company_name: str, website: str, logo: str) -> None:
    try:
        page = client.d1.database.query(
            account_id=CLOUDFLARE_USER_ID,
            database_id=CLOUDFLARE_DB_ID,
            sql=add_company_query(company_name, website, logo)
        )
        result = page.result[0]
        if(result.success):
            print(result.results)
    except Exception as e:
        print(type(e))
        if(type(e) == BadRequestError and str(e).count('no such table') != 0):
            create_company_table()
            return add_company(company_name, website, logo)
        print(e)


### -------GET------- ###
def get_companies() -> list[dict]:
    try: 
        page = client.d1.database.query(
            account_id=CLOUDFLARE_USER_ID,
            database_id=CLOUDFLARE_DB_ID,
            sql=get_companies_query
        )
        result = page.result[0]
        if(result.success):
            print(result.results)
    except Exception as e:
        print(e)


### -------CREATE------- ###
def create_company_table() -> list[dict]:
    try: 
        page = client.d1.database.query(
            account_id=CLOUDFLARE_USER_ID,
            database_id=CLOUDFLARE_DB_ID,
            sql=company_table
        )
        result = page.result[0]
        if(result.success):
            print(result.results)
    except Exception as e:
        print(e)