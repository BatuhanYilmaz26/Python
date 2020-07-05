
# DICTIONARIES
"""A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.
A key’s value can be a number, a string, a list, or even another dictionary.
In fact, you can use any object that you can create in Python as a value in a
dictionary.
In Python, a dictionary is wrapped in braces, {}, with a series of keyvalue
pairs inside the braces,"""

alien_0 = {"color": "green", "points": "5"}
print(alien_0["color"])
print(alien_0["points"])
new_points = alien_0["points"]
print("You just earned " + str(new_points) + " points!")
"""Adding New Key-Value Pairs
Dictionaries are dynamic structures, and you can add new key-value pairs
to a dictionary at any time. For example, to add a new key-value pair, you
would give the name of the dictionary followed by the new key in square
brackets along with the new value."""
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
"""Starting with an Empty Dictionary
It’s sometimes convenient, or even necessary, to start with an empty dictionary
and then add each new item to it. To start filling an empty dictionary,
define a dictionary with an empty set of braces and then add each key-value
pair on its own line."""
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = "5"
print(alien_0)
"""Typically, you’ll use empty dictionaries when storing user-supplied data
in a dictionary or when you write code that generates a large number of
key-value pairs automatically."""
# Modifying Values in a Dictionary
print("The alien is " + alien_0["color"] + ".")
alien_0["color"] = "yellow"
print("The alien is now " + alien_0["color"] + ".")
"""For a more interesting example, let’s track the position of an alien that
can move at different speeds."""
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("Original x position: " + str(alien_0["x_position"]))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0["x_position"] = alien_0["x_position"] + x_increment
print("New x position: " + str(alien_0["x_position"]))
"""Removing Key-Value Pairs
When you no longer need a piece of information that’s stored in a dictionary,
you can use the del statement to completely remove a key-value pair.
All del needs is the name of the dictionary and the key that you want to
remove."""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0["points"]
print(alien_0)
"""A Dictionary of Similar Objects
The previous example involved storing different kinds of information about
one object, an alien in a game. You can also use a dictionary to store one
kind of information about many objects."""
favorite_languages = {
    "jenny": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("\nSarah's favorite language is " + favorite_languages["sarah"].title() + ".")

# Looping Through a Dictionary
"""Looping Through All Key-Value Pairs
Before we explore the different approaches to looping, let’s consider a
new dictionary designed to store information about a user on a website.
The following dictionary would store one person’s username, first name,
and last name"""
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
    "jenny": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name, language in favorite_languages.items():
    print(name.title() + " 's favorite language is " + language.title() + ".")

"""Looping Through All the Keys in a Dictionary
The keys() method is useful when you don’t need to work with all of the
values in a dictionary. Let’s loop through the favorite_languages dictionary
and print the names of everyone who took the poll:"""
favorite_languages = {
    "jenny": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in favorite_languages.keys():
    print(name.title())

favorite_languages = {
    "jenny": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + ".")

favorite_languages = {
    "jenny": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
if "erin" not in favorite_languages.keys():
    print("\nErin, please take our poll! \n")
# Looping Through a Dictionary’s Keys in Order
"""One way to return items in a certain order is to sort the keys as they’re
returned in the for loop. You can use the sorted() function to get a copy of
the keys in order:"""
favorite_languages = {
    "jenny": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking our poll.")

"""Looping Through All Values in a Dictionary
If you are primarily interested in the values that a dictionary contains,
you can use the values() method to return a list of values without any keys."""

favorite_languages = {
    "jenny": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
"""This approach pulls all the values from the dictionary without checking
for repeats. That might work fine with a small number of values, but in a
poll with a large number of respondents, this would result in a very repetitive
list. To see each language chosen without repetition, we can use a set.
A set is similar to a list except that each item in the set must be unique:"""

favorite_languages = {
    "jenny": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

"""Nesting
Sometimes you’ll want to store a set of dictionaries in a list or a list of
items as a value in a dictionary. This is called nesting. You can nest a set
of dictionaries inside a list, a list of items inside a dictionary, or even a
dictionary inside another dictionary."""
# A List of Dictionaries
alien_0 = {"color": "green", "points": "5"}
alien_1 = {"color": "yellow", "points": "10"}
alien_2 = {"color": "red", "points": "15"}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
"""A more realistic example would involve more than three aliens with
code that automatically generates each alien. In the following example we
use range() to create a fleet of 30 aliens:"""
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens
for alien_numbers in range(30):
    new_alien = {"color": "green", "points": "5", "speed": "slow"}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = "10"
        alien["speed"] = "medium"
    if alien["color"] == "yellow":
        alien["color"] = "red"
        alien["points"] = "15"
        alien["speed"] = "fast"
# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been created.
print("Total numbers of aliens: " + str(len(aliens)))

"""A List in a Dictionary
Rather than putting a dictionary inside a list, it’s sometimes useful to put
a list inside a dictionary."""
# Store information about a pizza being ordered.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}
# Summarize the order
print("\nYou ordered a " + pizza["crust"] + " crust pizza" + " with the following toppings: ")
for topping in pizza["toppings"]:
    print("\t" + topping.title())

"""You can nest a list inside a dictionary any time you want more than
one value to be associated with a single key in a dictionary."""
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskel"],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is: ")
    else:
        print("\n" + name.title() + "'s favorite languages are: ")
    for language in languages:
        print("\t" + language.title())

"""A Dictionary in a Dictionary
You can nest a dictionary inside another dictionary, but your code can get
complicated quickly when you do. For example, if you have several users
for a website, each with a unique username, you can use the user names as
the keys in a dictionary. You can then store information about each user by
using a dictionary as the value associated with their username."""
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# Try It Yourself Part
peoples = {
    "myıldız": {
        "first": "mustafa",
        "last": "yıldız",
        "age": "28",
        "city": "istanbul",
    },
    "ecapan": {
        "first": "emin",
        "last": "capan",
        "age": "36",
        "city": "ankara",
    },
    "bkeskin": {
        "first": "buğra",
        "last": "keskin",
        "age": "35",
        "city": "ankara",
    },
}
for people, people_info in peoples.items():
    print("\nName: " + people)
    full_name = people_info["first"] + " " + people_info["last"]
    age = people_info["age"]
    location = people_info["city"]

    print("\tFull name: " + full_name.title())
    print("\tAge: " + age)
    print("\tLocation: " + location.title())



