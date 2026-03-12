tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "get_exchange_rate",
            "description": "Get exchange rate for a currency pair",
            "strict": True,
            "parameters": {
                "type": "object",
                "properties": {
                    "currency_pair": {
                        "type": "string",
                        "description": "Currency pair like USD_TWD"
                    }
                },
                "required": ["currency_pair"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Get stock price",
            "strict": True,
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock symbol like AAPL"
                    }
                },
                "required": ["symbol"],
                "additionalProperties": False
            }
        }
    }
]