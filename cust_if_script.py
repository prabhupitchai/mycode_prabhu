#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

message = 'Truth Hurts Mate... '

# wrap connection in a float() to accept decimals as numbers
age = float(input("What is your age is..yes real age. Not the age you say in the party:  "))

# if input value was higher or equal to 25
if age >= 50:
    message = message + '-----You are the Indiana Jones Generation.'
elif age >= 40:
    message = message + '--- You are still young &  Hobbit and Lord of Rings Generation.'
elif age >= 30:
    message = message + '... Young Kid..you belong to Chronicales of Narnia Generation.'
else:
    message = message + 'mmm.. Babies.. you are yet to enter the worforce..Harry Potter Generation.'
print(message)
