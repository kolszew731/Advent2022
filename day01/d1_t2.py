
def solve():
    with open('input.txt') as f:
        lines = f.readlines()
    maxes = [];
    sum = 0;
    for line in lines:
        if (line.strip() == ''):
            maxes.append(sum)
            sum = 0
        else:
            sum += int(line)
    maxes.sort()
    print(maxes.pop() + maxes.pop() + maxes.pop())


if __name__ == '__main__':
    solve();
