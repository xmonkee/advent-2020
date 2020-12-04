import utils

inp = utils.get_input(1)
s = set(inp)
def first():
    for n in s:
        if 2020 - n in s:
            print(n, 2020 - n)
            print(n * (2020 - n))
            return

def second():
    for i in s:
        for j in s:
            if j != i:
                k = 2020 - (i + j)
                if k in s:
                    print(i, j, k)
                    print(i * j * k)
                    return

first()
second()
