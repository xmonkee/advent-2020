import utils


def first(inp):
    trees = 0
    j = 0;
    for line in inp:
        width = len(line)
        if line[j] == "#":
            trees += 1
        j = (j + 3) % width
    print(trees)

def second(inp):
    slopes = [(1, 1),  (3, 1), (5, 1), (7, 1), (1, 2)]
    inp = list(inp)
    height = len(inp)
    width = len(inp[0])
    prod = 1

    for slope in slopes:
        right, down = slope
        trees = 0
        i = j = 0
        while i < height:
            line = inp[i]
            if line[j] == "#":
                trees += 1
            i = i + down
            j = (j + right) % width
        prod = prod * trees
    print(prod)

inp = utils.get_input(3, as_num=False)
first(inp)
second(inp)
