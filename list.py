'''
freinds = ["pranali","tanuja","shruti","sarthak","abhi","akshada","shivam","prasad"]
print(freinds)
#Accessing Element
print(freinds[0])
print(freinds[3])
print(freinds[-2])
print(freinds[0].title()) #same output only first letter capitallize
'''

#using individual value from a list
'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
'''

#modifying element
'''
bicycles = ['trek', 'cannondale', 'redline']
print(bicycles)
bicycles[0] ="specialized"
print(bicycles)

#adding element
bicycles.append('specialized')
print(bicycles)
'''

#inserting element
'''
freinds = ["pranali","tanuja","shruti","sarthak","abhi","akshada","shivam"]
freinds.insert(5,'prasad')
print(freinds)
'''

#removing element
'''
#using delete
bicycles = ['trek', 'cannondale', 'redline','specialized']
del bicycles[0]
print(bicycles)
#using remove
bicycles.remove('redline')
print(bicycles)


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is too expensive for me.")
'''

#sorting a list
'''
freinds = ["pranali","tanuja","shruti","sarthak","abhi","akshada","shivam","prasad"]
freinds.sort()
print(freinds)

#reverse sort list
freinds.sort(reverse=True)
print(freinds)

#finding length
len(freinds)
print(freinds)
'''

#looping through an entire list
'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
for cars in cars:
    print(cars)
    print(f"{cars.title()},that was a great car")
    print(f"A {cars.title()} is too expensive for me.\n")
'''

# find range
'''
for value in range(1,5):
    print(value)

#using range() to make a list of number
numbers = list(range(1,6))
print(numbers)

#list of square of numbers
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)
'''
'''
#Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for value in range(1,20):
    print(value)
'''

'''
numbers = list(range(1,20))
print("min num:" ,min(numbers))
print("max num:", max(numbers))
print("sum num:", sum(numbers))
'''

#mathematical func odd,even
'''
#Odd Numbers
odd_numbers = list(range(1, 21, 2))  
for num in odd_numbers:
    print(num)

#even numbers
even_numbers = list(range(2, 21, 2))  
for num in even_numbers:
    print(num)
'''

#multiple threes
'''
numbers =[]
for value in range(1,11):
    multiple = value*3
    numbers.append(multiple)
print(numbers)
'''

#cube comprehension
'''
numbers =[]
for value in range(1,11):
    multiple = value**3
    numbers.append(multiple)
print(numbers)
'''

#part of list
#slicing a list
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[2:])
print(players[-3:])
'''
#looping through a slice
'''
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("here are the first three players on my team:")
for players in players[0:3]:
    print(players.title())
'''

#copying a list
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
'''
'''
cubes = [n**3 for n in range(1, 11)]
print("The first three items in the list are:")
print(cubes[:3])     # First 3 items

print("\nThree items from the middle of the list are:")
print(cubes[3:6])    # Middle 3 items

print("\nThe last three items in the list are:")
print(cubes[-3:])    # Last 3 items
'''
'''
# Make a copy of the list of pizzas, and call it friend_pizzas. 
Then, do the following:
•	Add a new pizza to the original list.
•	Add a different pizza to the list friend_pizzas.
•	Prove that you have two separate lists. Print the message My favorite 
pizzas are:, and then use a for loop to print the first list. Print the message 
My friend’s favorite pizzas are:, and then use a for loop to print the sec
ond list. Make sure each new pizza is stored in the appropriate list.


pizzas = ["Margherita", "Pepperoni", "Cheese Burst"]
friend_pizzas = pizzas[:]
pizzas.append("BBQ Chicken")
friend_pizzas.append("Veggie Supreme")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
'''