# NCU Financial Agent

A CLI AI financial assistant built in Python.
It connects to a Large Language Model (LLM) and uses tool/function calling to retrieve financial information from mock data.


# Available Tools

- get_stock_price(symbol)
- get_exchange_rate(currency_pair)


# Installation

1. Clone the repository.
2. Install dependencies (openai and python-dotenv).


# API Key Setup

Create a .env file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```
The API key is loaded securely using **python-dotenv**.


# Run the Agent

```bash
python main.py
```


# Project Structure

```
NCU-Financial-Agent
│
├── main.py        # agent loop
├── tools.py       # mock financial functions
├── schemas.py     # tool schemas
├── config.py      # API configuration
├── .env
└── README.md
```
