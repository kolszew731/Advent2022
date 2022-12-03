
def solve():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    sum = 0
    conontOf3 = len(lines) // 3
    for n in range(conontOf3):
        lines3 = lines[n * 3:(n + 1) * 3]
        common = set(lines3[0])&set(lines3[1])&set(lines3[2])
        for c in common:
            if (c.isupper()):
                sum += ord(c) - 38
            else:
                sum += ord(c) - 96
    print(sum)

if __name__ == '__main__':
    solve();
