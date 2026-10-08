# Engineering Unit Converter

print("Engineering Unit Converter")
print("1. Meter to Kilometer")
print("2. Kilometer to Meter")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
print("5. Kilogram to Gram")
print("6. Gram to Kilogram")

choice = int(input("Enter your choice (1-6): "))

value = float(input("Enter the value: "))

if choice == 1:
    result = value / 1000
    print("Result =", result, "km")

elif choice == 2:
    result = value * 1000
    print("Result =", result, "m")

elif choice == 3:
    result = (value * 9 / 5) + 32
    print("Result =", result, "°F")

elif choice == 4:
    result = (value - 32) * 5 / 9
    print("Result =", result, "°C")

elif choice == 5:
    result = value * 1000
    print("Result =", result, "g")

elif choice == 6:
    result = value / 1000
    print("Result =", result, "kg")

else:
    print("Invalid choice. Please select between 1 and 6.")
