boards = []

with open("day4.input") as file:
    drawn_numbers = file.readline().rstrip().split(",")
    file.readline()

    board = []
    for line in file:
        if line != "\n":
            board.append({item: 0 for item in line.rstrip().split()})
        else:
            boards.append(board)
            board = []


def check_number(number):
    for bingo_board in boards:
        for board_line in bingo_board:
            if number in board_line:
                board_line[number] = 1


def check_bingo():
    # check lines
    for bingo_board in boards:
        for board_line in bingo_board:
            if all(val == 1 for val in board_line.values()):
                return bingo_board

    # check columns
    for bingo_board in boards:
        for i in range(5):
            if list(bingo_board[0])[i] == 1 and list(bingo_board[1])[i] == 1 and list(bingo_board[2])[i] == 1 \
                    and list(bingo_board[3])[i] == 1 and list(bingo_board[4])[i] == 1:
                return bingo_board


def get_card_score(bingo_board):
    score = 0
    for board_line in bingo_board:
        for key, val in board_line.items():
            if val == 0:
                score += int(key)

    return score


bingo = None
winning_number = -1
for num in drawn_numbers:
    check_number(num)
    bingo = check_bingo()
    if bingo:
        card_score = get_card_score(bingo)
        print(f"final score: {int(num)*card_score}")
        break
