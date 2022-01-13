# Get the load details
money_owed = float(input("How much do you owe?\n"))
apr = float (input("What is the percentage rate?\n"))
payment = float(input("What will the monthly payments be?\n"))
months = int(input("How many months to display results for?\n"))

# Divide APR by 100 to make %, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):
    # Add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break

    # Make payment
    money_owed = money_owed - payment

    # Print results after first month
    print("Paid", payment, "of which", interest_paid, "was interest.", end= ' ')
    print("Now I owe", money_owed)