import string

ignore_others = lambda x: x.translate(str.maketrans('', '', string.punctuation + string.digits + ' '))

check = lambda inputed: print('Yes') if ignore_others(inputed).lower() == ignore_others(inputed).lower()[::-1] else print('No')


# def check(inputed):
#     inputed = ignore_others(inputed).lower()
#     # print(inputed)
#     if inputed == inputed[::-1]:
#         print('Yes')
#     else:
#         print('No')



if __name__ == '__main__':
    text = input("Enter ")  # 'A man, a plan, a canal, Panama!'   Example input
    print(text)
    check(text)
