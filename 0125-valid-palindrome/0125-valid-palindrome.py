class Solution:
    def isPalindrome(self, s: str):
      strr = []
      for i in s:
        if not i.isalnum():
          continue
        strr.append(i.lower())
      if strr == strr[::-1]:
        return True
      return False
      
      
sol_1 = Solution()
print(sol_1.isPalindrome(' '))