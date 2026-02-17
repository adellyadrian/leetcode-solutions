class Solution:
    def lengthOfLastWord(self, param1: str) -> int:
        for i in param1:
            param1 = param1.split()
            return len(param1[-1])
    
    
sol_1 = Solution()
print(sol_1.lengthOfLastWord('Hello World'))