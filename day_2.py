horizontal = 0
vertical = 0

with open("day2.input") as f:
    # part 1
    for line in f:
        coords = line.rstrip().split(" ")
        if coords[0] == "up":
            vertical -= int(coords[1])
        elif coords[0] == "down":
            vertical += int(coords[1])
        elif coords[0] == "forward":
            horizontal += int(coords[1])

print(vertical*horizontal)
