import requests
from prettytable import PrettyTable

listings_api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/' \
               'listings/latest?sort=market_cap&start=1&limit=100&convert=USD'

headers = {
  'content-type': 'application/json',
  'X-CMC_PRO_API_KEY': '9bcbb4c7-3b19-40a4-9864-1bf80d679a9d',
}

listings_data = requests.get(listings_api,headers=headers).json()['data']


table = PrettyTable()
table.field_names = ['Name', 'Symbol', 'Price', 'Volume', 'MarketCap', 'Change 1h',
                     'Change 24h', 'Change 7d']


for coin in listings_data:

    name = coin['name']
    symbol = coin['symbol']
    coin_data = coin['quote']['USD']


    table.add_row([name,
                   symbol,
                   coin_data['price'],
                   coin_data['volume_24h'],
                   coin_data['market_cap'],
                   coin_data['percent_change_1h'],
                   coin_data['percent_change_24h'],
                   coin_data['percent_change_7d']])
    


field = input('''
Press: 
1. Sort by price
2. Sort by 24 Hour Volume
3. Sort by MarketCap
4. Sort by 1 Hour Change
5. Sort by 24 Hour Change
6. Sort by 7 Day Change

''')
try:
  field = int(field)

except:
  print('''
  input must be a number between 1-6
  ''')
  exit()

if field not in [1,2,3,4,5,6]: 
    print('''
    input must be a number between 1-6
    ''')
    exit()
else:
    table.sortby = table.field_names[field + 1]
    table.reversesort = True
    print(table)
