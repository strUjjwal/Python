# HANGMAN GAME
import random

list00 = ["macbook", "python", "modi", "kennedy", "biden", "random", "shinchan", "history", "physics"]
chance = 6
list01 = []
show00 = []
show01 = ""
word = list00[random.randint(0, 8)]
for i in word:
    list01.append(i)
    show00.append('_')
    show01 += i
T_alpha = len(word)

print(f"The word contain {T_alpha} alphabets")
print(show00)
huehue = False
while huehue is False:
    guess = input("Enter your guess:")
    guess = guess.lower()
    if guess in list01:
        print("Correct Guess")
        show00[list01.index(guess)] = list01[list01.index(guess)]
        print(show00)
        list01[list01.index(guess)] = 0
    else:
        print("Wrong Guess")
        chance -= 1
        print(f"{chance} chances left")

    if chance == 0:
        print("GAME OVER!")
        print(f"The word was \"{show01}\"")
        huehue = True
    elif '_' not in show00:
        huehue = True
        print("YOU WON!")