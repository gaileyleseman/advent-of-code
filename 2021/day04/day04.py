import numpy as np


def parse_text(input_txt):
    data = open(input_txt, "r").read().split('\n\n')
    numbers = [int(number) for number in data[0].split(",")]
    boards_data = [entry.split("\n") for entry in data[1:]]
    new_boards = []
    for item in boards_data:
        new_board = []
        for line in item:
            board_row = [int(number) for number in line.split(" ") if number != ""]
            new_board.append(board_row)
        new_board = np.array(new_board, dtype=object)
        new_boards.append(new_board)
    return numbers, new_boards


def check_for_bingo(board):
    for j in range(5):
        row = board[j]
        col = board.T[j]
        if np.count_nonzero(row) == 0 or np.count_nonzero(col) == 0:
            return True
    return False


def get_final_score(boards, board_index, winning_number):
    winning_board = boards[board_index]
    score = sum(winning_board[winning_board != np.array(None)])
    final_score = score * winning_number
    return final_score


def part1(input_txt):
    numbers, boards = parse_text(input_txt)
    for number in numbers:
        for b in range(len(boards)):
            board = boards[b]
            if number in board:
                board[np.where(board == number)] = None
                if check_for_bingo(board):
                    score = get_final_score(boards, b, number)
                    return score
    return False


def part2(input_txt):
    numbers, boards = parse_text(input_txt)
    n_boards = len(boards)
    winners = []
    for number in numbers:
        for b in range(n_boards):
            if b not in winners:
                board = boards[b]
                if number in board:
                    board[np.where(board == number)] = None
                    if check_for_bingo(board):
                        winners.append(b)
                        if len(set(winners)) == n_boards:
                            score = get_final_score(boards, b, number)
                            return score
    return False


if __name__ == '__main__':
    test_txt = "test.txt"
    input_txt = "input.txt"

    print("TEST: Part 1: ", part1(test_txt))
    print("Part 1: ", part1(input_txt))

    print("TEST: Part 2: ", part2(test_txt))
    print("Part 2: ", part2(input_txt))
