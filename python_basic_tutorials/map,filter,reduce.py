###############---------M A P--------####################
list_1 = [1, 3, 5, 7, 9, 11, 13, 15]

new_list_1 = list(map(lambda x: x * x, list_1))

print(new_list_1)

###############---------F I L T E R--------####################
list_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_grater_than_2(a):
    return a > 2


new_list_2 = filter(is_grater_than_2, list_2)
new_list_2 = list(new_list_2)
print(new_list_2)

###############---------R E D U C E--------####################
from functools import reduce

list_3 = [1, 2, 3, 4, 5]
mysum = lambda x, y: x + y

new_list_3 = reduce(mysum, list_3)
print(new_list_3)
# [1, 2, 3, 4, 5]
# [3, 3, 4, 5]
# [6, 4, 5]
# [10, 5]
# [15]
