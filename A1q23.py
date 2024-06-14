def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
choice = input("Choose an option (1 or 2): ")
if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(celsius, "Celsius is equal to", fahrenheit," Fahrenheit")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(fahrenheit, "Fahrenheit is equal to ",celsius, "Celsius")
else:
    print("Invalid choice. Please choose either 1 or 2.")