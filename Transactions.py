import requests
import json

contract = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
key = "DDWU8NFBHDEIT4M4CHWWRVNI78SUF891GF"

url = 'https://api.etherscan.io/api?module=account&action=tokennfttx&contractaddress=0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D&page=1&offset=10000&sort=desc&apikey=DDWU8NFBHDEIT4M4CHWWRVNI78SUF891GF'

data = requests.get(url)
obj = data.json()
print(data.text)
print(len(obj['result']))