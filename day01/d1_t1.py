
def solve():
    with open('input.txt') as f:
        lines = f.readlines()
    max_val = 0
    sum_val = 0
    for line in lines:
        if line.strip() == '':
            if sum_val > max_val:
                max_val = sum_val
            sum_val = 0
        else:
            sum_val += int(line)
    print(max_val)


if __name__ == '__main__':
    solve()

