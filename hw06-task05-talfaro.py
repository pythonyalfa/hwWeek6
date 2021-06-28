# Write a Python script that uses list comprehension and sequence operators to greet
# only the animals in the list based on the following list of animals:
# animals = ['dog', 'cat', 'bear', 'fossa', 'tapir']
# Additionally, you are welcome to add any animals you like to the list.

animals = ['dog', 'cat', 'bear', 'fossa', 'tapir']

fruits = ["elephant", "alienANimal", "dodo", "kiwi", "zebra"]
combinedList = animals + fruits


newlist = [x for x in combinedList if "a" in x]
for i in newlist:
    print("Hello,", i.capitalize(),"!")




