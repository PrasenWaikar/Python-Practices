temp_celsius = float(input("Enter temperature in Celsius: "))
if temp_celsius < 0:
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", temp_fahrenheit)
else:
    temp_kelvin = temp_celsius + 273.15
    print("Temperature in Kelvin:", temp_kelvin)
