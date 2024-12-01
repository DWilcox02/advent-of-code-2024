FILENAME = "./input.txt"


# Part 1
def part1():
    with open(FILENAME) as file:
        pairs = [line.rstrip().split() for line in file]
        l1 = [int(pair[0]) for pair in pairs]
        l1.sort()
        l2 = [int(pair[1]) for pair in pairs]
        l2.sort()
        dists = [abs(x - y) for x, y in zip(l1, l2)]
        return sum(dists)

# Part 2
def part2():
    with open(FILENAME) as file:
        pairs = [line.rstrip().split() for line in file]
        l1 = [int(pair[0]) for pair in pairs]
        l2 = [int(pair[1]) for pair in pairs]
        freqs = {i: l2.count(i) for i in set(l2)}
        return sum([i * freqs.get(i, 0) for i in l1])

print(part2())
