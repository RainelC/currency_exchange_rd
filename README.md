# Currency Exchange Rates RD

A Python tool to fetch and display the latest currency exchange rates (USD and EUR) from major financial institutions in the Dominican Republic.

## Features

- **Wide Coverage**: Scrapes data from multiple leading banks and exchange agents:
  - Banco Popular
  - Banreservas
  - BHD
  - Banco Santa Cruz (BSC)
  - Proamerica
  - Vimenca
  - Cibao
  - Caribe Express
  - BDI
  - Banesco
- **Consolidated Output**: Aggregates buying and selling rates for USD and EUR in a clean format.
- **Extensible**: Modular design allowing easy addition of new institutions.
- **API and Scraping Support**: Handles both RESTful APIs and web scraping for data retrieval.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd currency_exchange_rd
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv

   # Windows
   .\venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**CLOUDFLARE_API_TOKEN = 'AyH6d1C-lfJan5ZYJUm43PVVD9QxoD3EprG2L8Al'
CLOUDFLARE_USER_ID = '52071f92dd2c7de942593581d9d6d58f'
CLOUDFLARE_DB_ID='0125cb8f-f4e7-4e3f-8a5e-b6ce2f2e1ce3'
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file:**
   Copy the example environment variables and add your credentials (e.g., API tokens for external services like Cloudflare). Example:
   ```
   CLOUDFLARE_API_TOKEN=your_token_here
   CLOUDFLARE_USER_ID=your_user_id_here
   CLOUDFLARE_DB_ID=your_db_id_here
   ```
   Ensure this file is not committed to version control (add `.env` to `.gitignore`).

## Usage

Run the main script to fetch and display the current exchange rates:

```bash
python main.py
```

## Structure

- `api/`: Modules interacting with specific API endpoints or structured data sources (e.g., XML/JSON endpoints).
- `scrapers/`: Modules that scrape HTML content from bank websites.
- `common/`: Shared utilities for processing and displaying data.
- `data/`: (If applicable) Directory for storing scraped data.
- `main.py`: Entry point of the application.

## Disclaimer

This tool is for informational purposes only. Exchange rates can change rapidly and may not reflect real-time values. Always verify with the respective financial institution before making any transactions. Respect website terms of service and avoid excessive requests to prevent blocking.

## License

[Specify license, e.g., MIT] - See LICENSE file for details.
