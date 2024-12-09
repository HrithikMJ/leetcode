# prefix and sufix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fin = [1] * len(nums)
        i = 0
        mult = 1
        for i in range(len(nums)):
            if i - 1 < 0:
                continue
            else:
                fin[i] = fin[i - 1] * nums[i - 1]

        for i in range(i, -1, -1):
            if i + 1 > len(nums) - 1:
                continue
            else:
                mult = mult * nums[i + 1]
                fin[i] = fin[i] * mult
        return fin
