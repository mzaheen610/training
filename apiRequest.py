import requests

response = requests.get("https://reqres.in/api/users?page=2")
# print(type(response))

json = response.json()

# for elem in json:
#     print(elem)
# print(json["data"])
userData = json["data"]
for elem in userData:
    firstname = elem["first_name"]
    lastname = elem["last_name"]
    print(firstname,lastname)

