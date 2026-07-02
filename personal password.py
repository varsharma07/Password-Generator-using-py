import random

print("===== Personalized Password Generator =====")

name = input("Enter your name: ")
food = input("Enter your favorite food: ")
animal = input("Enter your favorite animal: ")
number = input("Enter your lucky number: ")

symbols = ["@", "#", "$", "%", "&", "!", "*", "?"]

passwords = [
    name + random.choice(symbols) + food + number
]

print("\nHere are your personalized passwords:\n")

for i, password in enumerate(passwords, start=1):
    print(f"{i}. {password}")