class Solution:
    def isHappy(self, n: int, seen=None) -> bool:
        if seen is None:
            seen = set()
            
        if n == 1:
            return True
            
        if n in seen:
            return False
            
        seen.add(n)
        
        adding = sum(int(digit) ** 2 for digit in str(n))
        return self.isHappy(adding, seen)   

sol_1 = Solution()
print(sol_1.isHappy(2))
