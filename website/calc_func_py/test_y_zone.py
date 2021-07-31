import unittest
from functions_for_calc import y_value_for_zones


class TestYValueForZones(unittest.TestCase):
    def test_y_value(self):
        self.assertEqual(y_value_for_zones(4, 333_333, 'захід'), 4_166_667)
        self.assertEqual(y_value_for_zones(5, 222_555, 'схід'), 5_722_555)
        self.assertEqual(y_value_for_zones(3, 188_155, 'схід'), 3_688_155)
        self.assertEqual(y_value_for_zones(45, 184_326, 'захід'), 15_315_674)
        self.assertEqual(y_value_for_zones(35, 184_326, 'захід'), 5_315_674)
        self.assertEqual(y_value_for_zones(4, 311_311, 'захід'), 4_188_689)
        self.assertEqual(y_value_for_zones(45, 184_326, 'схід'), 15_684_326)

    def test_values(self):
        self.assertRaises(ValueError, y_value_for_zones, -4, -333_333, 'захід')
        self.assertRaises(ValueError, y_value_for_zones, 4, -333_333, '1')
        self.assertRaises(ValueError, y_value_for_zones, 4, 0, 'захід')

    def test_type(self):
        self.assertRaises(TypeError, y_value_for_zones, "4", "333_333", 'захід')
        self.assertRaises(TypeError, y_value_for_zones, True, "333_333", None)
        self.assertRaises(TypeError, y_value_for_zones, ["4", ], ("333_333",), 'захід')
        self.assertRaises(TypeError, y_value_for_zones, ["4", ], 5j+2, 'захід')


if __name__ == "__main__":
    unittest.main()
