import unittest
from lib.plateau import Plateau


class PlateauTestCase(unittest.TestCase):

    def test_is_inside_plateau(self):
        coordinates = [2, 2]
        bounds = [0, 0, 5, 5]
        plateau_object = Plateau(bounds)
        self.assertTrue(plateau_object.is_inside_plateau(coordinates))

    def test_with_valid_input(self):
        coordinates = [5, 5]
        bounds = [0, 0, 5, 5]
        plateau_object = Plateau(bounds)
        self.assertTrue(plateau_object.is_inside_plateau(coordinates))

    def test_with_invalid_input(self):
        coordinates = [-5, 5]
        bounds = [0, 0, 5, 5]
        plateau_object = Plateau(bounds)
        self.assertFalse(plateau_object.is_inside_plateau(coordinates))
