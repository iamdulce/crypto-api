import requests

r = requests.get('https://rest.coinapi.io/v1/exchangerate/ETH/EUR?apikey=8B30787E-E140-44C4-B21A-E093FB2DAE75')

print(r.status_code)

print(r.text)