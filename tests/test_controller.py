import unittest
from lib.controller import Controller


class ControllerTestCase(unittest.TestCase):
    plateaubounds = (0, 0, 5, 5)
    path = './test_input.txt'

    def test_controller_init(self):
        controller = Controller(ControllerTestCase.path)
        self.assertEqual(ControllerTestCase.plateaubounds, (controller.x_plateau_lower,
                                                            controller.y_plateau_lower,
                                                            controller.x_plateau_upper,
                                                            controller.y_plateau_upper))
