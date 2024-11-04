import random

# Guessing Game

attempts = 9

number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {attempts} attempts to guess it.")
print("Good luck!")

guess = int(input("Enter your guess: "))

while attempts > 0:
    if guess < number:
        print("Too low. Try again.")
        attempts -= 1
    elif guess > number:
        print("Too high. Try again.")
        attempts -= 1
    else:
        print("Congratulations! You guessed the number.")
        break
    guess = int(input("Enter your guess: "))

if attempts == 0:
    print("Sorry, you ran out of attempts. The number was", number)


# Continue Statement

word = "Python"

for letter in word:
    if letter == "o":
        continue
    print(letter)


number = 3

while number < 100:
    count = 2
    while count < number:
        if number % count == 0:
            break
        else:
            count += 1
    number += 1
print(number)

