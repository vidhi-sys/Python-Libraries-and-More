choice = input("Convert to (F/C): ").upper()

temp = float(input("Enter temperature: "))

if choice == "F":
    print(f"Fahrenheit: {(temp * 9/5) + 32}")
elif choice == "C":
    print(f"Celsius: {(temp - 32) * 5/9}")
else:
    print("Invalid choice")
