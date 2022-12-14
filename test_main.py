"""Unit test pro číselné soustavy."""
from main import reminders
from main import system
import unittest


class Test(unittest.TestCase):
    """Třída pro Unit testy."""

    if system == 2:
        def test_binOcta(self):
            """Test funkce binOcta pro číslo 5 do dvojkouvé soustavy."""
            self.assertEqual(reminders, [1, 0, 1])

    elif system == 8:
        def test_binOcta(self):
            """Test funkce binOcta pro číslo 14 do osmičkové soustavy."""
            self.assertEqual(reminders, [1, 6])

    elif system == 16:
        def test_sixteenth(self):
            """Test funkce sixteenth pro číslo 23 do šestnástkové soustavy."""
            self.assertEqual(reminders, [1, 7])


if __name__ == '__main__':
    unittest.main()
