# JSON is commonly used with data APIs.

import json

# Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# parse to dict
user = json.loads(userJSON)

# print(user)
# print(user['first_name'])

# dict to JSON
car = {'make': 'Nissin', 'model':'Skyline', 'year':1990}

carJSON = json.dumps(car)
print(carJSON)