class Game:

    def __init__(self):
        self.monkeys = []

    def add_monkey(self, monkey):
        self.monkeys.append(monkey)

    def round(self):
        for monkey in self.monkeys:
            monkey.round(self.monkeys)

    def print(self):
        count = 0
        for monkey in self.monkeys:
            print("Monkey" + str(count) + ": ", end="")
            print(monkey.counter_inspected, end="")
            print(" - ", end="")
            print(monkey.items)
            count += 1

    def monkey_business(self):
        monkeys_copy = self.monkeys.copy()
        monkeys_copy.sort(key=lambda x: x.counter_inspected, reverse=False)
        return monkeys_copy[-2].counter_inspected * monkeys_copy[-1].counter_inspected

class Monkey:

    def __init__(self, items, operation, operation_number, division_by, true_destination, false_destination):
        self.false_destination = false_destination
        self.true_destination = true_destination
        self.division_by = division_by
        self.operation = operation
        self.operation_number = operation_number
        self.items = items
        self.counter_inspected = 0

    def new_item(self, item):
        if item > 9699690: # 2*3*5*7*11*13*17*19
            item = item % 9699690
            print("item % 9699690")
        self.items.append(item)

    def round(self, monkeys):
        for item in self.items:
            self.counter_inspected += 1
            worry = int(item)
            if self.operation == "^":
                worry *= int(item)
            elif self.operation == "*":
                worry *= self.operation_number
            elif self.operation == "+":
                worry += self.operation_number
            #worry = worry // 3
            if worry % self.division_by == 0:
                monkeys[self.true_destination].new_item(worry)
            else:
                monkeys[self.false_destination].new_item(worry)
        self.items = []

def solve():
    game = Game()
    with open('input.txt') as f:
        lines = f.readlines()
    start_items = []
    operation = ""
    division_by = 0
    operation_number = 0
    true_destination = -1
    false_destination = -1
    for line in lines:
        line = line.strip()
        if line.startswith("Monkey "):
            continue
        elif line.startswith("Starting items: "):
            line = line.replace("Starting items: ", "")
            start_items = line.split(", ")
        elif line.startswith("Operation:"):
            if "old * old" in line:
                operation = "^"
            else:
                if "*" in line:
                    operation = "*"
                elif "+" in line:
                    operation = "+"
                operation_number = int(line.split(" ")[-1])
        elif line.startswith("Test:"):
            division_by = int(line.split(" ")[-1])
        elif line.startswith("If true:"):
            true_destination = int(line.split(" ")[-1])
        elif line.startswith("If false:"):
            false_destination = int(line.split(" ")[-1])
        else:
            monkey = Monkey(start_items, operation, operation_number, division_by, true_destination, false_destination)
            game.add_monkey(monkey)

    print("Start:")
    game.print()
    for i in range(10000):
        print("Round: " + str(i + 1))
        game.round()
        game.print()
    print(game.monkey_business())

if __name__ == '__main__':
    solve()