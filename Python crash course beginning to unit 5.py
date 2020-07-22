print("hello world")

name = "batuhan yilmaz"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "batuhan"
last_name = "yilmaz"
full_name = first_name + " " + last_name
print(full_name)
print("Hello," + full_name.title() + "!")

message = "Hello," + full_name.title() + "!"
print(message)

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = '    Python     '
print(favorite_language)
print(favorite_language.lstrip())
print(favorite_language.strip())

age = 23
message1 = "Happy " + str(age) + "rd Birthday!"
print(message1)
# This is a comment line.
# And this is a hash mark, this line is being ignored by the Python interpreter.

spn = ["Dean", "Sam", "Bobby", "Castiel", "Jack"]
print(spn)
print(spn[2].upper())
print(spn[-1].lower())
# Item at index -1 always returns the last item in the list.
# Index positions starts at 0.
messagespn = "My favorite character is " + spn[0].upper() + ".!"
print(messagespn)

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)
# When you append an item to a list, the new element is added to the end of the list.
motorcycles.append("kawasaki")
print(motorcycles)
""" This is a multiline comment (not yet)
  now it is. """
"""You can add a new element at any position in your list by using the insert()
method. You do this by specifying the index of the new element and the
value of the new item."""
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(2, "ducati")
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
"""The pop() method removes the last item in a list, but it lets you work
with that item after removing it."""

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

""" Sometimes you won’t know the position of the value you want to remove
from a list. If you only know the value of the item you want to remove, you
can use the remove() method. """

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove("ducati")
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

guests = ["Kuzey", "Güney", "Farat", "Sami"]
print(guests)
print("Hey " + guests[0] + " I invite you to a dinner.")
pussy = "Güney"
guests.remove(pussy)
print(guests)
guests.insert(1, "Zımba")
print(guests)
guests.append("Handan")
print(guests)
print("Hey My Dear Guests " + str(guests) + " I invite you all to a dinner.")
print("Bad new I only have space for two of you")
popped_guests = guests.pop(4)
print(popped_guests + ", Sorry we dont have enough space.")
print(guests)
popped_guests = guests.pop(2)
print(popped_guests + ", Sorry oç you are not welcomed here")
print(guests)
popped_guests = guests.pop(1)
print(popped_guests + ", Sorry buddy we dont have enough space. ")
print((str(guests)) + " Dont worry you guys are still invited " + "!")
del guests[0]
print(guests)
del guests[0]
print(guests)

# sort() method changes the order of the list permanently.
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
""" You can also sort this list in reverse alphabetical order by passing the argument
 reverse=True to the sort() method."""
cars.sort(reverse=True)
# Again, the order of the list is permanently changed
print(cars)
# Sorting a List Temporarily with the sorted() Function
cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list")
print(cars)
print("\nHere is the sorted list")
print(sorted(cars))
print("\nHere is the original list again")
print(cars)
"""Notice that the list still exists in its original order at x after the sorted()
function has been used. The sorted() function can also accept a reverse=True argument 
if you want to display a list in reverse alphabetical order."""
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()
# Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list:
print(cars)
"""The reverse() method changes the order of a list permanently, but you
can revert to the original order anytime by applying reverse() to the same
list a second time."""
cars.reverse()
print(cars)

# You can quickly find the length of a list by using the len() function
cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))

holiday = ["Amsterdam", "Rome", "Paris", "London", "Barcelona"]
print(holiday)
print(sorted(holiday))
print(holiday)
holiday.reverse()
print(holiday)
holiday.reverse()
print(holiday)
holiday.sort()
print(holiday)
holiday.sort(reverse=True)
print(holiday)
print(len(holiday))

"""Write a program that creates a list containing these items
and then uses each list function"""
south_park = ["Eric", "Kyle", "Stan", "Kenny"]
print(south_park)
print(south_park[-1])
print(south_park[0])
print(south_park[1].upper())
print(south_park[2].lower())
message_sp = "My favorite character is " + south_park[3].upper() + "."
print(message_sp)

south_park = ["Eric", "Kyle", "Stan", "Kenny"]
south_park[0] = "Token"
print(south_park)
south_park.append("Clyde")
print(south_park)
south_park = ["Eric", "Kyle", "Stan", "Kenny"]
south_park.insert(3, "Butters")
print(south_park)
del south_park[3]
print(south_park)
popped_character = south_park.pop()
print(south_park)
print(popped_character)
print("OMG! They killed " + popped_character + ".\nYou Bastards.")
fav = south_park.pop(2)
print("My fav character is " + fav + ".")

south_park.remove("Eric")
print(south_park)
jew = "Kyle"
south_park.remove(jew)
print(south_park)

south_park = ["Eric", "Kyle", "Stan", "Kenny"]
south_park.sort()
print(south_park)
south_park.sort(reverse=True)
print(south_park)

# for loop
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title() + ", That was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone. That was a great magic show!\n")

metal_bands = ["metallica", "iron maiden", "slipknot"]
for bands in metal_bands:
    print(bands.title() + " is an amazing metal band.")
print("I love metal music.")

"""Making Numerical Lists
   Using the range() Function"""
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)
odd_numbers = list(range(1, 10, 2))
print(odd_numbers)
# two asterisks (**) represent exponents (üs alma işlemi)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# Kısaltılmış hali
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
"""The approach described earlier for generating the list squares consisted of
using three or four lines of code. A list comprehension allows you to generate
this same list in just one line of code. A list comprehension combines the
for loop and the creation of new elements into one line, and automatically
appends each new element."""
squares = [value ** 2 for value in range(1, 11)]
print(squares)
# Try It Yourself part
counting = [++value for value in range(1, 21)]
print(counting)
# OR
counting = [value + 1 for value in range(0, 20)]
print(counting)
print(sum(counting))
print(min(counting))
print(max(counting))

odd_nums = list(range(1, 20, 2))
print(odd_nums)

cube = []
for value in range(3, 30):
    cube.append(value ** 3)
print(cube)
# List comprehensions
cubes = [value ** 3 for value in range(3, 30)]
print(cubes)

# Working with Part of a List
# Slicing a List
players = ["charles", "martina", "michael", "florence", "eli"]
print(players)
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a List
my_foods = ["pizza", "lahmacun", "hamburger"]
friends_foods = my_foods[:]
my_foods.append("pancakes")
friends_foods.append("waffles")
print("My favorite foods are:", my_foods)
print("\nMy friend's favorite foods are: ", friends_foods)
print(my_foods[:3])
print(my_foods[1:])

# TUPLES  (tanımladığımız listedeki elemanları değiştiremeyiz.)
"""A tuple looks just like a list except you use parentheses instead of square
brackets. Once you define a tuple, you can access individual elements by
using each item’s index, just as you would for a list.
Its size doesnt change by putting the dimensions into a tuple. """

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
"""Looping Through All Values in a Tuple:
You can loop over all the values in a tuple using a for loop, just as you did with a list."""

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("\nThe original dimension")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("Modified dimension")
for dimension in dimensions:
    print(dimension)

foods = ("chicken", "beef", "meatloaf", "rice", "french fries")
print("\nHere's the menu ")
for food in foods:
    print(food)

foods = ("chicken", "beef", "meatloaf", "pancakes", "waffles")
print("\nHere's the revised menu")
for food in foods:
    print(food)

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# Checking for Inequality
ordered_meal = "hamburger"
meal = input("What did you order:")
if meal != "hamburger":
    print("Sorry we dont have that")
else:
    print(("Here's your meal " + ordered_meal.title()))

answer = 17
if answer != 42:
    print("That is not the correct answer.Please try again. ")
