# hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        # for i in range(len(nums)):
        for i in range(len(nums)):

            # a = map.get(target - nums[i])
            if (target - nums[i]) in map:
                return [i, map[target - nums[i]]]
            map[nums[i]] = i
