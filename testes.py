# testes.py
import unittest
from ordenacao import insertion_sort, merge_sort

class TesteOrdenacao(unittest.TestCase):

    def setUp(self):
        self.casos_teste = {
            "lista_vazia": [],
            "um_elemento": [42],
            "elementos_iguais": [7, 7, 7, 7, 7, 7],
            "ja_ordenada": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "lista_invertida": [9, 8, 7, 6, 5, 4, 3, 2, 1],
            "elementos_negativos_e_mistos": [-5, 3, 0, -2, 10, 3, -5],
            "lista_duplicados_aleatorios": [4, 2, 5, 2, 3, 1, 4]
        }

    def test_insertion_sort(self):
        for nome, lista in self.casos_teste.items():
            esperado = sorted(lista)
            resultado, _ = insertion_sort(lista)
            self.assertEqual(resultado, esperado, f"Falha no Insertion Sort para o caso: {nome}")

    def test_merge_sort(self):
        for nome, lista in self.casos_teste.items():
            esperado = sorted(lista)
            resultado, _ = merge_sort(lista)
            self.assertEqual(resultado, esperado, f"Falha no Merge Sort para o caso: {nome}")

if __name__ == "__main__":
    unittest.main()
