import logging
import json
import os 

logging.basicConfig(level=logging.DEBUG)

 
class CurrencyExchangeRatesJSON:
    def __init__(self):
        self.currencies_exchange_rates: dict = {} 
        self.file_name : str = 'currency_exchange_rates.json'
        self.file_path : str = 'data/' + self.file_name

    def save_data_json(self) -> None:
        logging.info(f'Saving data to JSON file: {self.file_name}')
        try:
            dir_path = os.path.dirname(self.file_path)
            os.makedirs(dir_path, exist_ok=True)

            with open(self.file_path, 'w') as f:
                json.dump(self.currencies_exchange_rates, f)
            logging.info(f'Data saved to JSON file: {self.file_name}')
        except Exception as e:
            logging.error(f'Failed to save data to JSON with error: {e}')



    def load_data_json(self) -> None:
        logging.info(f'Loading data from JSON file: {self.file_name}')
        if(os.path.exists(self.file_path)):
            try:
                with open(self.file_path, 'r') as f:
                    self.currencies_exchange_rates = json.load(f)
                logging.info(f'Data loaded from JSON file: {self.file_name}')
            except Exception as e:
                logging.error(f'Failed to load data from JSON with error: {e}')
        else:
            logging.info(f'Calling save_data_json() to create the JSON file: {self.file_name}')
            self.save_data_json()
            