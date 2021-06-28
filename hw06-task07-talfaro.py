# Write a Python script that uses a function to return the amount of change made from a
# given value based on the following table of coin values:
# 0   1   2   3   4   5
#-----------------------|
# 1 .35 .23 .12 .03 .01
# The function should take in the change due as an argumentand return a dictionary of
# the coin values.
# Input Strng: Enter Value: 9.76
# Expected Ouptput: {'1 coin': 9, '.35 coin': 2, '.23 coin': 0, '.12 coin': 0, '.03 coin': 2, '.01 coin': 0}


#def calculate_coin(total):

import math

def coin_changedollar(cents):
    dollar = cents / 1.0
    return dollar

def coin_changethirtyfive(cents):
    thirtyfive = cents / .35
    return thirtyfive

def coin_changetwentythree(cents):
    twenty_three = cents / .23
    return twenty_three

def coin_changetwelve(cents):
    twelve = cents / .12
    return  twelve
def coin_changethree(cents):
    three = cents / .03
    return three

def coin_changepennies(cents):
    penni = cents / .01
    return penni


def main():

    cents= float(input("Enter value: "))

    print("The numbers of coins for",cents, " value are: ")
    dollars = coin_changedollar(cents)
    print("Dollars: ", math.floor(dollars))

    cents = cents - math.floor(dollars)

    thirtyfive = coin_changethirtyfive(cents)
    print(".35: ", round(thirtyfive))
    print("This is what is left over after removing the 9 and the 35 cents", cents)
    cents = (cents - round(thirtyfive)*.35)
    print("Now we have: ", round(cents,2))


    twenty_three = coin_changetwentythree(round(cents,2))
    print(".23: ",round(twenty_three))
    cents = (cents - round(twenty_three))


    twelve = coin_changetwelve(round(cents,2))
    print(".12",round(twelve))

    three = coin_changethree(round(cents,2))
    print(".03:",three)

    cents = (three*.03) - cents
    print("We now have", round(cents))

    penni = coin_changepennies(round(cents))
    print(".01",round(penni))

    dict1 = {"1 coin":math.floor(dollars),'.35 coin':round(thirtyfive),'.23 coin':round(twenty_three),'.12 coin':round(twelve),'.03':round(three),'.01':round(penni)}
    print(dict1)


main()

