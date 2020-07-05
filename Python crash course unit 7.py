"""How the input() Function Works
The input() function pauses your program and waits for the user to enter
some text. Once Python receives the user’s input, it stores it in a variable to
make it convenient for you to work with.
message = input("Tell me something and i will repeat it back to you: ")
print(message)"""
"""Writing Clear Prompts
Each time you use the input() function, you should include a clear, easy-tofollow
prompt that tells the user exactly what kind of information you’re
looking for. Any statement that tells the user what to enter should work.
name = input("Please enter your name: ")
print("Hello, " + name + "!")"""
"""Sometimes you’ll want to write a prompt that’s longer than one line.
You can store your prompt in a variable and pass that variable to the input()
function. This allows you to build your prompt over several lines, then write
a clean input() statement.
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first  name? "
name = input(prompt)
print("Hello, " + name + "!")"""

"""Using int() to Accept Numerical Input
When you use the input() function, Python interprets everything the user
enters as a string.
age = input("How old are you? ")
age = int(age)
print(age)

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou are tall enough to ride! ")
else:
    print("\nYou will be able to ride when you get little taller. ")"""

"""The Modulo Operator
A useful tool for working with numerical information is the modulo operator (%),
which divides one number by another number and returns the remainder.
The modulo operator doesn’t tell you how many times one number fits
into another; it just tells you what the remainder is.

number = input("Enter a number and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even. ")
else:
    print("\nThe number " + str(number) + " is odd. ")"""



