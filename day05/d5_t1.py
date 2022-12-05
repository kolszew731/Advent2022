

def solve():
    stacks = [list("HTZD"), list("QRWTGCS"), list("PBFQNRCH"),
              list("LCNFHZ"), list("GLFQS"), list("VPWZBRCS"),
              list("ZFJ"), list("DLVZRHQ"), list("BHGNFZLD")]
    with open('input.txt') as f:
        lines = f.readlines()
    lines = [l.replace("move ", "").replace(" from ", ",").replace(" to ", ",").strip() for l in lines]
    for line in lines:
        command = line.split(",")
        count = int(command[0])
        move_from = int(command[1]) - 1
        move_to = int(command[2]) - 1
        for _ in range(count):
            stacks[move_to].append(stacks[move_from].pop())
    for stack in stacks:
        print(stack.pop(), end="")

if __name__ == '__main__':
    solve()
