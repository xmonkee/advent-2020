import utils
import re
from collections import defaultdict

def parse_rule(line):
    containing, contained = line.split(" bags contain ")
    contained = [re.sub(r' bags?\.?','', x) for x in contained.split(", ")]
    contained = [c for c in contained if c != 'no other']
    contained = [re.match(r'(\d+) (.*)', c).groups() for c in contained]
    return (containing, contained)

def get_outer_containers(graph, color):
    for c in graph[color]:
        yield c
        yield from get_outer_containers(graph, c)


def first(inp):
    graph = defaultdict(list)
    for line in inp:
        containing, contained = parse_rule(line)
        for n, color in contained:
            graph[color].append(containing)

    print(len(set(get_outer_containers(graph, 'shiny gold'))))


def find_sub_bags(graph, curr):
    count = 0
    for (n, color) in graph[curr]:
        count += int(n)
        count += int(n) * find_sub_bags(graph, color)
    return count


def second(inp):
    graph = {}
    for line in inp:
        containing, contained = parse_rule(line)
        graph[containing] = contained
    print(find_sub_bags(graph, 'shiny gold'))




inp = utils.get_input(7, False)
first(inp)
second(inp)
