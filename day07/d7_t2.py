def solve():
    with open('input.txt') as f:
        lines = f.readlines()
    dir_sizes = {}
    pwd = []
    for line in lines:
        line = line.strip()
        if line.startswith("$"):
            line = line[2:]
            if line.startswith("cd"):
                change_to_dir = line[3:]
                if change_to_dir == "..":
                    pwd.pop()
                else:
                    pwd.append(change_to_dir)
                dir_name = "/".join(pwd)
                if dir_name not in dir_sizes:
                    dir_sizes[dir_name] = 0

        if line[0].isdigit():
            line = line.split(" ")[0]
            file_size = int(line)
            pwd_copy = pwd.copy()
            while len(pwd_copy) > 0:
                dir_name = "/".join(pwd_copy)
                dir_sizes[dir_name] = dir_sizes[dir_name] + file_size
                pwd_copy.pop()
    size_of_outermost = dir_sizes["/"]
    size_of_unused_space = 70000000 - size_of_outermost
    size_of_need_space = 30000000 - size_of_unused_space
    dir_sizes = {k:v for (k, v) in dir_sizes.items() if v >= size_of_need_space}
    min_size = min(dir_sizes.values())
    print(min_size)

if __name__ == '__main__':
    solve()
