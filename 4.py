import utils
import re

FIELDS = set([
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        "cid",
        ])

def is_valid(line):
    pairs = re.split(r'\n|\s', line)
    fields = set([pair.split(":")[0] for pair in pairs if pair])
    diff = (FIELDS - fields)
    # print(f"line = {line}\npairs = {pairs}\nfields = {fields}\ndiff = {diff}")
    return diff == set() or diff == {'cid'}

def is_data_valid(line):
    pairs = line.split()
    for pair in pairs:
        if pair:
            key, val = pair.split(":")
            if not is_pair_valid(key, val):
                return False
    return True


def is_pair_valid(key, val):
    if key == 'byr':
        return 1920 <= int(val) <= 2002
    elif key == 'iyr':
        return 2010 <= int(val) <= 2020
    elif key == 'eyr':
        return 2020 <= int(val) <= 2030
    elif key == 'hgt':
        if m := re.match(r'(\d+)(cm|in)', val):
            n, unit = m.groups()
            n = int(n)
            if unit == 'cm':
                return 150 <= n <= 193
            elif unit == 'in':
                return 59 <= n <= 76
        return False
    elif key == 'hcl':
        return re.match('#[0-9a-f]{6}', val)
    elif key == 'ecl':
        return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return re.match('(\d{9})', val)
    elif key == 'cid':
        return True
    else:
        raise AssertionError(f"wtf is {key}")



def first(inp):
    passports = re.split('\n\n', inp)
    count = 0
    for passport in passports:
        if is_valid(passport):
            count += 1
    print(count)

def second(inp):
    passports = re.split('\n\n', inp)
    count = 0
    for passport in passports:
        vf = is_valid(passport)
        vd = is_data_valid(passport)
        if vf and vd:
            count += 1
    print(count)


inp = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

inp = utils.get_raw_input(4)
first(inp)
second(inp)
