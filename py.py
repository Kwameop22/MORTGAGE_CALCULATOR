import math  # Needed for powers and logs

print(" Welcome to this Mortgage calculator ")


def mortgage(c, deposit):
    #c is house price, deposit is money paid towards mortgage from one's own pocket
    return c - deposit


def total_mortgage(mt, interest):
    # mt is principal, interest is annual rate
    # Real mortgages use monthly payment * total months
    t_years = 25
    monthly_rate = (interest / 100) / 12
    total_months = t_years * 12
    # Formula for monthly payment(Amortization Formula)
    payment = mt * (monthly_rate * (1 + monthly_rate) ** total_months) / ((1 + monthly_rate) ** total_months - 1)
    #This is the Amortization formula
    return payment * total_months


def monthly_payment(tm, time):
    # tm here is the Total mortgage calculated from Choice 2
    return tm / (time * 12)


def overpayment_amount(fd, oa, tm_principal):
    #fd is monthly payment, oa is overpayment amount, tm is total mortgage
    # This calculates how many years it takes to pay off the total mortgage cost with extra money
    annual_interest_rate = i  # Uses 'i' from the global scope
    monthly_rate = (annual_interest_rate / 100) / 12
    total_monthly_pay = fd + oa

    # Logarithmic formula to find months remaining
    #I used a logarithmic formula for the overpayment section.
    # I did this because when you pay extra,you aren't just lowering the balance;
    # you are also stopping the bank from charging interest on that money in the future.
    # A simple division won't work here because the interest amount changes every month.
    # The math.log function helps the program calculate when the debt will hit zero based on the new,higher payments
    months = -math.log(1 - (monthly_rate * tm_principal) / total_monthly_pay) / math.log(1 + monthly_rate)
    return months / 12


print("""
1. Mortgage Principal
2. Total Mortgage Cost
3. Monthly Payment
4. New Payoff Time
""")


while True:
  try:
    choice = int(input("Choose: "))
    if choice == 1:
        currency = input("Enter currency(in its symbol): ")
        a = int(input(f"House price:  {currency}"))
        b = int(input(f"Deposit on house:  {currency}"))
        print(f"The mortgage is {currency}{mortgage(a, b):,.2f}")
        break

    elif choice == 2:
        currency = input("Enter currency(in its symbol): ")
        a = int(input(f"House price:  {currency}"))
        b = int(input(f"Deposit on house:  {currency}"))
        i = float(input("Interest on mortgage(%): "))
        m = a - b
        print(f"The total mortgage cost is {currency}{round(total_mortgage(m, i), 2):,.2f}")
        break

    elif choice == 3:
        currency = input("Enter currency(in its symbol): ")
        a = int(input(f"House price:  {currency}"))
        b = int(input(f"Deposit on house:  {currency}"))
        i = float(input(f"Interest on mortgage(%):   "))
        m = a - b
        t = 25
        # We calculate the real total cost first
        total_cost = total_mortgage(m, i)
        print(f"The monthly payment is {currency}{round(monthly_payment(total_cost, t), 2):,.2f}")
        break

    elif choice == 4:
        currency = input("Enter currency(in its symbol): ")
        a = int(input(f"House price:  {currency}"))
        b = int(input(f"Deposit on house:  {currency}"))
        i = float(input(f"Interest on mortgage(%):   "))
        m = a - b
        t = 25
        total_cost = total_mortgage(m, i)
        fd = monthly_payment(total_cost, t)
        oa = float(input("Overpayment amount: "))
        # Passing m (the principal) to the formula
        years_left = overpayment_amount(fd, oa, m)
        print(f"The new payoff time is {round(years_left, 1)} years")
        break
    else:
        print(f"{choice} is not a valid option") # Prevents user from entering a choice which is not 1-4


  except ValueError: #Enables user to enter variables(words,symbols) as choice without the code breaking
      print("Invalid input.")

