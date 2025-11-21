# Можно улучшить:
# 1. Заменить импорт roman на функцию, это сторонняя библиотека, лучше без неё
# 2. Проверку на палиндром переписать, можно уменьшить количество строк
import roman

class RomanNums:
    def __init__(self, nums):
        self.nums = nums

    def from_roman(self):
        return roman.fromRoman(self.nums)

    def is_palindrome(self):
        a = str(roman.fromRoman(self.nums))
        b = str(roman.fromRoman(self.nums))
        c = b[::-1]
        return a == c