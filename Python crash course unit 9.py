"""Classes"""
"""Object-oriented programming is one of the
most effective approaches to writing software.
In object-oriented programming you
write classes that represent real-world things
and situations, and you create objects based on these
classes. When you write a class, you define the general
behavior that a whole category of objects can have."""


class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


"""The __init__() Method
A function that’s part of a class is a method. Everything you learned about
functions applies to methods as well; the only practical difference for now is
the way we’ll call methods.
We define the __init__() method to have three parameters: self, name,
and age. The self parameter is required in the method definition, and it
must come first before the other parameters. It must be included in the definition
because when Python calls this __init__() method later (to create an
instance of Dog), the method call will automatically pass the self argument.
Every method call associated with a class automatically passes self, which
is a reference to the instance itself; it gives the individual instance access to
the attributes and methods in the class.
When we make an instance of Dog,
Python will call the __init__() method from the Dog class. We’ll pass Dog()
a name and an age as arguments; self is passed automatically, so we don’t
need to pass it. Whenever we want to make an instance from the Dog class,
we’ll provide values for only the last two parameters, name and age."""
my_dog = Dog("willie", 6)
print("My dogs name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
"""The __init__() method has no explicit return
statement, but Python automatically returns an instance representing this
dog. We store that instance in the variable my_dog. The naming convention is
helpful here: we can usually assume that a capitalized name like Dog refers
to a class, and a lowercase name like my_dog refers to a single instance created
from a class."""
my_dog.sit()
my_dog.roll_over()


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurants name is " + self.restaurant_name.title() + ".")
        print("This restaurant cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant called " + self.restaurant_name + " is open right now.")
        print("Enjoy your dinner")


my_restaurant = Restaurant("Arbys", "BBQ")
print("My fav place's name is " + my_restaurant.restaurant_name.title() + ".")
print("My fav place's cuisine type is " + my_restaurant.cuisine_type + ".")
my_restaurant.open_restaurant()
second_restaurant = Restaurant("Five Guys", "Homemade")
second_restaurant.describe_restaurant()
third_restaurant = Restaurant("Adanus", "Ocakbaşı")
third_restaurant.describe_restaurant()
third_restaurant.open_restaurant()


class User:
    def __init__(self, first_name, last_name, age, weight, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.height = height

    def describe_user(self):

        print("User's name is " + self.first_name + " " + self.last_name + ".")
        print("User's age is " + self.age + ".")
        print("User's weight is " + self.weight + ".")
        print("User's height is " + self.height + ".")

    def greet_user(self):
        print("Hello, " + self.first_name + " " + self.last_name + ".")


user1 = User("Batuhan", "Yılmaz", "21", "73", "173")
user1.describe_user()
user1.greet_user()
"""Setting a Default Value for an Attribute
Every attribute in a class needs an initial value, even if that value is 0 or an
empty string. In some cases, such as when setting a default value, it makes
sense to specify this initial value in the body of the __init__() method; if
you do this for an attribute, you don’t have to include a parameter for that
attribute."""
"""Let’s add an attribute called odometer_reading that always starts with a value of 0.
 We’ll also add a method read_odometer() that helps us read each car’s odometer:"""


class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
"""Not many cars are sold with exactly 0 miles on the odometer, so we 
need a way to change the value of this attribute."""
"""Modifying Attribute Values
You can change an attribute’s value in three ways: you can change the value directly through an instance,
 set the value through a method, or increment the value (add a certain amount to it) through a method."""
"""Modifying an Attribute’s Value Directly
The simplest way to modify the value of an attribute is to access the attribute directly through an instance."""
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


