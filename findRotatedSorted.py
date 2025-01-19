a = [5, 1, 3]
a = [6, 7, 1, 2, 3, 4, 5]
a = [4, 5, 6, 7, 0, 1, 2]
a = [1, 3, 5]
a = [2, 3, 4, 5, 6, 7, 8, 9, 1]

mid = len(a) // 2
midV = a[mid]
tar = 9
ans = -1

## if mid is greater than target search left if and only if target is less than a[0] else search right
print(mid, a[mid], a[0], tar)


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
