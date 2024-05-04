import random, string

def gg():
    characters = string.ascii_lowercase
    return ''.join(random.choices(characters, k=3))

def encryption(text):
    splited_text = text.split(' ')

    for i, s in enumerate(splited_text):

        if len(splited_text[i]) <= 2:
            splited_text[i] = s[::-1]

        elif len(splited_text[i]) >= 2:
            s = s[1:] + (s[0])
            splited_text[i] = gg() + s + gg()

    encrypted = " ".join(splited_text)
    return encrypted

def decryption(encrypted):
    splited_text = encrypted.split(' ')

    for i, s in enumerate(splited_text):

        if len(splited_text[i]) <= 2:
            splited_text[i] = s[::-1]

        elif len(splited_text[i]) >= 2:
            s = s[3:-3]
            print(s,' ')
            splited_text[i] = s[:-1]
            splited_text[i] = s[-1] + splited_text[i]

    decrypted = " ".join(splited_text)
    return decrypted

text = input('Enter text : ')

while 1:
    try:
        choice = int(input('1.encrypt\n2.decrypt\n'))

    except Exception as e:
        print(e)

    if choice == 1:
        print(f'Text:\t\t{text}\nEncrypted:\t{encryption(text)}')
        break
    elif choice == 2:
        print(f'Text:\t\t{text}\nDecrypted\t{decryption(text)}')
        break
    elif choice!=1 or choice!=2:
        print('ValueError: please enter 1 or 2 ')
        continue