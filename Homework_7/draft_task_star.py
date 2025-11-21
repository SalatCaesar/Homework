import roman

class RomanNums:
    def __init__(self, nums):
        self.nums = nums

    def from_roman(self):
        return roman.fromRoman(self.nums)

    def is_palindrome(self):
        def is_palindrome(self):
            a = str(roman.fromRoman(self.nums))
            b = str(roman.fromRoman(self.nums))
            c = b[::-1]
            return a == c