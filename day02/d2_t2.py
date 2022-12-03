# A, X Rock
# B, Y Paper
# C, Z Scisor

# X You must lose
# Y You must draw
# Z You must win

def makeYourChose(line):
    moves = {"A X":"A Z", "A Y":"A X", "A Z":"A Y",
             "B X":"B X", "B Y":"B Y", "B Z":"B Z",
             "C X":"C Y", "C Y":"C Z", "C Z":"C X"}
    return moves[line]

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
        line = makeYourChose(line)
        sum += calcPointsForResult(line) + calcPointsForYouChose(line)
    print(sum)

if __name__ == '__main__':
    solve();
