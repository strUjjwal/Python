# PASSWORD GENERATOR
import random

fnl = []
alph = int(input("How many alphabets do you want in your password?"))
count = alph

list_alph = ['A', 'b', 'C', 'd', 'E', 'f', 'G', 'h', 'I', 'j', 'K', 'l', 'M', 'n', 'O', 'p', 'Q', 'r', 'S',
        't', 'U', 'v', 'W', 'x', 'Y', 'z']
list_sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+']
list_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

while count != 0:
    fnl.append(list_alph[random.randint(0, 25)])
    count -= 1

num = int(input("How many numbers do you want in your password?"))
count = num

while count != 0:
    fnl.append(list_num[random.randint(0, 9)])
    count -= 1

sym = int(input("How many symbols do you want in your password?"))
count = sym

while count != 0:
    fnl.append(list_sym[random.randint(0, 12)])
    count -= 1

random.shuffle(fnl)
str = ""
for i in fnl:
    str += i
print(f"You can use \"{str}\" as your password.")
