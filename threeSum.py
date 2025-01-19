# 2 ptr or hashmap, fix a element and convert the problem to a twosum
# i struggled to find the stop condition, overcomplicated things a bit by trying to pop
# later i found out i could just move my left pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        for i in range(len(nums)):
            if i + 1 == len(nums) or (i > 0 and nums[i - 1] == nums[i]):
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = nums[right] + nums[left]
                if (temp + nums[i]) == 0:
                    final.append([nums[i], nums[right], nums[left]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif (temp + nums[i]) > 0:
                    right = right - 1
                elif (temp + nums[i]) < 0:
                    left = left + 1
        return final
