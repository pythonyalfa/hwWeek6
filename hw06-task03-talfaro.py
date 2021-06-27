# Task 03
# Write a Python script that will take in two separate lists and return all of the possible
# combinations of the elements in those lists.
# Enter first list: blue, green
# Enter second list: beans, bird

import random
import array as firsList
import array as secondList

def makeitRandom(randomAnimal):

    for i in randomAnimal:
        print(random.choice(randomAnimal),"",random.choice(randomAnimal))


   # return randomized


def main():
    firstList = ['lion','tiger','cow','hippo','rooster']
    secondList = ['homework','is','hard','labs','too','can','do','attitude']
    both_lists = firstList + secondList
    #print(random.choice(both_lists),"",random.choice(both_lists))
    makeitRandom(both_lists)
main()