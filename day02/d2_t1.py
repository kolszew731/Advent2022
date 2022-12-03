# A, X Rock
# B, Y Paper
# C, Z Scisor

def calcPointsForResult(line):
    wins = ["A Y", "B Z", "C X"]
    draws = ["A X", "B Y", "C Z"]
    return wins.count(line) *  6 + draws.count(line) * 3

def calcPointsForYouChose(line):
    chosesAndPoints = {"X":1, "Y":2, "Z":3}
    return chosesAndPoints[line[-1]]

def solve():
    with open('input.txt') as f:
        lines = f.readlines();
    sum = 0;
    for line in lines:
        line = line.strip()
        sum += calcPointsForResult(line) + calcPointsForYouChose(line)
    print(sum)

if __name__ == '__main__':
    solve();
