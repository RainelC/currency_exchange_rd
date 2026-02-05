##--- Format: {"company_name": {"currency": {'buyingRate': $$.$, 'sellingRate': $$.$}, ...} ---##
##--- Example: 
"""
   { 
        BHD: {
            USD: {
                'buyingRate': 62.33, 
                'sellingRate': 64.44
            },
            EUR: {
                'buyingRate': 72.33, 
                'sellingRate': 74.44
            }
        },
        Popular : .......
   }
"""

get_currency_exchange_rates_query = """
    SELECT company.company_name, company.logo, ce.Currency_name, ce.Currency_prefix, ce.Buying_rate, ce.Selling_rate
    FROM currency_exchange as ce
    INNER JOIN company ON ce.company_id = company.Id
"""

get_companies_query = """
    SELECT * 
    FROM company
"""
