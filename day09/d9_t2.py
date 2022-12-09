def sign(number):
    # no sign() in Python ... why!
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0

class Element:

    def __init__(self):
        self.positions = set()
        self.x = 0
        self.y = 0

    def move_to_position(self, new_x, new_y):
        new_position_identifier = "" + str(new_x) + "," + str(new_y)
        self.x = new_x
        self.y = new_y
        self.positions.add(new_position_identifier)

    def count_positions_discovered(self):
        return len(self.positions)

    def move_to_direction(self, direction):
        if direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "U":
            self.y -= 1
        elif direction == "D":
            self.y += 1

    def x_distance(self, other_element):
        return other_element.x - self.x

    def y_distance(self, other_element):
        return other_element.y - self.y

    def move_after(self, element_to_track):
        distance_x = self.x_distance(element_to_track)
        distance_y = self.y_distance(element_to_track)
        move_to_x = 0
        move_to_y = 0
        if abs(distance_x) == 2:
            move_to_x = sign(distance_x)
            if abs(distance_y) == 1:
                move_to_y = sign(distance_y)
        if abs(distance_y) == 2:
            move_to_y = sign(distance_y)
            if abs(distance_x) == 1:
                move_to_x = sign(distance_x)
        self.move_to_position(self.x + move_to_x, self.y + move_to_y)

class Rope:

    def __init__(self):
        self.positions = []
        for i in range(10):
            position = Element()
            self.positions.append(position)

    def head(self):
        return self.positions[0]

    def tail(self):
        return self.positions[9]

    def move_head(self, direction, steps):
        for step in range(steps):
            self.head().move_to_direction(direction)
            for i in range(1, 10, 1):
                self.positions[i].move_after(self.positions[i - 1])

def solve():
    rope = Rope()
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        command = line.split(" ")
        rope.move_head(command[0], int(command[1]))
    print(rope.tail().count_positions_discovered())

if __name__ == '__main__':
    solve()
