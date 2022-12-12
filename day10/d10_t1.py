class Processor:

    def __init__(self):
        self.cycles = []

    def instruction(self, line):
        splitted = line.split(" ")
        command = splitted[0]
        curreent_value = 1
        if len(self.cycles) != 0:
            curreent_value = self.cycles[-1]
        if command == "noop":
            self.cycles.append(curreent_value)
        else:
            self.cycles.append(curreent_value)
            new_value = int(splitted[1])
            self.cycles.append(curreent_value + new_value)

    def signal_strength(self):
        sum_signal = 0
        for i in range(19, 220, 40):
            signal = self.cycles[i - 1] * (i + 1)
            sum_signal += signal
        return sum_signal

def solve():
    processor = Processor()
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        processor.instruction(line)
    print(processor.signal_strength())

if __name__ == '__main__':
    solve()