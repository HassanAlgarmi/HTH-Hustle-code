
# Task 1: Working with Strings
food = 'buldak carbonara'
print(food [:3]) #Print first 3 characters print(food[-3:]) #Print last 3 characters first_last
first_last = food [0] + food[-1] #combine first and last character
#print(first_last)
food_list = food.split
#print(food_list)
joined_food = ' '.join(food_list)
#print(joined_food)

# Task 2: Working with Lists
number_list = [1, 7675647456, 32, -5, 0, 234]
number_list. append (67)
#print(number_list)
number_list. insert(3, 1000) #print(number_list) number_list. pop(l #print (number_list)
number_list. remove(number_list[1])

# Task 3: Working with Dictionaries
books = {
    'Dr. Seuss': 'Cat in the Hat',
    'JK Rowling': 'Harry Potter',
    'George Orwell': '1984',
    'Harper Lee': 'To Kill a Mockingbird'
}

# Print list of all keys
print(books.keys())
# Print list of all thingx
print(books.values())
# Get a value for a specific key
print(books.get('JK Rowling'))
# Remove the 3rd keyalue pair
books.pop('George Orwell')
print(books)
# Remove the 1st key-value pair
del books['Dr. Seuss']
print(books)
