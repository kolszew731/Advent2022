def solve():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    sum_val = 0
    count_of_3 = len(lines) // 3
    for n in range(count_of_3):
        lines3 = lines[n * 3:(n + 1) * 3]
        common = set(lines3[0]) & set(lines3[1]) & set(lines3[2])
        for c in common:
            if c.isupper():
                sum_val += ord(c) - 38
            else:
                sum_val += ord(c) - 96
    print(sum_val)


if __name__ == '__main__':
    solve()
