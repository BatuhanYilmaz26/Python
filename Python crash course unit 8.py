"""Functions
If you need to perform that task multiple times throughout your program, you don’t
need to type all the code for the same task again and again; you just call
the function dedicated to handling that task, and the call tells Python to
run the code inside the function."""
# Defining a Function
# Here’s a simple function named greet_user() that prints a greeting:


def greet_user(username):
    print("Hello, " + username.title() + "!")


greet_user("jesse")


def display_message():
    print("I am learning Python.")


display_message()


"""Passing Arguments
Because a function definition can have multiple parameters, a function call
may need multiple arguments. You can pass arguments to your functions
in a number of ways. You can use positional arguments, which need to be in
136 Chapter 8
the same order the parameters were written; keyword arguments, where each
argument consists of a variable name and a value; and lists and dictionaries
of values."""
"""Positional Arguments
When you call a function, Python must match each argument in the function
call with a parameter in the function definition. The simplest way to
do this is based on the order of the arguments provided. Values matched
up this way are called positional arguments."""""


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("hamster", "harry")
describe_pet("dog", "willie")
"""Multiple Function Calls
You can call a function as many times as needed. Describing a second, different
pet requires just one more call to describe_pet():"""
describe_pet(animal_type="hamster", pet_name="harry")


def describe_city(cit_name, country_name="Turkey"):

    print(cit_name.title() + " is in " + country_name.title() + ".")


describe_city("ankara")
describe_city("eskişehir", "turkey")
describe_city("milan", "Italy")
"""Return Values
A function doesn’t always have to display its output directly. Instead, it can
process some data and then return a value or set of values. The value the
function returns is called a return value. The return statement takes a value
from inside a function and sends it back to the line that called the function."""


def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)
"""When you call a function that returns a value, you need to provide a
variable where the return value can be stored. In this case, the returned
value is stored in the variable musician"""

"""Making an Argument Optional
Sometimes it makes sense to make an argument optional so that people
using the function can choose to provide extra information only if they  want to."""
"""To make the middle name optional, we can give the middle_name argument
an empty default value and ignore the argument unless the user provides a
value. To make get_formatted_name() work without a middle name, we set the
default value of middle_name to an empty string and move it to the end of the
list of parameters"""


def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)
singer = get_formatted_name("john", "hooker", "lee")
print(singer)

"""Returning a Dictionary
A function can return any kind of value you need it to, including more complicated
data structures like lists and dictionaries."""


def build_person(first_name, last_name, age=""):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix", age=27)
print(musician)

"""Using a Function with a while Loop
You can use functions with all the Python structures you’ve learned about
so far."""

"""
def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


# This is an infinite loop
while True:
    print("Please tell me your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello " + formatted_name + "!")
    """


"""def get_formatted_name(first_name, last_name):
    full_name = first_name + last_name
    return full_name.title()


while True:
    print("Please tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello " + formatted_name + "!")
"""


def get_location(city_name, country_name):
    location = {"city": city_name, "country": country_name}
    return location


loc = get_location("eskişehir", "turkey")
print(loc)

"""
def get_location(city_name, country_name):
    location = city_name.title() + ", " + country_name.title()
    return location


while True:
    print("Please tell me where you live: ")
    print("(enter 'q' at any time to quit)")
    ci_name = input("City name: ")
    if ci_name == "q":
        break
    co_name = input("Country name: ")
    if co_name == "q":
        break
    location = get_location(ci_name, co_name)
    print("So you are living in " + location)"""


def make_album(artist, album, tracks=""):
    album = {"Artist": artist, "Album": album}
    if tracks:
        album["Tracks"] = tracks
    return album


info = make_album("Metallica", "Ride the Lightning", "8")
print(info)
fav = make_album("Slipknot", "We Are Not Your Kind", "14")
print(fav)
rap = make_album("Ceza", "Rapstar")
print(rap)


# Passing a List
def greet_user(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ["a", "b", "c"]
greet_user(usernames)


# Modifying a List in a Function
"""Consider a company that creates 3D printed models of designs that
users submit. Designs that need to be printed are stored in a list, and after
being printed they’re moved to a separate list. The following code does this
without using functions:"""
unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_desing = unprinted_designs.pop()
    print("Printing model: " + current_desing)
    completed_models.append(current_desing)
# Display all completed models.
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

# We can reorganize this code by writing two functions, each of which does one specific job.


def print_models(unprinted_designs, completed_models):
    """" Simulate printing each design, until none are left. Move each design to completed_models after printing."""
    while unprinted_designs:
        current_desing = unprinted_designs.pop()
        print("Printing model: " + current_desing)
        completed_models.append(current_desing)


def show_completed_models(completed_models):
    print("The following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Passing an Arbitrary Number of Arguments
""" The asterisk in the parameter name *toppings tells Python to make an
empty tuple called toppings and pack whatever values it receives into this
tuple."""


def make_pizza(*toppings):
    print("\nMaking pizza with the following topings: ")
    for topping in toppings:
        print("- " + topping.title())


make_pizza("pepperoni")
make_pizza("pepperoni", "green peppers", "extra cheese")
# This syntax works no matter how many arguments the function receives.
"""If you want a function to accept several different kinds of arguments, the
parameter that accepts an arbitrary number of arguments must be placed
last in the function definition. Python matches positional and keyword
arguments first and then collects any remaining arguments in the final
parameter."""


def make_pizza(size, *toppings):
    print("\nMaking a " + size + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping.title())


make_pizza("16", "mushroom")
make_pizza("24", "pepperoni", "extra cheese", "green peppers")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile("albert", "einstein",
                             location="princeton",
                             field="physics")
print(user_profile)
"""The definition of build_profile() expects a first and last name, and
then it allows the user to pass in as many name-value pairs as they want. The
double asterisks before the parameter **user_info cause Python to create
an empty dictionary called user_info and pack whatever name-value pairs it
receives into this dictionary. Within the function, you can access the name-value
pairs in user_info just as you would for any dictionary."""


"""Storing Your Functions in Modules
You can go a step further by
storing your functions in a separate file called a module and then importing
that module into your main program. An import statement tells Python to
make the code in a module available in the currently running program file."""
"""Importing an Entire Module
To start importing functions, we first need to create a module. A module
is a file ending in .py that contains the code you want to import into your program."""

"""Importing Specific Functions
You can also import a specific function from a module. Here’s the general
syntax for this approach:
from module_name import function_name """

"""Importing All Functions in a Module
You can tell Python to import every function in a module by using the asterisk (*) operator:"""
"""from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')"""
