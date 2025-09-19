def dec(fun):
    def wrapper():
        print('before function called')
        fun()
        print('after function called')
    return wrapper
@dec
def hey():
    print('hey j')
hey()