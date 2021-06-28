# Write a Python script that uses a function to testa given input value and return whether
# it is enough to cover a purchase of $14.85. Your scriptshould take in the amount due as
# an argument and continually prompt the user to entertheir payment. The function
# should compare the payment to the cost, print whether it is over or under and by how
# much, and if it is too much it should then return the difference.
# Enter a number: 12.89
# Enter a number: 14.85
# Enter a number: 25.13
import time

total = 14.85

print("Your total:", total)

while True:
    paidThis = eval(input("Enter amount being paid (0 to quit): "))
    if paidThis > total:
        print("You paid too much! ")
        owed = paidThis - total
        print("Your balance is, {:.2f}".format(owed))
    if paidThis < total:
        print("Calculating balance...")
        time.sleep(.75)
        nowOwe = total - paidThis
        print("You still owe, {:.2f}".format(nowOwe))
    if paidThis == total:
        print("Thanks for your patronage, goodbye!")
        break
    if paidThis == 0:
        break






