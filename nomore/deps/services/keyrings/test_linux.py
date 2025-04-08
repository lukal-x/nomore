import unittest

from . import get_password


class TestLinux(unittest.TestCase):

    def test_setter(self) -> None:
        """?"""
        pass

    def test_getter(self) -> None:
        """?"""
        got = get_password("lorem", "ipsum")
        print(got)
        self.assertTrue(False)
