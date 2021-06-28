# Write a Python script that will calculate the change due, if any, for a given payment if the
# total cost is $16.48, based on the following table of coin values. If the payment is made
# with exact change, no change will be due. If the paymentis over the total amount, then
# the output will be the change due. If the paymentis under the total amount, the output
# will be how much more is needed. Your script should also provide input checking to
# ensure that only digits are being entered and are in the correct format before doing any
# calculations.
# 0 1 2 3 4 5
# 1 .35 .23 .12 .03 .01

# Input string Exxpected output of script
# Enter your payment: 20.00     change: 3 1 coins, 1 .35 coins, 1 .12 coins, 1 .03 coins, 2 .01 coins,
# Enter your payment: 16.48     No change due
# Enter your payment: 10.70     needed: 5 1 coins, 2 .35 coins, 2 .03 coins, 2 .01 coins,


def get_calculate(balance):
    money_values = [1, .35, .23, .12, .03, .01]
    for i in money_values:
        value = balance/i
        print()

        #print("{1:.0f}".format(value))

        #answer = {"coins: ", round(value, 2), money_values.index(1),"coin\n"





def main():

    total_cost = 16.48
    tender = eval(input("Enter amount: "))

    if tender > total_cost:
        balance = tender - total_cost
        print("You have an overpayment,", round(balance, 2))


        print(get_calculate(round(balance, 2)))

    else:
        if tender < total_cost:
            balance = total_cost - tender
            print("You still owe", round(balance, 2))
        else:
            if tender == total_cost:
                print("No change due, goodbye!")
            pass


main()

