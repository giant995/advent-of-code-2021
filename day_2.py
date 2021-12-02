# Part 1
with open("day2.input") as f:
    horizontal = 0
    vertical = 0

    for line in f:
        coords = line.rstrip().split(" ")
        if coords[0] == "up":
            vertical -= int(coords[1])
        elif coords[0] == "down":
            vertical += int(coords[1])
        elif coords[0] == "forward":
            horizontal += int(coords[1])

    print(vertical*horizontal)

# Part 2
with open("day2.input") as f:
    horizontal = 0
    vertical = 0
    aim = 0

    for line in f:
        coords = line.rstrip().split(" ")
        if coords[0] == "up":
            aim -= int(coords[1])
        elif coords[0] == "down":
            aim += int(coords[1])
        elif coords[0] == "forward":
            horizontal += int(coords[1])
            vertical += aim * int(coords[1])

    print(vertical*horizontal)
