# binary addition
class Solution:
    def getSum(self, a: int, b: int) -> int:
        intmax = 2147483647
        while (b & intmax) != 0:
            carry = a & b
            carry = carry << 1
            a = a ^ b
            b = carry
        return a & intmax if b > 0 else a
