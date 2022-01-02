# A dictionary is a collection which is unordered, changeable, and indexed. No duplicate members

# Create a dictionary
person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 30
}

# Constructor
# person2 = dict(first_name='Sarah', last_name='Williams')

# Get value
print(person['first_name'])

# Get method
print(person.get('last_name'))

# Add key/value
person['phone'] = '1-800-555-6666'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Get dict items
print(person.values())

# Copy dictionary
person2 = person.copy()
person2['city'] = 'Houston'

print(person2)

# Remove item
del person['age']

# Remove thru pop
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dictionaries
people = [
    {'name': 'Martha', 'age':30},
    {'name': 'Kevin', 'age':27}
]

print(people)

# Get value of list dictionaries
print(people[1]['name'])

print(person, type(person))
# print(person2, type(person2))