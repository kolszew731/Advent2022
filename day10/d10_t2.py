class Crt:

    def __init__(self):
        self.lines = []
        self.crt_counter = 0

    def clock(self, register_value):
        crt_line_index = self.crt_counter // 40
        if len(self.lines) < crt_line_index + 1:
            self.lines.append([])
        crt_index_in_line = self.crt_counter % 40
        sprite_middle_position = register_value % 40
        if (
            (crt_index_in_line == sprite_middle_position or
            crt_index_in_line == sprite_middle_position - 1 or
            crt_index_in_line == sprite_middle_position + 1)):
           self.lines[crt_line_index].append("#")
        else:
            self.lines[crt_line_index].append(".")
        self.crt_counter += 1

    def print(self):
       for line in  self.lines:
           for p in line:
               print(p, end="")
           print("")


class Processor:

    def __init__(self):
        self.cycles = []
        self.crt = Crt()

    def instruction(self, line):
        splitted = line.split(" ")
        command = splitted[0]
        curreent_value = 1
        if len(self.cycles) != 0:
            curreent_value = self.cycles[-1]
        self.crt.clock(curreent_value)
        if command == "noop":
            self.cycles.append(curreent_value)
        else:
            self.cycles.append(curreent_value)
            self.crt.clock(curreent_value)
            new_value = int(splitted[1])
            self.cycles.append(curreent_value + new_value)

    def print_crt(self):
        self.crt.print()

def solve():
    processor = Processor()
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        processor.instruction(line)
    processor.print_crt()

if __name__ == '__main__':
    solve()