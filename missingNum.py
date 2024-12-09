# missing number


# initially i went with xor'ng my way into finding the missing number
# but i also came across another intersting solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] ^ i:
                return i
        return i + 1


# solution 2
# this method uses (n*(n+1))//2 to find the value of first n natural numbers
# and subtracts values in nums finally ariving at conclusion
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = (len(nums) * (len(nums) + 1)) // 2
        for i in range(len(nums)):
            sum -= nums[i]
        return sum
