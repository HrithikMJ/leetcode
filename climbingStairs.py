from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def findStairs(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return findStairs(n - 1) + findStairs(n - 2)

        return findStairs(n)
