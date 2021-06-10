from coinapi_rest_v1.restapi import CoinAPIv1
import requests
import json

# Get metadata on all Crypto Exchanges
url = 'https://rest-sandbox.coinapi.io/v1/exchanges'
headers = {'X-CoinAPI-Key' : 'YOUR-COINAPI-KEY-HERE'}
response = requests.get(url, headers=headers)

# Write out metadata to new file

# TODO: Check if file is present. If so then add _#,
#       incrementing # by 1 and repeating check until
#       no file found.
# TODO: Check if folder for MM-YYYY exists under /Exchanges-Metadata

json_response = response.json()
prettified_metadata = json.dumps(json_response, indent=4)
with open('exchanges_meta.txt', 'w') as f:
    f.write(prettified_metadata)

# Show Exchange names 
names = []
exch_ids = []
for exchange in json_response:
    for k, v in exchange.items():
        if k == 'name':
            names.append(v)
        if k == 'exchange_id':
            exch_ids.append(v)

# Create dictionary of Exchange names and IDs
exchanges = dict(zip(names, exch_ids))

# Output names with IDs
line = ''
for k, v in exchanges.items():
    ex = '{} ({})'.format(v, k)
    if (len(line) + len(ex) + 1) < 79:
        line += (ex + ' ')
    else:
        print(line)
        line = (ex + ' ')
