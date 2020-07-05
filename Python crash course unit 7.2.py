"""Introducing while Loops
The for loop takes a collection of items and executes a block of code once
for each item in the collection. In contrast, the while loop runs as long as,
or while, a certain condition is true."""
"""The while Loop in Action
You can use a while loop to count up through a series of numbers. For
example, the following while loop counts from 1 to 5:
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1"""

"""Letting the User Choose When to Quit
We can make the parrot.py program run as long as the user wants by putting
most of the program inside a while loop. We’ll define a quit value and then
keep the program running as long as the user has not entered the quit value:
prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)"""

"""Using a Flag
For a program that should run only as long as many conditions are true,
you can define one variable that determines whether or not the entire program
is active. This variable, called a flag, acts as a signal to the program. We
can write our programs so they run while the flag is set to True and stop running
when any of several events sets the value of the flag to False. As a result,
our overall while statement needs to check only one condition: whether or
not the flag is currently True. Then, all our other tests (to see if an event has
occurred that should set the flag to False) can be neatly organized in the rest
of the program.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)"""

"""Using break to Exit a Loop
To exit a while loop immediately without running any remaining code in the
loop, regardless of the results of any conditional test, use the break statement.
The break statement directs the flow of your program; you can use it to control
which lines of code are executed and which aren’t, so the program only
executes code that you want it to, when you want it to.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n Enter 'quit' when you are finished. "

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print("I'd love to go to " + city.title() + "!")"""

"""A loop that starts with while True  will run forever unless it reaches a
break statement. The loop in this program continues asking the user to enter
the names of cities they’ve been to until they enter 'quit'. When they enter
'quit', the break statement runs, causing Python to exit the loop:"""

"""Using continue in a Loop
Rather than breaking out of a loop entirely without executing the rest of its
code, you can use the continue statement to return to the beginning of the
loop based on the result of a conditional test."""

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue

    print(number)

""" TRY IT YOURSELF PART
prompt = "Enter toppings that you want in your pizza: "
prompt += "\nEnter 'quit' if you are done. "
active = True
message = ""
while active:
    message = input(prompt)
    if message == "quit":
        active = False  or use break
    else:
        print("I added " + message + " to your pizza.")"""
"""
age = input("How old are you? ")
age = int(age)
if age < 3:
    print("\nThe ticket is free for you.")
elif 3 <= age <= 12:
    print("\nThe ticket is 10$")
elif age > 12:
    print("\nThe ticket is 15$")"""

"""Using a while Loop with Lists and Dictionaries
for loop is effective for looping through a list, but you shouldn’t modify
a list inside a for loop because Python will have trouble keeping track of the
items in the list. To modify a list as you work through it, use a while loop.
Using while loops with lists and dictionaries allows you to collect, store, and
organize lots of input to examine and report on later."""
# Moving Items from One List to Another

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("The following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing All Instances of Specific Values from a List
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)

# Filling a Dictionary with User Input
"""responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Store the response in the dictionary
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input(" Would you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False
# Polling is complete. Show the results.
print("\n---Poll Results---")
for name,response in responses.items():
    print(name.title() + " would like to climb " + response.title() + ".")"""

# TRY IT YOURSELF PART
sandwich_orders = ["pastrami", "steak", "tuna", "pastrami", "chicken", "roast beef", "pastrami", "turkey", "veggie"]
finished_sandwiches = []
for sandwich in sandwich_orders:
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)
while "pastrami" in finished_sandwiches:
    finished_sandwiches.remove("pastrami")
print("Finished sandwiches are: " + ",".join(finished_sandwiches) + ".")
