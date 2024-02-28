import requests
import json

class APIException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={base}&vs_currencies={quote}"
        response = requests.get(url)
        data = json.loads(response.text)

        if base not in data or quote not in data[base]:
            raise APIException(f"Не удалось получить курс {base}/{quote}")

        price = data[base][quote]
        total = price * amount
        return total