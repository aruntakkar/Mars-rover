import unittest
from lib.rover import Rover
from lib.plateau import Plateau


class RoverTestCase(unittest.TestCase):

    def test_rover_move(self):
        test_cases = [[5, 5, 'N'], [0, 0, 'S'], [5, 0, 'E'], [0, 0, 'W']]
        cases_expected_results = [[5, 6, 'N'], [
            0, -1, 'S'], [6, 0, 'E'], [-1, 0, 'W']]
        plateau = Plateau([0, 0, 5, 5])

        for count, element in enumerate(test_cases):
            rover = Rover(test_cases[count])
            x, y, direction = rover.get_new_location('M')

            self.assertEqual(cases_expected_results[count], [x, y, direction])

            if plateau.is_inside_plateau([x, y]):
                rover.set_location(x, y, direction)
            self.assertEqual(test_cases[count], [
                rover.x, rover.y, rover.direction])
