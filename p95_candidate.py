"""Исправленный кандидат. Использует nearest-rank и math.ceil по контракту."""
import math

def p95(values):
    if not isinstance(values, list) or not values:
        raise ValueError("Нужен непустой список")
    if any(isinstance(x, bool) or not isinstance(x, (int, float))
           or (isinstance(x, float) and not math.isfinite(x)) or x < 0 for x in values):
        raise ValueError("Нужны конечные неотрицательные числа")
    
    # Сортируем значения, не меняя исходный список
    ordered = sorted(values)
    
    # По контракту SPEC.md: ранг k = ceil(0.95 * N)
    # Используем math.ceil для строгого округления вверх.
    # max(1, ...) защищает от нулевого индекса на всякий случай (хотя для N>0 ceil(0.95*N) >= 1)
    rank = max(1, math.ceil(0.95 * len(ordered)))
    
    # Индексация в Python с 0, поэтому вычитаем 1
    return ordered[rank - 1]