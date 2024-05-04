def greet(fx):
    def mfx(*args, **kwargs):
        print('\nGood morning')
        fx(*args, **kwargs)
        print('Goodbye\n')
    return mfx


def add(a, b):
    print(a+b)


@greet
def hello():
    print('Hello world')


hello()
hello()
greet(add)(1, 2)
add(1, 2)

