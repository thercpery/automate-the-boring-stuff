# A list is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Bananas', 'Mangoes']

# Use a constructor
# numbers2 = list((1,2,3,4,5))

# print(numbers)
# print(numbers2)

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Grapes')

# Remove to list
fruits.remove('Mangoes')

# Insert into position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Cherries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)