question = input("Is this temperature in Celsius or Fahrenheit (C/F): ")

if question != "C" and "F":

 print(f"{question} is an invalid unit of measurement")

temp = float(input("Enter the temp: "))

if question == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} °F")

elif question == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Fahrenheit is: {temp} °C")



