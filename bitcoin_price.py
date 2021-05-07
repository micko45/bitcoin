import requests


def getCoinList():

    url = "https://coingecko.p.rapidapi.com/coins/list"

    headers = {
        'x-rapidapi-key': "57ac8bd5b3msh179b4aba89e9d6ep13a72cjsn8f10693b7bd0",
        'x-rapidapi-host': "coingecko.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers)

    return response.json()

def getCoinValue(coin = 'bitcoin', cur = 'eur'):
    url = "https://coingecko.p.rapidapi.com/simple/price"

    querystring = {"ids":coin,"vs_currencies":cur}

    headers = {
        'x-rapidapi-key': "57ac8bd5b3msh179b4aba89e9d6ep13a72cjsn8f10693b7bd0",
        'x-rapidapi-host': "coingecko.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

getCoinValue()

# h = getCoinList()

#print(h[10])

# for i in h:
#     # print(i)
#     if i['name'] == 'Bitcoin':
#         print(i)

