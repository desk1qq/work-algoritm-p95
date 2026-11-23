"""Добавьте собственные тесты. Ожидания получите независимо от кандидата."""
import unittest
from starter.p95_candidate import p95

class StudentChecks(unittest.TestCase):
    
    # 1. Граница ранга (на 20 элементах 0.95 * 20 = 19, берем 19-й)
    def test_boundary_rank_20(self):
        data = list(range(1, 21))  # от 1 до 20
        # 0.95 * 20 = 19.0, ceil(19.0) = 19. Элемент с индексом 18 (19-й по счету) это 19.
        self.assertEqual(p95(data), 19)

    # 2. Граница ранга на 11 элементах (0.95 * 11 = 10.45, ceil = 11)
    def test_boundary_rank_11(self):
        data = list(range(10, 111, 10))  # 10, 20, ..., 110
        # 0.95 * 11 = 10.45, ceil(10.45) = 11. Берем 11-й элемент (индекс 10) это 110.
        self.assertEqual(p95(data), 110)

    # 3. Дубликаты и перемешанный список
    def test_unsorted_duplicates(self):
        data = [50, 10, 50, 20, 50, 30, 50, 40, 50, 50]
        # 0.95 * 10 = 9.5, ceil = 10. Берем 10-й элемент (максимальный) = 50
        self.assertEqual(p95(data), 50)

    # 4. Неверный вход
    def test_invalid_inputs(self):
        for bad in ([], [-5], [float("nan")], [float("inf")], [True], ["string"]):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    p95(bad)

    # 5. Исходный список не меняется
    def test_original_list_unchanged(self):
        data = [5, 1, 3, 2, 4]
        old_data = data.copy()
        p95(data)
        self.assertEqual(data, old_data)

if __name__ == "__main__":
    unittest.main()