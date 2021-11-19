import json

#with open('client.json') as client:
#    client_dict = json.loads(client.read())

#es lo mismo

with open('client.json') as client:
    client_dict = json.load(client)

print(client_dict)
print(client_dict['name'])
print(client_dict['interest'])
print(client_dict['interest'][2])
print(client_dict['last articles'])
print(client_dict['last articles']['clothes'])

person_dict = {

        'name':'clark',
        'lastname': 'kent',
        'nickname':'superman',
        'languagues': ['kriptonian','english']

}

with open('customer.json','w') as customer:
    json.dump(person_dict, customer)

with open('customer.json') as customer:
    customer_dict = json.load(customer)

print(person_dict)