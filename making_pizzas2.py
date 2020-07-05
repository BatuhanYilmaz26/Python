from pizza import make_pizza as mp
mp(16, "pepperoni")
mp(12, "mushroom", "pineapple")
"""With this syntax, you don’t need to use the dot notation when you call a
function. Because we’ve explicitly imported the function make_pizza() in the
import statement, we can call it by name when we use the function."""