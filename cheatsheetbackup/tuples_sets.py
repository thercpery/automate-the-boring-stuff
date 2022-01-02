# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Bananas', 'Mangoes')
# fruits2 = tuple(('Apples', 'Oranges', 'Bananas', 'Mangoes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
# print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
# print(len(fruits))

# print(fruits)
# print(fruits2)

# print(fruits2, type(fruits2))

# A set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mangoes', 'Grapes'}

print(fruits_set)

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Bananas')

# Remove from set
fruits_set.remove('Grapes')

# Add duplicate
fruits_set.add('Apples')

# Clear set
fruits_set.clear()

# Delete set
# del fruits_set

print(fruits_set)