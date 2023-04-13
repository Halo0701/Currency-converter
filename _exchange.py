import requests
import json

# https://api.exchangeratesapi.io/latest?base= => type the currency that u want to exchange

api_url = "https://api.exchangeratesapi.io/latest?base="

exchanged_currency = input("exchanged currency type: ")
bought_currency = input("bought currency type: ")

amount = int(input(f"the amount {exchanged_currency} that you want to exchange ?"))

result = requests.get(api_url + exchanged_currency)
result = json.loads(result.text)

print(" 1 {0} = {1} {2}".format(exchanged_currency,result["rates"][bought_currency,bought_currency]))
print("{0} {1} = {2} {3}".format(amount,exchanged_currency,amount*result[r"rates"][bought_currency]))