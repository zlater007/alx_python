import random
number = random.randint(-10, 10)

print(number)
if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")
