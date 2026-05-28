money_owed = float(input("Enter the amount you owe?"))
apr = float(input("Enter the annual percentage rate?"))
payment = float(input("How much payment you want to make?"))
months = int(input("How many months do you want to see the results for?"))

monthly_rate = apr/100/12

for i in range(months):

    interest_paid = money_owed * monthly_rate

    money_owed = money_owed+interest_paid

    money_owed = money_owed - payment
    print('Paid', payment, 'of which', interest_paid, 'was interest', end= ' ')
    print('Now I Owe', money_owed)