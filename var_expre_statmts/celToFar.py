
def theOther():
    tempQues = input("""
        What Temperature do you want to convert from?

            Celsius or Fahrenheit
                C   /    F
                
                :  """)
    # changing the input to lowercase, to fulfil conditonal statements
    tempQues = tempQues.lower()
# first conditional for celsius
    if tempQues == "c":
        tempC = float(input("Enter the temperature in celsius: "))
        farConv = (tempC * 1.8)+32
        print(farConv,"F")
#  second condition for fahrenhiet
    elif tempQues == "f":
        tempF = float(input("Enter the temperature in fahrenheit: "))
        celConv = (tempF - 32)*0.5556
        print(celConv,"C")
#  raising an exception
    else:
        raise Exception("Temperature can be c or f only !!")

if __name__ == "__main__":
    theOther()