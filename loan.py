# get the loan details
money_owed = float(input("How much money do you owe, in dollars? \n"))  # 50K
apr = float(input("What is the annual percentage rage? \n"))  # 3%
payment = float(
    input("What will your montly payment be, in dollars ? \n"))  # 1K
# 24 == 2 years
months = int(input("How many months do you want to see results for? \n"))

# divide apr by 100 to make it a percent, then by 12 to get monty interes rate
montly_rate = apr/100/12

for i in range(months):
    # add in interest
    interest_paid = money_owed * montly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break

    # make payment
    money_owed = money_owed - payment

    # print
    print("Paid ", payment, "of wich", interest_paid, "was interes", end=' ')
    print("Now I owe", money_owed)
