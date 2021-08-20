import unittest
from functions import (y_value_for_zones, accuracy_of_scale, get_scale_from_segment, divide_scales, 
                       convert_grad_min_secs_to_decimal, scale_from_size)


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


class TestMapAccurancy(unittest.TestCase):
    def test_accurancy(self):
        self.assertEqual(accuracy_of_scale(10_000), 1)
        self.assertEqual(accuracy_of_scale(1_000), 0.1)
        self.assertEqual(accuracy_of_scale(50_000), 5)
        self.assertEqual(accuracy_of_scale(5_000), 0.5)
        self.assertEqual(accuracy_of_scale(2_000), 0.2)
        self.assertEqual(accuracy_of_scale(25_000), 2.5)
        self.assertEqual(accuracy_of_scale(500), 0.05)
        self.assertEqual(accuracy_of_scale(2_000), 0.2)

    def test_values(self):
        self.assertRaises(ValueError, accuracy_of_scale, 0)
        self.assertRaises(ValueError, accuracy_of_scale, -10000)

    def test_type(self):
        self.assertRaises(TypeError, accuracy_of_scale, [10_000])
        self.assertRaises(TypeError, accuracy_of_scale, (10_000,))
        self.assertRaises(TypeError, accuracy_of_scale, '10_000')
        self.assertRaises(TypeError, accuracy_of_scale, True)
        self.assertRaises(TypeError, accuracy_of_scale, None)
        self.assertRaises(TypeError, accuracy_of_scale, 5j+2)

    
class TestGetScaleFromSegment(unittest.TestCase):
    def test_get_scale_from_segment(self):
        self.assertEqual(get_scale_from_segment('L–35–35–А–а'), '1:25 000')
        self.assertEqual(get_scale_from_segment('ІХ–М–35'), '1:300 000')
        self.assertEqual(get_scale_from_segment('С–3–9'), '1:100 000')
        self.assertEqual(get_scale_from_segment('М–35–4-(2–в)'), '1:2 000')
        self.assertEqual(get_scale_from_segment('М–34–44-(4)'), '1:5 000')
        self.assertEqual(get_scale_from_segment('L–35–3'), '1:100 000')
        self.assertEqual(get_scale_from_segment('М–35-ІХ'), '1:200 000')
        self.assertEqual(get_scale_from_segment('В–4–1–А–в'), '1:25 000')
        self.assertEqual(get_scale_from_segment('М–35–14–А'), '1:50 000')
        self.assertEqual(get_scale_from_segment('А–35-А'), '1:500 000')
        self.assertEqual(get_scale_from_segment('М–5–5-(5–в)'), '1:2 000')
        self.assertEqual(get_scale_from_segment('М–35-ХІІІ'), '1:200 000')
        self.assertEqual(get_scale_from_segment('М–35-Г'), '1:500 000')
        self.assertEqual(get_scale_from_segment('L–35'), '1:1 000 000')
        self.assertEqual(get_scale_from_segment('К–22–4–А–а–4'), '1:10 000')
        self.assertEqual(get_scale_from_segment('М–35–1–Г'), '1:50 000')
        self.assertEqual(get_scale_from_segment('ІІІ–М–35'), '1:300 000')
        self.assertEqual(get_scale_from_segment('М–4–4-(4)'), '1:5 000')

    def test_values(self):
        self.assertRaises(ValueError, get_scale_from_segment, 'М-ХІІІ-35')
        self.assertRaises(ValueError, get_scale_from_segment, 'М–4–4-(4)-ХІІІ-35')
        self.assertRaises(ValueError, get_scale_from_segment, 'A-A-A')

    def test_type(self):
        self.assertRaises(TypeError, get_scale_from_segment, 0)
        self.assertRaises(TypeError, get_scale_from_segment, True)
        self.assertRaises(TypeError, get_scale_from_segment, [0,])
        self.assertRaises(TypeError, get_scale_from_segment, (0,))
        self.assertRaises(TypeError, get_scale_from_segment, set())
        self.assertRaises(TypeError, get_scale_from_segment, tuple())
        self.assertRaises(TypeError, get_scale_from_segment, dict())


class TestDivideScales(unittest.TestCase):
    def test_divide_scale(self):
        self.assertEqual(divide_scales('1 000 000', '200 000',), 36)
        self.assertEqual(divide_scales('1 000 000', '300 000',), 9)
        self.assertEqual(divide_scales('5 000', '2 000',), 9)
        self.assertEqual(divide_scales('1 000 000', '100 000',), 144)
        self.assertEqual(divide_scales('1 000 000', '500 000',), 4)
        self.assertEqual(divide_scales('100 000', '5 000',), 256)
        self.assertEqual(divide_scales('50 000', '25 000',), 4)
        self.assertEqual(divide_scales('100 000', '50 000',), 4)
        self.assertEqual(divide_scales('25 000', '10 000',), 4)

    
    def test_types(self):
        self.assertRaises(TypeError, divide_scales, True, '5 000')
        self.assertRaises(TypeError, divide_scales, '5 000', (1,))
        self.assertRaises(TypeError, divide_scales, 1, '100 000')
        self.assertRaises(TypeError, divide_scales, dict(), '1 000 000')
        self.assertRaises(TypeError, divide_scales, tuple(), 1)

    
    def test_values(self):
        self.assertRaises(ValueError, divide_scales, '0', '1')
        self.assertRaises(ValueError, divide_scales, 'True', 'None')
        self.assertRaises(ValueError, divide_scales, 'set()', 'spam')
        self.assertRaises(ValueError, divide_scales, '[1, 2, 3]', '1')


class TestDegreesToDecimal(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(convert_grad_min_secs_to_decimal('4 00'), 4.00)
        self.assertEqual(convert_grad_min_secs_to_decimal('2 00'), 2.00)
        self.assertEqual(convert_grad_min_secs_to_decimal('1 20'), 1.333)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 40'), 0.667)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 20'), 0.333)
        self.assertEqual(convert_grad_min_secs_to_decimal('6 00'), 6.00)
        self.assertEqual(convert_grad_min_secs_to_decimal('3 00'), 3.00)
        self.assertEqual(convert_grad_min_secs_to_decimal('2 00'), 2.00)
        self.assertEqual(convert_grad_min_secs_to_decimal('1 00'), 1.00)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 30'), 0.50)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 10'), 0.167)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 05'), 0.083)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 02 30'), 0.042)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 15'), 0.25)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 7 30'), 0.125)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 3 45'), 0.062)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 1 15'), 0.021)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 1 52.5'), 0.031)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 0 25'), 0.007)
        self.assertEqual(convert_grad_min_secs_to_decimal('0 0 37.5'), 0.010)


    def test_types(self):
        self.assertRaises(TypeError, convert_grad_min_secs_to_decimal, True)
        self.assertRaises(TypeError, convert_grad_min_secs_to_decimal, None)
        self.assertRaises(TypeError, convert_grad_min_secs_to_decimal, tuple())
        self.assertRaises(TypeError, convert_grad_min_secs_to_decimal, [True])
        self.assertRaises(TypeError, convert_grad_min_secs_to_decimal, 1)

    def test_values(self):
        self.assertRaises(ValueError, convert_grad_min_secs_to_decimal, '5j+1')
        self.assertRaises(ValueError, convert_grad_min_secs_to_decimal, 'spam')

    
class TestSizes(unittest.TestCase):
    def test_size(self):
        self.assertEqual(scale_from_size('0 0 25', '0 0 37.5'), '1:2 000')
        self.assertEqual(scale_from_size('0 02 30', '0 3 45'), '1:10 000')
        self.assertEqual(scale_from_size('0 20 0', '0 30 0'), '1:100 000')

    def test_types(self):
        self.assertRaises(TypeError, False, True)
        self.assertRaises(TypeError, 1, .05)
        self.assertRaises(TypeError, dict(), list())

    def test_values(self):
        self.assertRaises(ValueError, scale_from_size, 'bsifvbd', 'usevo')
        self.assertRaises(ValueError, scale_from_size, '5j+2', '5j+2')
        
        

if __name__ == "__main__":
    unittest.main()
