def solve():
    with open('input.txt') as f:
        lines = f.readlines()
    sum_val = 0
    for line in lines:
        line = line.strip()
        middle = len(line) // 2
        left_part = line[:middle]
        right_part = line[middle:]
        common = set(left_part) & set(right_part)
        for c in common:
            if c.isupper():
                sum_val += ord(c) - 38
            else:
                sum_val += ord(c) - 96
    print(sum_val)


if __name__ == '__main__':
    solve()

