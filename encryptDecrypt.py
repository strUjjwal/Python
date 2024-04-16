def encrypt(lst1, sft):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cipher_text = ""
    for a in lst1:
        index_of_user_input = lst1.index(a)
        new_index = (alph.index(a) + sft) % 26
        cipher_text += alph[new_index]
    print(cipher_text)
    # print("Encrypted:", ''.join(lst1))


def decrypt(lst1, sft):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encipher_text = ""
    for b in lst1:
        index_of_user_input = lst1.index(b)
        new_index = (alph.index(b) - sft) % 26
        encipher_text += alph[new_index]
    print(encipher_text)


resp = True
while resp == True:
    what_to_do = input("type 'encrypt' or 'decrypt':")
    text0 = input("Enter your text:")
    shift0 = int(input("enter shift level:"))
    list1 = []
    for i in text0:
        list1 += i
    if what_to_do == "encrypt":
        encrypt(list1, shift0)
    elif what_to_do == "decrypt":
        decrypt(list1, shift0)
    haha = input("to continue type 'yes' and to stop the program type 'no,")
    if haha == 'no':
        resp = False
