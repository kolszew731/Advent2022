# A, X Rock
# B, Y Paper
# C, Z Scissor

def calc_points_for_result(line):
    wins = ["A Y", "B Z", "C X"]
    draws = ["A X", "B Y", "C Z"]
    return wins.count(line) * 6 + draws.count(line) * 3


def calc_points_for_you_choice(line):
    choices_and_points = {"X": 1, "Y": 2, "Z": 3}
    return choices_and_points[line[-1]]


def solve():
    with open('input.txt') as f:
        lines = f.readlines()
    sum_val = 0
    for line in lines:
        line = line.strip()
        sum_val += calc_points_for_result(line) + calc_points_for_you_choice(line)
    print(sum_val)


if __name__ == '__main__':
    solve()
