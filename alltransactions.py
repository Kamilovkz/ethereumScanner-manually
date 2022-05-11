from operator import add
from unittest import result
import requests
from decimal import Decimal
import certifi
from collections import defaultdict

number_transactions = 100

def get_transactions_by_address(address, number_transactions):
    url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + \
    "&startblock=0&endblock=99999999&page=1&offset=" + str(
        number_transactions) + "&sort=asc&apikey=YourApiKeyToken"
    
    response = requests.get(url, verify=certifi.where())
    address_content = response.json()
    result = address_content.get("result")
    data = defaultdict(dict)

    for n, transaction in enumerate(result):
        hash = transaction.get("hash")
        tx_from = transaction.get("from")
        tx_to = transaction.get("to")
        value = transaction.get("value")
        confirmations = transaction.get("confirmations")
        if tx_from == address:
            out = ("Отправка")
        else:
            out = ("Получение")
        eth_value = Decimal(value) / Decimal("1000000000000000000")
        if int(confirmations) >= 16:
            confirmed = ("Успешная транзакция!")
        else:
            confirmed = ("Ошибка, код ошибки - ", confirmations)

        data[n]["hash"] = hash
        data[n]["tx_from"] = tx_from
        data[n]["tx_to"] = tx_to
        data[n]["eth_value"] = eth_value
        data[n]["out"] = out 
        data[n]["confirmed"] = confirmed
    return data

address1 = get_transactions_by_address("0xa320b8156189893c5da5f862b198f055fb1f16b0", 25)
# for something in address1:
#     hash1 = something.get("hash")
#     print(hash1)
#print(address1[0]("hash"))
for key, value in address1.items():
    print('ID:', key+1)
    # Again iterate over the nested dictionary
    for tx_from, eth_value in value.items():
        print(tx_from, ' : ', eth_value)