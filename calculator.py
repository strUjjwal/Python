# 01

def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mplt(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


cont = True
while cont is True:
    num1 = int(input("Enter first number:"))
    print('+\n', '-\n', '*\n', '/')
    # call function
    call = dict({
        '+': add,
        '-': sub,
        '*': mplt,
        '/': div
    })
    res = 0
    ask = ""
    cont1 = True
    while cont1 is True:
        opr = input("Pick an operator:")
        num2 = int(input("Enter another number:"))
        temp = call[opr]
        res = temp(num1, num2)
        print(f"Sum of {num1}{opr}{num2}={res}")
        ask = input("Type \"y\" to continue, \"n\" to stop, \"x\" to start a new calculation?")
        if ask == 'y':
            num1 = res
        elif ask == 'x':
            cont1 = False
            cont = True
        else:
            cont1 = False
            cont = False
            print(res)

