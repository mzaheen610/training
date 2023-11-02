import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')

jsonData = response.json()


# for line in jsonData:
#     print(line['address']['city'])

#Posting data to the same api

data = {
    'id' : '13',
    "name" : "Robin",
    "place" : "Manchester"
}

response = requests.head('https://jsonplaceholder.typicode.com/users')
# info = response.json()
print(response.text)