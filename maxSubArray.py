# max sub array
# my initial solution was to find the subarray till the last value
# eg [-2,1,-3,4,-1,2,1,-5,4], my sol was 4-4
# but this isn't right, the correct ans is[4,-1,2,1]
# the sub array should stop at the maximum value
# so i used a 2ptr approach
# maxVal holds the best ever value
# maxEnd checks all the best values


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal = nums[0]
        maxEnd = nums[0]
        for i in range(1, len(nums)):
            maxEnd = max(maxEnd + nums[i], nums[i])
            maxVal = max(maxEnd, maxVal)
        return maxVal
