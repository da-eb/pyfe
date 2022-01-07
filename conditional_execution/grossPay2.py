# this program computes the gross pay and gives 1.5 extra bonus for 40+ work hours

def grossPay():
    hours = int(input("Enter number of hours worked: "))
    rate = float(input("Enter the agreed per hour: "))

    pay = hours * rate

    if hours >= 40:
        payPlus = hours * (rate*1.5)
        print("payment is ", payPlus)
    
    else:
        print("payment is ", pay)


if __name__== "__main__":
    grossPay()