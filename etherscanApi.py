import requests
from decimal import Decimal
import certifi

address = "0xa320b8156189893c5da5f862b198f055fb1f16b0"
number_transactions = 100
url = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&startblock=0&endblock=99999999&page=1&offset=" + str(number_transactions) + "&sort=asc&apikey=YourApiKeyToken"

response = requests.get(url, verify=certifi.where())
address_content = response.json()
result = address_content.get("result")
data = {}

for n, transaction in enumerate(result):
        hash = transaction.get("hash")
        tx_from = transaction.get("from")
        tx_to = transaction.get("to")
        value = transaction.get("value")
        confirmations = transaction.get("confirmations")

        print("ID транзакции: ", n+1)
        print("HASH транзакции: ", hash)
        print("Отправитель: ", tx_from)
        print("Получатель: ", tx_to)

        if tx_from == address:
            print("Отправка")
        else:
            print("Получение")
        eth_value = Decimal(value) / Decimal("1000000000000000000")
        print("Количество: ", eth_value, "ETH")
        if int(confirmations) >= 16:
            print("Успешная транзакция!")
        else:
            print("Ошибка, код ошибки - ", confirmations)
        print(" ")