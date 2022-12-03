
def solve():
    with open('input.txt') as f:
        lines = f.readlines();
    sum = 0
    for line in lines:
        line = line.strip()
        middle = len(line) // 2
        leftPart = line[:middle]
        rightPart = line[middle:]
        common = set(leftPart)&set(rightPart)
        for c in common:
            if (c.isupper()):
                sum += ord(c) - 38
            else:
                sum += ord(c) - 96
    print(sum)

if __name__ == '__main__':
    solve();
