employee_name = input("Enter your name: ")
hourly_wage = float(input("Enter your hourly wage: "))
hours_worked = float(input("Enter the number of hours worked: "))

weekly_pay = hourly_wage * hours_worked

print(f"{employee_name.title().strip()} earned ${weekly_pay:.2f} this week.")


