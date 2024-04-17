# Silent Auction Program
import os


def winner(info):
    least = -1
    for i in info.keys():
        if least < info[i]:
            least = info[i]
            name = i
    print(f"Winner is {name} with a bid of {least}")


flag = True
list00 = []
info = {}  # empty dictionary
while flag is True:

    name = input("Enter a name:")
    name = name.lower()
    bid = int(input(f"{name} enter your bid:"))
    info[name] = bid  # assigning values to the empty dictionary
    name = input("Enter 'y' for next bidder or 'n' for no bidder:")
    if name == "n":
        flag = False
        break
    elif name == 'y':
        os.system('clear')
winner(info)  # calling function
