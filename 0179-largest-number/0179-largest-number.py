from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        nums_str.sort(key=lambda x: x * 10, reverse=True)
        result = ''.join(nums_str)
        if result[0] == '0':
            return '0'
        return result


sol_1 = Solution()
print(sol_1.largestNumber([3, 30, 34, 5, 9]))
