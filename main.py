import random

print("Random Number Generator")

min_number = int(input("Enter the minimum number: "))
max_number = int(input("Enter the maximum number: "))

random_number = random.randint(min_number, max_number)

print("Generated Number:", random_number)
