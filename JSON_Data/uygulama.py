# uygulama
# user.json daki verileri aldığım yer : https://jsonplaceholder.typicode.com/users


import json

# json dosyasını okumak için :

# with ile okuyunca dosya otomatik kapanır.

with open("JSON_Data/users.json") as users:
    data = json.load(users)
    # print(data)
    print(data[0])  # bu şekilde 0. dataya ulaşırız. [0] yazmadan yaparsak tüm bilgileri gösterir.
    print(data[0]["username"])
    print(data[0]["address"]["street"])
    print(data[0]["address"]["geo"]["lat"])
