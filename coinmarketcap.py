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
    

table.sortby = table.field_names[4]
table.reversesort = True
print(table)