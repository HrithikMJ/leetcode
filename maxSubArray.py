# max sub array
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal = nums[0]
        maxEnd = nums[0]
        for i in range(1, len(nums)):
            maxEnd = max(maxEnd + nums[i], nums[i])
            maxVal = max(maxEnd, maxVal)
        return maxVal
