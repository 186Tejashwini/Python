def temp_converter(temp,unit):
    if unit=='celsius':
        convert_temp=(temp*(9/5))+32
    else:
        covert_temp=(temp-32)*(5/9)
    return convert_temp
print("Enter a value to covert:")
temp=int(input())
print("Enter the unit of the temperature(celsius/fahrenheit):")
unit=input().lower()
print(temp_converter(temp,unit))