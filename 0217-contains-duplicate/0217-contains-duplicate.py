from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        else: 
            return False

sol_1 = Solution()
print(sol_1.containsDuplicate([3,1]))