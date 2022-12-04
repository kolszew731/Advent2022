def get_range(str_range):
    parts = str_range.split("-")
    calculated_range = [int(parts[0]), int(parts[1])]
    return calculated_range


def has_common_part(str_range1, str_range2):
    range1 = get_range(str_range1)
    range2 = get_range(str_range2)
    return not (range1[0] < range2[0] and range1[1] < range2[0] or
                range1[0] > range2[1] and range1[1] > range2[1])


def solve():
    with open('input.txt') as f:
        lines = f.readlines()
    common_parts = 0
    for line in lines:
        line = line.strip()
        parts = line.split(",")
        left_part = parts[0]
        right_part = parts[1]
        if has_common_part(left_part, right_part):
            common_parts += 1

    print(common_parts)


if __name__ == '__main__':
    solve()
