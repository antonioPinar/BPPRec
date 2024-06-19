import unittest
from bpppCalculadora import validar_positivo, area_circulo, area_triangulo, area_cuadrado, volumen_cubo

class TestCalculadora(unittest.TestCase):

    def test_validar_positivo(self):
        self.assertTrue(validar_positivo(5))
        self.assertTrue(validar_positivo(3.14))
        self.assertFalse(validar_positivo(-1))
        self.assertFalse(validar_positivo(0))
        with self.assertRaises(ValueError):
            validar_positivo("no_numero")
    
    def test_area_circulo(self):
        self.assertAlmostEqual(area_circulo(1), 3.141592653589793)
        self.assertAlmostEqual(area_circulo(2), 12.566370614359172)
        with self.assertRaises(ValueError):
            area_circulo(-1)
        with self.assertRaises(ValueError):
            area_circulo("no_numero")
    
    def test_area_triangulo(self):
        self.assertAlmostEqual(area_triangulo(3, 6), 9.0)
        self.assertAlmostEqual(area_triangulo(5, 10), 25.0)
        with self.assertRaises(ValueError):
            area_triangulo(-3, 6)
        with self.assertRaises(ValueError):
            area_triangulo(3, "no_numero")
    
    def test_area_cuadrado(self):
        self.assertAlmostEqual(area_cuadrado(2), 4.0)
        self.assertAlmostEqual(area_cuadrado(5), 25.0)
        with self.assertRaises(ValueError):
            area_cuadrado(-2)
        with self.assertRaises(ValueError):
            area_cuadrado("no_numero")
    
    def test_volumen_cubo(self):
        self.assertAlmostEqual(volumen_cubo(2), 8.0)
        self.assertAlmostEqual(volumen_cubo(3), 27.0)
        with self.assertRaises(ValueError):
            volumen_cubo(-2)
        with self.assertRaises(ValueError):
            volumen_cubo("no_numero")

if __name__ == '__main__':
    unittest.main()
