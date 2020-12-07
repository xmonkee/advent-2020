import utils

def first(inp):
    groups = inp.split('\n\n')
    total_count = 0
    for group in groups:
        questions = [0]*26
        for person in group.split('\n'):
            for question in person:
                questions[ord(question)-ord('a')] = 1
        count = sum(questions)
        total_count += count
    print(total_count)

def second(inp):
    groups = inp.split('\n\n')
    total_count = 0
    for group in groups:
        questions = [0]*26
        persons = group.split('\n')
        n_persons = len(persons)
        for person in group.split('\n'):
            for question in person:
                questions[ord(question)-ord('a')] += 1
        count = sum([1 for question in questions if question == n_persons])
        total_count += count
    print(total_count)

inp = utils.get_raw_input(6)
first(inp)
second(inp)
