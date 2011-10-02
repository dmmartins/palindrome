from palindrome import palindrome
from palindrome import numero_de_palindromes
import unittest

class TestaPalindrome(unittest.TestCase):
    def testa_palindrome_osso(self):
        self.assertEqual(True, palindrome('osso'))

    def testa_palindrome_abc(self):
        self.assertEqual(False, palindrome('abc'))

    def testa_numero_de_palindromes_aaxyx(self):
        self.assertEqual(2, numero_de_palindromes('aaxyx'))

    def testa_numero_de_palindromes_axa(self):
        self.assertEqual(1, numero_de_palindromes('axa'))

    def testa_numero_de_palindromes_xyzyyx(self):
        self.assertEqual(4, numero_de_palindromes('xyzyyx'))

    def testa_numero_de_palindromes_bbabcbbaab(self):
        self.assertEqual(4, numero_de_palindromes('bbabcbbaab'))

if __name__ == '__main__':
    unittest.main()

