# find the max area of rectangle
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] >= height[right]:
                temp = height[right] * (right - left)
                maxArea = temp if temp > maxArea else maxArea
                right -= 1
            elif height[right] > height[left]:
                temp = height[left] * (right - left)
                maxArea = temp if temp > maxArea else maxArea
                left += 1
        return maxArea
