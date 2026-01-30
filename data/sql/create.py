company_table = """
    CREATE TABLE company ( 
        Id INTEGER, 
        Name TEXT, 
        Site TEXT, 
        Logo TEXT ##could be a BLOD
    )
"""

currency_table = """
    CREATE TABLE currency ( 
        Id INTEGER, 
        Name Varchar(255), 
        Prefix varchar(255)
    )
"""

currency_exchange = """
    ID INTEGER,
    Company_id INTEGER REFERENCES company(id),
    currency_id INTEGER REFERENCES currency(id),
"""