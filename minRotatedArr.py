# min in rotated sorted arr
# binary search
# follow pattern in which order its decreasing and search in that way
# eg [4,5,6,7,0,1,2] in this array 7 is the mid value 7 > 4 so we have to search in its left half
# eg [5,1,2,3,4] in this array 2 is the mid value 2 < 5 so we have to search in the right half
class Solution:
    def findMin(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        minV = nums[0]

        if nums[mid] >= nums[0]:
            for i in range(mid, len(nums)):
                if minV > nums[i]:
                    minV = nums[i]
        else:
            for i in range(0, mid + 1):
                if minV > nums[i]:
                    minV = nums[i]
        return minV
