temp=int(input("Enter temperature: "))
unit=input("Enter unit (C/F): ")
if unit=="C" or unit=="c":
    convertedtemp=(temp*9/5)+32
    print(temp, "degrees Celsius is", convertedtemp, "degrees Fahrenheit")
elif unit=="F" or unit=="f":
    convertedtemp=(temp-32)*5/9
    print(temp, "degrees Fahrenheit is", convertedtemp, "degrees Celsius")
else:
    print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
