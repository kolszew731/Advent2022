
def solve():
    with open('input.txt') as f:
        lines = f.readlines()
    max = 0;
    sum = 0;
    for line in lines:
        if (line.strip() == ''):
            if (sum > max):
                max = sum
            sum = 0
        else:
            sum += int(line)
    print(max)

if __name__ == '__main__':
    solve();
