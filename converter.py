
import json
from typing import Final
import requests


class GetData:
    def __init__(self, url, api):
        self.url = url
        self.api = api

    def fetch_data(self):
        pay_amnt: dict = {'access_key': self.api}
        request = requests.get(url= self.url, params=pay_amnt)

        try:
            if request.status_code == 200:
                data  = requests.get(url=BASE_URL, params= pay_amnt)
                return data.json()
        except requests.exceptions.RequestException as e:
            print(f"This is error that occured {e}")

        return None

    def get_currency(self, currency_check):
        currency_check: str = currency_check.upper()

        data_currency = self.fetch_data().get('rates',None)
        if currency_check in data_currency.keys():
            return data_currency[currency_check]
        else:
            raise ValueError(f'{currency_check} does not appear in the currency keys')


# class Currency:
#     pass
#
# class GetCurrency:
#     pass
#
# class ConvertCurrency:
#     pass


if __name__ == "__main__":

    BASE_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'
    API_KEY: Final[str] = '924b8e007b6804e9d6c74acfb501e218'
    cs = GetData(BASE_URL, API_KEY)
    # print(cs.fetch_data())
    print(cs.get_currency('AWG'))

