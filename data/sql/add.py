def add_company_query(company_name: str, website:str, logo:str) -> str: 
     return f"""
        INSERT INTO company(company_name, website, logo)
        VALUES ('{company_name}', '{website}', '{logo}')   
    """

def add_currency_exchange_query(company_id: str, currency_name: str, currency_prefix: str, buying_rate: float, selling_rate: float) -> str:
    return f"""
        INSERT INTO currency_exchange(Company_id, currency_name, Currency_prefix, Buying_rate, Selling_rate)
        VALUES ('{company_id}', '{currency_name}', '{currency_prefix}', {buying_rate}, {selling_rate})
    """