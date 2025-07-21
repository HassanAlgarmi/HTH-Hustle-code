# Incorrect:
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])

# Incorrect:
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area

radius = 5
print(calculate_area(radius))


# Incorrect:
#missing two colons 
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))


# Incorrect:
# #missing colon
for i in range(5):
   print(i)

# Incorrect:
#forgot f string
def greet(name):
   return f"Hello, {name}" 
 
print(greet("Alice"))

# Incorrect:
#missing indent
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)

# Incorrect:
#n-1
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
 
print(factorial(5))

# Incorrect:
name = input("Enter your name: ")
if name == ("Alice" or "Bob"):
   print("Hello, " + name)
else:
   print("Hello, stranger!")
