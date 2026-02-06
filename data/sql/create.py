company_table = """
    CREATE TABLE company ( 
        Id INTEGER, 
        company_name TEXT, 
        website TEXT, 
        Logo TEXT
    )
"""

currency_exchange_table = """
    CREATE TABLE currency_exchange (
        Id INTEGER,
        Company_id INTEGER REFERENCES company(Id),
        Currency_name TEXT, 
        Currency_prefix TEXT
        Buying_rate REAL,
        Selling_rate REAL,
        Date_created TEXT
    )
"""