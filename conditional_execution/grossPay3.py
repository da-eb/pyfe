# this program computes the gross pay and gives 1.5 extra bonus for 40+ work hours

def grossPay():
    hours = (input("Enter number of hours worked: "))
    rate = (input("Enter the agreed per hour: "))

    try:
        hours = int(hours)
        rate = float(rate)
        pay = hours * rate

        if hours >= 40:
            payPlus = hours * (rate*1.5)
            print("payment is ", payPlus)
        
        else:
            print("payment is ", pay)
    except:
        raise Exception("Error, Please enter a numeric input, Thanks")

if __name__== "__main__":
    grossPay()