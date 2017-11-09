# module for rovers

"""
Rover class that has attributes:- x, y, direction

get_new_location:- returns possible coordinates & direction
coordinates still need to be checked whether it is inside plateau.

set_location will set new location of rover on plateau.

"""


class Rover:
    def __init__(self, args):
        self.x, self.y, self.direction = int(args[0]), int(args[1]), args[2]
        self.possible_moves = ['L', 'R', 'M']
        self.log_of_positions = [[args[0], args[1], args[2]]]

    def get_new_location(self, step):
        left_rotate_dict = {'N': 'W', 'S': 'E', 'E': 'N', 'W': 'S'}
        right_rotate_dict = {'N': 'E', 'S': 'W', 'E': 'S', 'W': 'N'}
        move_dict = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
        if step == 'M':
            x = move_dict[self.direction][0] + self.x
            y = move_dict[self.direction][1] + self.y
            direction = self.direction
        elif step == 'L':
            x, y = self.x, self.y
            direction = left_rotate_dict[self.direction]
        elif step == 'R':
            x, y = self.x, self.y
            direction = right_rotate_dict[self.direction]
        else:
            return self.x, self.y, self.direction
        return x, y, direction

    def set_location(self, x, y, direction):
        self.x, self.y, self.direction = x, y, direction
        self.log_of_positions.append([self.x, self.y, self.direction])
