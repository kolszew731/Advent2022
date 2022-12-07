def solve():
    with open('input.txt') as f:
        line = f.readlines()[0]
    find_range = 14
    position = 0
    for i in range(len(line) - find_range):
        set_of_range = set()
        for j in range(find_range):
            set_of_range.add(line[i +j])
        if len(set_of_range) == find_range:
            position = i + find_range
            break
    print(position)


if __name__ == '__main__':
    solve()
