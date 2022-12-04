def get_range(str_range):
    parts = str_range.split("-")
    calculated_range = [int(parts[0]), int(parts[1])]
    return calculated_range


def full_contain(str_range1, str_range2):
    range1 = get_range(str_range1)
    range2 = get_range(str_range2)
    return range1[0] <= range2[0] and range1[1] >= range2[1] or \
        range1[0] >= range2[0] and range1[1] <= range2[1]


def solve():
    with open('input.txt') as f:
        lines = f.readlines()
    count_full_contain = 0
    for line in lines:
        line = line.strip()
        parts = line.split(",")
        left_part = parts[0]
        right_part = parts[1]
        if full_contain(left_part, right_part):
            count_full_contain += 1

    print(count_full_contain)


if __name__ == '__main__':
    solve()
