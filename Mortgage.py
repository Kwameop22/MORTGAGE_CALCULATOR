# Actually this is the first Mortgage Calculator I made.
# I made a 2nd Mortgage calculator because I used Simple interest for the whole mortgage process instead of compound interest
# This makes the whole project unaccurate / unreliable or wrong

print("Welcome to this Mortgage calculator")

def mortgage(c, deposit):
# c is house price, deposit is th
    return c - deposit


# noinspection PyTypeChecker
def total_mortgage(mt: object, interest: object) -> object:
# mt is mortgage, interest is annual value 
    return mt +((mt * interest) / 100)

def fixed_deposit(tm, time):
#tm is total mortgage(with interest), time is period to pay(usually 25 years)
    return (tm / time)/12

def overpayment_amount(fd,oa,tm):
#fd is monthly payment,oa is overpayment, total mortgage
# Overpayment is the extra money paid in addition to the monthly payment
# the reason is to reduce the number of years and the interest it takes to pay off the mortgage
    return tm/((fd+oa)*12)

print("1. Mortgage(Without interest)")
print("2. Mortgage(With Interest)")
print("3. Fixed deposit")
print("4. Years after overpayment")

choice = int(input("Choose: "))

while True:
    if choice == 1:
        currency = input("Enter currency(in its symbol): ")
        a = int(input(f"House price:  {currency}"))
        b = int(input(f"Deposit on house:  {currency}"))
        print(f"The mortgage is {currency}{mortgage(a, b)}")
        break

    elif choice == 2:
        currency = input("Enter currency(in its symbol): ")
        a = int(input(f"House price:  {currency}"))
        b = int(input(f"Deposit on house:  {currency}"))
        i = float(input("Interest on mortgage: "))
        m = a - b
        print(f"The total mortgage is {currency}{total_mortgage(m,i)}")
        break

    elif choice == 3:
        currency = input("Enter currency(in its symbol): ")
        a = int(input(f"House price:  {currency}"))
        b = int(input(f"Deposit on house:  {currency}"))
        i = float(input(f"Interest on mortgage:   "))
        m = a - b
        t = 25
        s =  m +((m * i)/100)
        print(f"The fixed deposit per month is {currency}{round(fixed_deposit(s,t))}")
        break

    elif choice == 4:
        currency = input("Enter currency(in its symbol): ")
        a = int(input(f"House price:  {currency}"))
        b = int(input(f"Deposit on house:  {currency}"))
        i = float(input(f"Interest on mortgage:   "))
        m = a - b
        t = 25
        tm = m + ((m * i) / 100)
        fd = (tm / t)/12
        oa = float(input("Overpayment amount: "))
        print(f"The years left using overpayment is {round(overpayment_amount(fd,oa,tm))} 4"
              f"years")









