# module for plateau

"""
 Plateau is an object that has bounding coordinates 
 for bottom left and top right with which it is 
 initialized. Additionally it can help check whether
 a given pair of coordinates is within Pleatue or not.
"""


class Plateau:
    def __init__(self, bounding_coordinates):
        self.bound = [bounding_coordinates[0], bounding_coordinates[1],
                      bounding_coordinates[2], bounding_coordinates[3]]

    def is_inside_plateau(self, coordinates):
        x, y = int(coordinates[0]), int(coordinates[1])

        if ((x >= self.bound[0] and y >= self.bound[1]) and
                (x <= self.bound[2] and y <= self.bound[2])):
            return True
        else:
            return False
