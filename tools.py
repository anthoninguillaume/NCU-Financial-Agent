import json

def get_exchange_rate(currency_pair: str):
    """
    Get exchange rate for a currency pair

    Input:
    - currency_pair (str): The 2 currencies names

    Output:
    - (json): The currency pair and the rate in a json
    """

    data = {
        "USD_TWD": "32.0",
        "JPY_TWD": "0.2",
        "EUR_USD": "1.2"
    }

    if currency_pair not in data:
        return json.dumps({"error": "Data not found"})

    return json.dumps({
        "currency_pair": currency_pair,
        "rate": data[currency_pair]
    })


def get_stock_price(symbol: str):
    """
    Get stock price of a company

    Input:
    - symbol (str): The company symbol

    Output:
    - (json): The company symbol and its stock price in a json
    """
    
    data = {
        "AAPL": "260.00",
        "TSLA": "430.00",
        "NVDA": "190.00"
    }

    if symbol not in data:
        return json.dumps({"error": "Data not found"})

    return json.dumps({
        "symbol": symbol,
        "price": data[symbol]
    })