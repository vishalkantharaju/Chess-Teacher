#!/usr/bin/env python3
import os
import sys
import unittest

from ArmMovement.xarm import XArmAPI

class UnitTests(unittest.TestCase):

    def setup():
        pass


class SystemTests(unittest.TestCase):

    def setup():
        pass


class GizzmoIntegrationTests(unittest.TestCase):

    def setup():
        pass


if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

    unittest.main()
