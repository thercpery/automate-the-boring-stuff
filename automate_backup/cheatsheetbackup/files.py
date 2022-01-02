# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myFile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is closed: ', myFile.closed)
print('Opening mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write('. I also like PHP.')
myFile.close()

# Read a file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)