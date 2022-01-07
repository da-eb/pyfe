# this program computes the gross pay


def grossPay():
    hours = input("Enter number of hours worked: ")
    rate = input("Enter the agreed per hour: ")

    pay = int(hours) * float(rate)

    print("payment is ", pay)


if __name__== "__main__":
    grossPay()