import json
from typing import Final
import requests

class GetData:
    def __init__(self, url, api, currency):
        self.url = url
        self._api =  '924b8e007b6804e9d6c74acfb501e218'
        self.currency = currency

    @property
    def api(self):
        return self._api
    @api.setter
    def api(self, value):
        # You can add additional validation logic here if needed
        self._api = value

    def fetch_data(self):
        pay_amnt: dict = {'access_key': self.api}
        request = requests.get(url=self.url, params=pay_amnt)
        try:
            request.status_code == 200
            data = requests.get(url=self.url, params=pay_amnt)
            return data.json()
        except requests.exceptions.RequestException as e:
            print(f"This is the error that occurred: {e}")
            return None

    def get_currencies(self):
        returned_data = self.fetch_data()
        data_amount = returned_data.get('rates', None)
        base_currency = returned_data.get('base')
        base_currency_amnt = data_amount.get(base_currency)
        foreign_currency_amnt = data_amount.get(self.currency)
        return base_currency_amnt, foreign_currency_amnt, base_currency, self.currency

    @property
    def conversion_rate(self):
        ba, fv, base_currency, foreign_currency = self.get_currencies()
        conversion = ba / fv
        print(f"{base_currency} base amount to {foreign_currency} amount is {conversion:.2f}")
        return conversion

if __name__ == "__main__":
    BASE_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'
    # API_KEY: Final[str] = '924b8e007b6804e9d6c74acfb501e218'
    cs = GetData(BASE_URL, GetData.api,'AUD')
    conversion_result = cs.conversion_rate

    if conversion_result is not None:
        print(f'conversion result is {conversion_result}')
    else:
        print(f'something is wrong with conversion rate')

