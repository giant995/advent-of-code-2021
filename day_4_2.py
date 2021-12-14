boards = []

with open("day4_2.input") as file:
    drawn_numbers = file.readline().rstrip().split(",")
    file.readline()

    board = []
    for line in file:
        if line != "\n":
            board = board + line.rstrip().split()
        else:
            boards.append(board)
            board = []


def check_number(number):
    for b in boards:
        b[:] = ["-1" if int(n) == number else n for n in b]


def check_bingo():
    for b in boards:
        for i in range(5):
            if int(b[i]) == -1 and int(b[i+1]) == -1 and int(b[i+2]) == -1 and int(b[i+3]) == -1 and int(b[i+4]) == -1:
                pass


for num in drawn_numbers:
    # check for numbers
    check_number(int(num))
    print(boards)
