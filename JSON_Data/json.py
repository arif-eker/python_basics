# JSON İle Çalışmak

import json

data = '{"firstName": "Arif","lastName": "Eker"}'

y = json.loads(data)

print(type(y))

customer = {"ad": "Arif",
            "email": "xyz@gmail.com"}

customerJson = json.dumps(customer)
print(type(customerJson))
print(customerJson)