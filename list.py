'''
freinds = ["pranali","tanuja","shruti","sarthak","abhi","akshada","shivam","prasad"]
print(freinds)
#Accessing Element
print(freinds[0])
print(freinds[3])
print(freinds[-2])
print(freinds[0].title()) #same output only first letter capitallize
'''
'''
#using individual value from a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
'''
'''
#modifying element
bicycles = ['trek', 'cannondale', 'redline']
print(bicycles)
bicycles[0] ="specialized"
print(bicycles)

#adding element
bicycles.append('specialized')
print(bicycles)
'''
'''
#inserting element
freinds = ["pranali","tanuja","shruti","sarthak","abhi","akshada","shivam"]
freinds.insert(5,'prasad')
print(freinds)
'''
'''
#removing element
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
'''
#sorting a list
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
'''
#looping through an entire list
cars = ['bmw', 'audi', 'toyota', 'subaru']
for cars in cars:
    print(cars)
    print(f"{cars.title()},that was a great car")
    print(f"A {cars.title()} is too expensive for me.\n")
'''
'''
# find range
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
'''
#multiple threes
numbers =[]
for value in range(1,11):
    multiple = value*3
    numbers.append(multiple)
print(numbers)
'''
'''
#cube comprehension
numbers =[]
for value in range(1,11):
    multiple = value**3
    numbers.append(multiple)
print(numbers)
'''
