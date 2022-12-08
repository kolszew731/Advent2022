def calc_vivible_number(area, i, j):
    tree_hight = int(area[i][j])
    n1 = 0
    for jn in range(j - 1, -1, -1):
        n1 += 1
        if int(area[i][jn]) >= tree_hight:
            break
    n2 = 0
    for jn in range(j + 1, len(area[i])):
        n2 += 1
        if int(area[i][jn]) >= tree_hight:
            break
    n3 = 0
    for ien in range(i - 1, -1, -1):
        n3 += 1
        if int(area[ien][j]) >= tree_hight:
            break
    n4 = 0
    for ien in range(i + 1, len(area)):
        n4 += 1
        if int(area[ien][j]) >= tree_hight:
            break
    return n1 * n2 * n3 * n4


def count_visibility(area, visibility_counts):
    for i in range(1, len(area) - 1):
        for j in range(1, len(area[i]) - 1):
            visible_number = calc_vivible_number(area, i, j)
            visibility_counts[i][j] = visible_number

def solve():
    area = []
    visibility_counts = []
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        area.append(list(line.strip()))
        visibility_counts.append(list(range(len(line))))
    count_visibility(area, visibility_counts)
    max_visibility = max([max(l) for l in visibility_counts])
    print(max_visibility)

if __name__ == '__main__':
    solve()
