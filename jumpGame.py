# Traverse in reverse and move the target near to 0
# eg [2,3,1,1,4], we start from index 4 and value 4 and move 1 step back
# if we reach this we can reach 4, we further move 1 step back if we reach this we can reach the new target 1 , continue this loop
# [3,2,1,0,4], In this example if we try that we cant reach 4 at all


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        a = nums
        target = len(a) - 1
        i = 0
        for i in range(len(a) - 1, -1, -1):
            print(i, a[i])
            if a[i] + i >= target:
                target = i
                print("ch", target)
        return True if target == 0 else False
