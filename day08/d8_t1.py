def tree_is_not_visibe(area, i, j):
    tree_hight = int(area[i][j])
    all_lower = True
    for jn in range(j):
        if int(area[i][jn]) >= tree_hight:
            all_lower = False
            break
    if all_lower:
        return False
    all_lower = True
    for jn in range(j + 1, len(area[i])):
        if int(area[i][jn]) >= tree_hight:
            all_lower = False
            break
    if all_lower:
        return False
    all_lower = True
    for ien in range(i):
        if int(area[ien][j]) >= tree_hight:
            all_lower = False
            break
    if all_lower:
        return False
    all_lower = True
    for ien in range(i + 1, len(area)):
        if int(area[ien][j]) >= tree_hight:
            all_lower = False
            break
    if all_lower:
        return False
    return True


def mark_is_not_visible(vivibility_marks, i, j):
    vivibility_marks[i][j] = 10


def mark_not_visible(area, area_vivibility_marks):
    for i in range(1, len(area) - 1):
        for j in range(1, len(area[i]) - 1):
            if tree_is_not_visibe(area, i, j):
                mark_is_not_visible(area_vivibility_marks, i, j)


def solve():
    area = []
    area_vivibility_marks = []
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        area.append(list(line.strip()))
        area_vivibility_marks.append(list(line.strip()))
    mark_not_visible(area, area_vivibility_marks)
    count_visible = 0
    for row in area_vivibility_marks:
        count_visible += sum(int(elem) < 10 for elem in row)
    print(count_visible)


if __name__ == '__main__':
    solve()
