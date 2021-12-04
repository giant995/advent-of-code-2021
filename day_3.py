lines = []
with open("day3.input") as file:
    for line in file:
        lines.append(line.rstrip())


# Part 1
data = ''.join(line.rstrip() for line in lines)
count = {}
for i in range(len(data)):
    if data[i] == "0":
        count.setdefault(i % 12, {0: 0, 1: 0})[0] += 1
    else:
        count.setdefault(i % 12, {0: 0, 1: 0})[1] += 1

gamma = ""
epsilon = ""
for key, value in count.items():
    if value[0] > value[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(f"power consumption: {int(gamma, 2) * int(epsilon, 2)}")
