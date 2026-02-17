from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
          return nums[i]
          

        
sol_1 = Solution()
print(sol_1.singleNumber([1]))