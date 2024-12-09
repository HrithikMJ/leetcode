# use the previous setBits for easy calculation
# eg 9 -> 1001 [9]
# 9>>1 -> 0100 [4]
# we already calculated set bits for 4 use that and add +1 if its a odd number


class Solution:
    def countBits(self, n: int) -> List[int]:
        a = [0] * (n + 1)
        for i in range(n + 1):
            a[i] = a[i >> 1] + (i & 1)
        return a
