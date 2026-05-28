
# expenses = [100, 200, 400, 60, 75, 900]
# sum = 0

# for x in expenses:
#     sum = sum + x

# print('You Spent $', sum, sep = '')

# we can do with the help of function sum().

expenses = [100, 200, 400, 60, 75, 900]

total = sum(expenses)
print('You spent $', total, sep = '')