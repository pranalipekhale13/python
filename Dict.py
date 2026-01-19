'''
alien_0 = {'color': 'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
'''
#accesing value in a Dictionary
'''
alien_0 = {'color':'green', 'points': 5}
new_points = alien_0['points']
print(f"you just earned {new_points} points!")
'''
#Adding New Key-Value pair
'''
alien_0 = {
    'color' : 'greeen',
    'points' : 5
}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

'''
#starting with an empty dictionary
'''
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
'''
#Modifying Values in a Dictionary
'''
alien_0 = {'color': 'green'}
print(f"the alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"the alien is now {alien_0['color']}.")
'''
'''
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
3rif alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
'''
#removing key-value pair
'''
alien_0 = {
    'color' :'green',
    'points': 5
}
print(alien_0);
del alien_0['points']
print(alien_0)
'''
'''
favorite_language = {
    'pranali': 'python',
    'tanu' : 'java',
    'shruti' : 'c++',
    'sarthak' : 'ruby',
    'abhi': 'c'
}
language = favorite_language['shruti'].title()
print(f"shruti favorite language is {language}.")
'''
'''
person = {
    'first_name':'pranali',
    'last_name': 'pekhale',
    'age': 20,
    'city':'Nashik'
    }
print(person)
'''
'''
glossary = {
    "variable": "A name that stores a value.",
    "function": "A block of code that performs a specific task.",
    "list": "A collection of items stored in a specific order.",
    "loop": "Used to repeat a block of code multiple times.",
    "dictionary": "A collection of key-value pairs."
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n    {meaning}\n")
'''
#looping through a dictionary
'''
user ={
    'username':'pekhale123',
    'first':'pranali',
    'last':'pekhale'
}
for key ,value in user.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")
'''
'''
favorite_language = {
    'pranali': 'python',
    'tanu' : 'java',
    'shruti' : 'c++',
    'sarthak' : 'ruby',
    'abhi': 'c'
}
for name,language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
'''
'''
favorite_language = {
    'pranali': 'python',
    'tanu' : 'java',
    'shruti' : 'c++',
    'sarthak' : 'ruby',
    'abhi': 'c'
}
for name in favorite_language.keys():
    print(name.title())
'''
'''
favorite_language = {
    'pranali': 'python',
    'tanu' : 'java',
    'shruti' : 'c++',
    'sarthak' : 'ruby',
    'abhi': 'c'
}
friends = ['pranali','shruti']
for name in favorite_language.keys():
    print(name.title())
    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()},I see you love {language}!")
'''
#looping through all keys in a dictionary
'''
favorite_language = {
    'pranali': 'python',
    'tanu' : 'java',
    'shruti' : 'c++',
    'sarthak' : 'ruby',
    'abhi': 'c'
}
for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
'''
#looping through all values in a dictionary
'''
favorite_language = {
    'pranali': 'python',
    'tanu' : 'java',
    'shruti' : 'c++',
    'sarthak' : 'python',
    'abhi': 'c'
}
for language in favorite_language.values():
    print(language.title())
'''
#set is a collection in which each item must be unique:
'''
favorite_language = {
    'pranali': 'python',
    'tanu' : 'java',
    'shruti' : 'c++',
    'sarthak' : 'python',
    'abhi': 'c'
}
print("the following languages have been mentioned:")
for language in set (favorite_language.values()):
    print(language.title())
'''
'''
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

# List of people who should take the poll
people_to_poll = ["jen", "edward", "michael", "pranali", "sarah"]

# Loop through the list
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, please take the favorite languages poll.")
'''
'''
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "ganges": "india"
}

# Sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()  # blank line

# Print the name of each river
print("Rivers:")
for river in rivers.keys():
    print(river.title())

print()  # blank line

# Print the name of each country
print("Countries:")
for country in rivers.values():
    print(country.title())
'''
#Nesting
'''
alien_0 = {'color':'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_3 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_3]
for alien in aliens:
    print(alien)
'''
'''
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
'''
'''
favorite_language = {
    'pranali': ['python','c++','java'],
    'tanu' : ['java','python'],
    'shruti' :[ 'c++','java'],
    'sarthak' : ['python','ruby'],
    'abhi': ['c']
}
for name ,languages in favorite_language.items():
    print(f"\n {name.title()}'s favorite language are:")
    for language in languages:
        print(f"\t{language.title()}")
'''
'''
favorite_places = {
    "pranali": ["goa", "lonavala", "mahabaleshwar"],
    "rahul": ["ladakh", "manali"],
    "tanuja": ["mumbai", "pune", "nashik"]
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")

    for place in places:
        print(f" - {place.title()}")
'''
'''
favorite_numbers = {
    "pranali": [7, 21, 3],
    "rahul": [10, 14],
    "tanuja": [5, 9, 11],
    "sneha": [2],
    "abhishek": [4, 8, 12]
}

for person, numbers in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are:")

    for number in numbers:
        print(f" - {number}")
'''
'''
cities = {
    "mumbai": {
        "country": "india",
        "population": "20 million",
        "fact": "It is known as the financial capital of India."
    },
    "paris": {
        "country": "france",
        "population": "2.1 million",
        "fact": "It is famous for the Eiffel Tower."
    },
    "tokyo": {
        "country": "japan",
        "population": "37 million",
        "fact": "It is one of the most populated cities in the world."
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f" Country: {info['country'].title()}")
    print(f" Population: {info['population']}")
    print(f" Fact: {info['fact']}")
'''
'''
person1 = {
    "first_name": "pranali",
    "last_name": "pekhale",
    "age": 20,
    "city": "pune"
}

person2 = {
    "first_name": "rahul",
    "last_name": "sharma",
    "age": 25,
    "city": "mumbai"
}

person3 = {
    "first_name": "tanuja",
    "last_name": "patil",
    "age": 22,
    "city": "nashik"
}

people = [person1, person2, person3]

for person in people:
    print("\nPerson Information:")
    for key, value in person.items():
        print(f" {key.replace('_', ' ').title()}: {value}")
'''
pet1 = {
    "animal": "dog",
    "owner": "pranali"
}

pet2 = {
    "animal": "cat",
    "owner": "rahul"
}

pet3 = {
    "animal": "parrot",
    "owner": "tanuja"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("\nPet Information:")
    for key, value in pet.items():
        print(f" {key.title()}: {value.title()}")
