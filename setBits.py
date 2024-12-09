class Solution:
    def hammingWeight(self, n: int) -> int:
        return len(f"{n:b}".replace("0", ""))
