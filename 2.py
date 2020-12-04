import utils

inp = utils.get_input(2, False)

def first():
    good_count = 0
    for line in inp:
        policy, password = utils.split(line, ":")
        rng, letter = policy.split()
        min_r, max_r = utils.split(rng, "-", as_num=True)
        cnt = password.count(letter)
        if (min_r <= cnt <= max_r):
            good_count += 1
    print(good_count)
    return

def second():
    good_count = 0
    for line in inp:
        policy, password = utils.split(line, ":")
        rng, letter = policy.split()
        min_r, max_r = utils.split(rng, "-", as_num=True)
        if (password[min_r-1] == letter) != (password[max_r-1] == letter):
            good_count += 1
    print(good_count)
    return

first()
second()
