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
'''
#checking whether a value is not in a list
banned_user = ['andrew','carolina','david']
user = 'marie'
if user not in banned_user:
    print(f"{user.title()}, you can post a response if you wish")
    '''
#if else statement
'''
cars = ["audi","bmw","subaru","toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
'''
'''
age = 17
if age >= 18:
    print("you are old enough to vote!")
    print("have you register to vote yet ?")
else:
    print("sorry, you are too young to vote.")
    print("please register to vote as soon as you turn 18!")
'''
#checking inequality
'''
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
'''

# if-elif-else statement
'''
age = 12
if age < 4:
    price = 0
elif age < 18:
    price =25
else:
    price = 40
print(f"your admission cost is ${price}.")
'''
#multiple elif block
'''
age = 45
if age < 4:
    price = 0
elif age < 18:
    price =25
elif age < 50:
    price = 40
else:
    price = 20
print(f"your admission cost is ${price}.")
'''
'''
items = ['mushrooms','extra cheese']
if 'mushroom' in items:
    print("adding mushroom.")
elif 'pepperoni' in items:
    print("adding pepperoni")
elif 'extra cheese' in items:
    print("adding extra cheese")
print("\n finished making your pizza")
'''
#if statement
'''
alien_color = 'green'
if alien_color == 'green':
    print("player just earned 5 points")
    '''
#if else statement
'''
alien_color = 'yellow'
if alien_color == 'green':
    print("player just earned 5 points")
else:
    print("player just earn 10 points")
'''
#if-elif-else
'''
alien_color = 'yellow'
if alien_color == 'green':
    print("player just earned 5 points")
elif alien_color == 'yellow':
    print("player just earn 10 points")
else:
    print("player earned 15 points")
'''
#if-elif-else
'''
age = 1
if age < 2:
    print("the person is a baby")
elif age < 4:
    print("the person is a toddler")
elif age < 13:
    print("the person is a kid")
elif age < 20:
    print("the person is a teenager")
elif age < 65:
    print("the person is adult")
else:
    print("the person is elder")
'''
'''
favorite_fruits = ['orange','kiwi','banana']
if 'mango' in favorite_fruits:
    print("you really like mango")
if 'orange' in favorite_fruits:
    print("you really like orange")
if 'kiwi' in favorite_fruits:
    print("you really like kiwi")
if 'cherry' in favorite_fruits:
    print("you really like cherry")
if 'banana' in favorite_fruits:
    print("you really like banana")
'''
'''
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
'''
'''
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry,we are out of green peppers rigth now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
'''
#using multiple lists
'''
available_toppings = ['mushrooms','olives',';green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding {requested_topping}.")
    else:
        print("sorry, we don't have {requested_topping}.")
print("\n finished making your pizza!")
'''
'''
username = ['admin','pranali','tanu','shruti']
for user in username:
    if user == 'admin':
        print("hello admin,would you like to see a status report?")
    else:
        print(f"hello {user}, thank you for logging in again")
'''

# No Users: Add an if test to hello_admin.py to make sure the list of users is 
#not empty.
#•	If the list is empty, print the message We need to find some users!
#•	Remove all of the usernames from your list, and make sure the correct 3
#message is printed.
'''
username = ['admin','pranali','tanu','shruti']
if username:
    for user in username:
        if user == 'admin':
            print("hello admin,would you like to see a status report")
        else:
            print(f"hello {user},thank you for logging in again")
else:
    print("we need to find some user!")
'''
'''
current_username = ["admin","pranali","tanu","shruti"]
new_usernames = ["admin","sarthak","abhi","PRANALI"]
for new_username in new_usernames:
    if new_username in current_username:
        print("the person will need to enter a new username")
    else:
        print(f"the {new_username} is availlable")
'''
'''
current_users = ["admin","pranali","tanu","shruti"]
new_users = ["admin","sarthak","abhi","PRANALI"]
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available!")
'''
'''
numbers = [1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num == 1:
        print("1st")
    elif num== 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")
'''
'''
for num in range(1,100,1):
     if num == 1:
        print("1st")
     elif num== 2:
        print("2nd")
     elif num == 3:
        print("3rd")
     else:
        print(f"{num}th")
'''
