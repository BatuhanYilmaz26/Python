# Checking Whether a Value Is Not in a List
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(user.title()+" you can post a response if you wish.")
# first example
age = 19
if age >= 18:
    print("You are old enough to vote.")
    print("Have you registered to vote yet? ")
else:
    print("Sorry, you are too young to vote.")
# second example
age = 52
if age <= 4:
    print("Your admission cost is 0$. ")
elif age <= 18:
    print("Your admission cost is 5$. ")
elif age <= 65:
    print("Your admission cost is 10$. ")
else:
    print("Your admission cost is 7$. ")

# Better solution for second example
age = 15
if age <= 4:
    price = 0
elif age <= 18:
    price = 5
elif age <= 65:
    price = 10
else:
    price = 7
print("Your admission cost is " + str(price) + "$.")

"""Omitting the else Block
Python does not require an else block at the end of an if-elif chain. Sometimes
an else block is useful; sometimes it is clearer to use an additional
elif statement that catches the specific condition of interest:"""
age = 65
if age <= 4:
    price = 0
elif age <= 18:
    price = 5
elif age <= 65:
    price = 10
elif age > 65:
    price = 7
print("Your admission cost is " + str(price) + "$.")

requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("\n Finished making your pizza!")
"""The if statement checks to see whether the person requested mushrooms
on their pizza. If so, a message is printed confirming that topping. The
test for pepperoni is another simple if statement, not an elif or else
statement, so this test is run regardless of whether the previous test passed
or not."""

alien_color = ["green", "red", "yellow"]
if "green" in alien_color:
    print("\nYou earned 5 points.")
if "blue" not in alien_color:
    print("You earned 10 points.")

alien_color = ["green", "red", "yellow"]
chosen_color = "red"
if chosen_color == "green":
    print("\nYou earned 5 points.")
elif chosen_color == "yellow":
    print("\nYou earned 10 points.")
else:
    print("\nYou earned 15 points.")

"""question = input("How old are you ? :")
age = int(question)
if 0 < age < 2:
    print("Person is  a baby.")
elif 2 <= age < 4:
    print("Person is a a toddler.")
elif 4 <= age < 13:
    print("Person is a kid.")
elif 13 <= age < 20:
    print("Person is a teenager.")
elif 20 <= age < 65:
    print("Person is an adult.")
elif age >= 65:
    print("Person is an elder.")
else:
    print("Negative numbers are not allowed.")
    """
# Checking for Special Items
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    print("Added " + requested_topping + ".")
print("\nFinished making your pizza!\n")

"""But what if the pizzeria runs out of green peppers? An if statement
inside the for loop can handle this situation appropriately:"""
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("Finished making your pizza!\n")

# Checking That a List Is Not Empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping)
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n")

# Using Multiple Lists
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni",
                      "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("Finished making your pizza!\n ")

# Try It Yourself part
username = ["admin", "bill", "jack", "john", "mark"]
for name in username:
    # OR if name == "admin":
    if name == username[0]:
        print("Hello " + name.title() + " would you like to see a status report?")
    else:
        print("Hello " + name.title() + " thank you for logging in again.")

"""Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3."""

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
for number in numbers:
    if number == "1":
        print(number + "st")
    elif number == "2":
        print(number + "nd")
    elif number == "3":
        print(number + "rd")
    else:
        print(number + "th")








