from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
          if nums[i] == 0:
            nums.remove(nums[i])
            nums.append(0)
        print(nums)
        

sol_1 = Solution()
print(sol_1.moveZeroes([0,1,0,3,12]))