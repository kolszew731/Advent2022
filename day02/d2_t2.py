# A, X Rock
# B, Y Paper
# C, Z Scissor

# X You must lose
# Y You must draw
# Z You must win

def make_your_choice(line):
    moves = {"A X": "A Z", "A Y": "A X", "A Z": "A Y",
             "B X": "B X", "B Y": "B Y", "B Z": "B Z",
             "C X": "C Y", "C Y": "C Z", "C Z": "C X"}
    return moves[line]


def calc_points_for_result(line):
    wins = ["A Y", "B Z", "C X"]
    draws = ["A X", "B Y", "C Z"]
    return wins.count(line) * 6 + draws.count(line) * 3


def calc_points_for_your_choice(line):
    choices_and_points = {"X": 1, "Y": 2, "Z": 3}
    return choices_and_points[line[-1]]


def solve():
    with open('input.txt') as f:
        lines = f.readlines()
    sum_val = 0
    for line in lines:
        line = line.strip()
        line = make_your_choice(line)
        sum_val += calc_points_for_result(line) + calc_points_for_your_choice(line)
    print(sum_val)


if __name__ == '__main__':
    solve()
