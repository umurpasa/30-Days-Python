# employees = [
#     ("Rolf Smith", 35, 8.75),
#     ("Anne Pun", 30, 12.50),
#     ("Charlie Lee", 50, 15.50),
#     ("Bob Smith", 20, 7.00)
# ]
# total_hourly_wage = 0

# for employee in employees:
#     print(f"{employee[0]} weekly salary is ${employee[1] * employee[2]:.2f}")
#     total_hourly_wage += employee[2]

# average_hourly_wage = total_hourly_wage / len(employees)

# for employee in employees:
#     if employee[2] > average_hourly_wage:
#         print(f"{employee[0]} earns more than average hourly wage")


# Day 7 

name_surname = input("Please enter your name and surname: ")

print(name_surname.split())

name = name_surname.split()[0]
surname = name_surname.split()[1]

print(name)
print(surname)

list = [1, 2, 3, 4, 5]

print(" | ".join(str(item) for item in list))

quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
 ]

for quote in quotes:
    print(quote.strip("'"))

for quote in quotes:
    print(quote[1:-1])

word = input("Please enter a word: ")

print(len(word))