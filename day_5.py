kofi = ["espresso", "latte", "cappuccino"]

kofi_new = ["espresso", "latte", "cappuccino"]

print(id(kofi) == id(kofi_new))

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

numbers = [1, 2, 3, 4]
numbers.append(5)

print(new_numbers is numbers)

number = int(input("Enter a number: "))

if number < 0:
    print("Number is negative")
elif number == 0:
    print("Number is zero")
else:
    print("Number is positive")


hourly_wage = int(input("Enter your hourly wage: "))
hours_worked = int(input("Enter the number of hours worked: "))

if hours_worked > 40:
    print("You worked overtime. Your total pay is $", hourly_wage * 40 + (hours_worked - 40) * 1.1 * hourly_wage)
else:
    print("You did not work overtime. Your total pay is $", hourly_wage * hours_worked)
