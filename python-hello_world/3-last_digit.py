import random
number = random.randint(-10000, 10000)

print(number)

last_digit = abs(number) % 10
print("Last digit of the number:", last_digit)

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("änd is 0")
else:
    print("and is less than 6 and not 0")

