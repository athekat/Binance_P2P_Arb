import json
import requests


headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "123",
    "content-type": "application/json",
    "Host": "p2p.binance.com",
    "Origin": "https://p2p.binance.com",
    "Pragma": "no-cache",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
}

data = {
  "asset": "BTC",
  "fiat": "ARS",
  "merchantCheck": True,
  "page": 1,
  "payTypes": [],
  "publisherType": None,
  "rows": 3,
  "tradeType": "BUY"
}

r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)

with open("btc.txt", "w", encoding='utf-8') as f:
    f.write(r.text)

data = {
  "asset": "ETH",
  "fiat": "ARS",
  "merchantCheck": True,
  "page": 1,
  "payTypes": [],
  "publisherType": None,
  "rows": 3,
  "tradeType": "BUY"
}

r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)

with open("eth.txt", "w", encoding='utf-8') as f:
    f.write(r.text)


data = {
  "asset": "USDT",
  "fiat": "ARS",
  "merchantCheck": True,
  "page": 1,
  "payTypes": [],
  "publisherType": None,
  "rows": 10,
  "tradeType": "BUY"
}

r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)

with open("usdt.txt", "w", encoding='utf-8') as f:
    f.write(r.text)


p2pusdt = "usdt.txt"
with open(p2pusdt) as file:
    p2pusdt_json = json.load(file)
p2pusdtok = p2pusdt_json['data'][3]['adv']['price']

p2peth = "eth.txt"
with open(p2peth) as file:
    p2peth_json = json.load(file)
p2pethok = p2peth_json['data'][2]['adv']['price']

p2pbtc = "btc.txt"
with open(p2pbtc) as file:
    p2pbtc_json = json.load(file)
p2pbtcok = p2pbtc_json['data'][2]['adv']['price']

apieth = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT")
apieth_json = apieth.json()
priceeth = apieth_json['price']

apibtc = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
apibtc_json = apibtc.json()
pricebtc = apibtc_json['price']

resulteth = ((((100 / int(float(p2pusdtok))) / int(float(priceeth))) * int(float(p2pethok))) / 100 - 1) * 100
resultbtc = ((((100 / int(float(p2pusdtok))) / int(float(pricebtc))) * int(float(p2pbtcok))) / 100 - 1) * 100

#Remove temp txt files
fn = "eth.txt"
fb = "btc.txt"
fa = "usdt.txt"

import os
if os.path.exists(fn):
    os.remove(fn)
if os.path.exists(fb):
    os.remove(fb)
if os.path.exists(fa):
    os.remove(fa)

print("\nP2P USDT: ", p2pusdtok, "\nP2P ETH: ", p2pethok, "\nP2P BTC: ", p2pbtcok, "\n\nETH Gains: ", resulteth, "%", "\nBTC Gains: ", resultbtc, "%", "\n\nPress ENTER to exit... ")
input()
