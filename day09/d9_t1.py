def sign(number):
    # no sign() in Python ... why!
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0

class Position:

    def __init__(self):
        self.__positions = set()
        self.x = 0
        self.y = 0
        self.move_to_pos(0, 0)

    def move_to_pos(self, new_x, new_y):
        new_position_key = "" + str(new_x) + "," + str(new_y)
        self.__positions.add(new_position_key)
        self.x = new_x
        self.y = new_y

    def count_positions_discovered(self):
        return len(self.__positions)

    def move_to(self, direction):
        if direction == "R":
            self.x += 1
        elif direction == "L":
            self.x -= 1
        elif direction == "U":
            self.y -= 1
        elif direction == "D":
            self.y += 1

    def x_distance(self, other_position):
        return other_position.x - self.x

    def y_distance(self, other_position):
        return other_position.y - self.y

    def move_after(self, position_to_track):
        distance_x = self.x_distance(position_to_track)
        distance_y = self.y_distance(position_to_track)
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
        self.move_to_pos(self.x + move_to_x, self.y + move_to_y)


class Rope:
    __head_position = Position()
    __tail_position = Position()

    def move_head(self, direction, steps):
        for step in range(steps):
            self.__head_position.move_to(direction)
            self.__tail_position.move_after(self.__head_position)

    def count_positions_discovered_by_tail(self):
        return self.__tail_position.count_positions_discovered()


def solve():
    rope = Rope()
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        command = line.split(" ")
        rope.move_head(command[0], int(command[1]))
    print(rope.count_positions_discovered_by_tail())

if __name__ == '__main__':
    solve()
