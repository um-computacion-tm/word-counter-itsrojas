import unittest

from trabajo_contar_letras import contar_letras
from trabajo_contar_palabras import count_words

class TestCountLetters(unittest.TestCase):

    def test_simple(self):
        result = contar_letras('a')
        self.assertEqual(result, {'a': 1})

    def test_complex(self):
        result = contar_letras('hola')
        self.assertEqual(
            result,
            {
                'h': 1,
                'o': 1,
                'l': 1,
                'a': 1,
            }
        )

    def test_super_complex(self):
        result = contar_letras('hola chau')
        self.assertEqual(
            result,
            {
                'h': 2,
                'o': 1,
                'l': 1,
                'a': 2,
                ' ': 1,
                'c': 1,
                'u': 1
            }
        )

class TestCountWords(unittest.TestCase):

    def test_simple(self):
        result = count_words('hola')
        self.assertEqual(result, {'hola': 1})

    def test_complex(self):
        result = count_words('Hola como estas hola')
        self.assertEqual(
            result,
            {
                'hola': 2,
                'como': 1,
                'estas': 1,
            },
        )



if __name__ == '__main__':
    unittest.main()