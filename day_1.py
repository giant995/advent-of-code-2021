import itertools

with open("day1.input") as f:
    lines = f.readlines()
    lines = [int(line.rstrip()) for line in lines]


def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def evaluate_increases(groups):
    increases = 0
    sums = [sum(i) for i in groups]
    for i in range(len(sums) - 1):
        if sums[i + 1] > sums[i]:
            increases = increases + 1

    print(increases)


# Part 1
pairs = pairwise(lines)
evaluate_increases(pairs)


def triplewise(iterable):
    for (a, _), (b, c) in pairwise(pairwise(lines)):
        yield a, b, c


# Part 2
triplets = triplewise(lines)
evaluate_increases(triplets)
