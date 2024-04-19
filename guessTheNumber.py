import random

print("You have to choose a number b/w 1-50:")
lvl = input("Choose difficulty level:")
flag = 0
guess = random.randint(1, 50)
# print(guess)
if lvl == 'easy':
    flag = 10
else:
    flag = 5

while flag != 0:
    num = int(input("Enter a number:"))
    if num > guess:
        print("Your guess is too high")
    elif num < guess:
        print("Your guess is too low")
    elif num == guess:
        print("Correct guess")
        break
    flag = flag - 1

