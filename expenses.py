# expenses = [10.50, 8, 5, 15, 20, 5, 3]

num_expenses = int(input('Enter # of expenses:'))

expenses = []
for i in range(num_expenses):
    expenses.append(float(input('Enter a expense: ')))

total = sum(expenses)

# sum = 0

# for exp in expenses:
#     sum = sum + exp

print("You spent $", total, " on lunch this week", sep="")
