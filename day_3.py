word_length = 12
lines = []
with open("day3.input") as file:
    for line in file:
        lines.append(line.rstrip())


def count_bits(bit_str):
    bits_count = {}
    for i in range(len(bit_str)):
        if bit_str[i] == "0":
            bits_count.setdefault(i % word_length, {0: 0, 1: 0})[0] += 1
        else:
            bits_count.setdefault(i % word_length, {0: 0, 1: 0})[1] += 1
    return bits_count


data = ''.join(line.rstrip() for line in lines)
gamma = ""
epsilon = ""
count = count_bits(data)
for key, value in count.items():
    if value[0] > value[1]:
        gamma += "0"
        epsilon += "1"

    else:
        gamma += "1"
        epsilon += "0"

print(f"power consumption: {int(gamma, 2) * int(epsilon, 2)}")


# Part 2
idx = 0
oxygen = lines
while len(oxygen) != 1:
    oxygen_subset = []
    oxygen_str = ''.join(report_line.rstrip() for report_line in oxygen)
    oxygen_bits_count = count_bits(oxygen_str)

    if oxygen_bits_count[idx % word_length][0] > oxygen_bits_count[idx % word_length][1]:
        oxygen_subset = [report_line for report_line in oxygen if report_line[idx % word_length] == "0"]
    else:
        oxygen_subset = [report_line for report_line in oxygen if report_line[idx % word_length] == "1"]

    oxygen = oxygen_subset
    idx += 1

scrubber = lines
while len(scrubber) != 1:
    scrubber_subset = []
    scrubber_str = ''.join(report_line.rstrip() for report_line in scrubber)
    scrubber_bits_count = count_bits(scrubber_str)

    if scrubber_bits_count[idx % word_length][0] > scrubber_bits_count[idx % word_length][1]:
        scrubber_subset = [report_line for report_line in scrubber if report_line[idx % word_length] == "1"]
    else:
        scrubber_subset = [report_line for report_line in scrubber if report_line[idx % word_length] == "0"]

    scrubber = scrubber_subset
    idx += 1

print(f"life support rating: {int(oxygen[0],2) * int(scrubber[0], 2)}")
