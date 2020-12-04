import requests

SESSION = requests.sessions.Session()
SESSION.cookies.update({'session':'53616c7465645f5f566276e4880ef8189a82baff95f3f68e84df2a221d6a443e5b8a72b4a465726e0bd222a6313c4370'})

def get_raw_input(problem_number, as_num=True):
   inp = SESSION.get(f'https://adventofcode.com/2020/day/{problem_number}/input').text[:-1]
   return inp


def get_input(problem_number, as_num=True):
   inp = get_raw_input(problem_number)
   inp = inp.split('\n')[:-1]
   if as_num:
       inp = map(int, inp)
   return inp

def split(s, sep, as_num=False):
    ret = [k.strip() for k in s.split(sep)]
    if as_num:
        ret = map(int, ret)
    return ret

if __name__ == '__main__':
    print(list(get_input(1)))
