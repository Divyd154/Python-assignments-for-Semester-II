from temperature.celsius_to_fahrenheit import celsius_to_fahrenheit
from temperature.fahrenheit_to_celsius import fahrenheit_to_celsius
from temperature.celsius_to_kelvin import celsius_to_kelvin

print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit(c))

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius:", fahrenheit_to_celsius(f))

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    print("Kelvin:", celsius_to_kelvin(c))

else:
    print("Invalid choice!")