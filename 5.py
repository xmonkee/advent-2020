import re
import utils

def get_row(s):
    a = re.sub('F', '0', s[:7])
    a = re.sub('B', '1', a)
    return int(a, 2)

def get_col(s):
    a = re.sub('L', '0', s[-3:])
    a = re.sub('R', '1', a)
    return int(a, 2)

def get_id(s):
    return get_row(s) * 8 + get_col(s)

def first(inp):
    ids = [get_id(s) for s in inp]
    print(max(ids))

def second(inp):
    ids = set([get_id(s) for s in inp])
    all_ids = set(x for x in range(128 * 8))
    missing = all_ids - ids
    final_missing = set(n for n in missing if n-1 not in missing and n+1 not in missing)
    print(final_missing)


inp = utils.get_input(5, False)
first(inp)
second(inp)
