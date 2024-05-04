# a = True
# print(a := False)
#
# _list = [1, 2, 3, 4, 5]
#
# while (n := len(_list)) > 0:
#     _list.pop()
#     print(_list)

# ------------------------------------------------------------------------ #

names = []  # or list()
while True:
    name = input('Enter a name or no to quit')
    if name == 'no':
        break
    names.append(name)

#       OR(with walrus)nn

names = list()
while (name := input('Enter a name or no to quit') != 'no'):
    names.append(name)
