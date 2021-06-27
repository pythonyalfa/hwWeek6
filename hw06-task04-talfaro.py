# Write a Python script that uses list comprehension to greet each animal in the list.
# Input Strng : dog, cat, bear, fossa, tapir
import time

input_string = ['dog', 'cat', 'bear', 'fossa', 'tapir']

comprehend = list(input_string)

for i in comprehend:
    print("Hello ",i.capitalize())
    time.sleep(.70)
print("Goodbye!")