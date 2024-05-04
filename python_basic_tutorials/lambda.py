# go check in the palindromechecker and map,filter file
squarer = lambda x: x * x
print(squarer(2))


def apply(fx, val):
    return 6 + fx(val)


print(apply(squarer, 4))
