import unittest
from ClasePalindromo import Palindromo

class TestPalindromo(unittest.TestCase):
    __palindromo: Palindromo

    def setUp(self):
        self.__palindromo = Palindromo("MENEM")

    def test_esPalind(self):
        self.assertTrue(self.__palindromo.esPalindromo())

    def test_palindromo_con_un_caracter(self):
        self.__palindromo.setPalabra('a')
        self.assertTrue(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra('#')
        self.assertTrue(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra('🖖')
        self.assertTrue(self.__palindromo.esPalindromo())

    def test_palindromo_con_dos_caracteres(self):
        self.__palindromo.setPalabra('ab')
        self.assertFalse(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra('ba')
        self.assertFalse(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra('aa')
        self.assertTrue(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra('🖖🖖')
        self.assertTrue(self.__palindromo.esPalindromo())

    def test_palindromo_con_tres_caracteres(self):
        self.__palindromo.setPalabra('aba')
        self.assertTrue(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra('abb')
        self.assertFalse(self.__palindromo.esPalindromo())

    def test_palindromo_con_cuatro_caracteres(self):
        self.__palindromo.setPalabra('abba')
        self.assertTrue(self.__palindromo.esPalindromo())

        self.__palindromo.setPalabra('abab')
        self.assertFalse(self.__palindromo.esPalindromo())


if __name__ == '__main__':
    unittest.main()
