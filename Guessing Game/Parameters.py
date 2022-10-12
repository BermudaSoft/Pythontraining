def start():
    print('What is the starting number?')
    a = input()
    return a


def end():
    print('What is the ending number?')
    b = input()
    c = int(b) + 1
    return c


s = start()
e = end()

if __name__ == '__main__':
    print(s)
    print(e)
