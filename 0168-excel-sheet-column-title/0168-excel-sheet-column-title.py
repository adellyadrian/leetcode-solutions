class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
      string = ""
      while columnNumber > 0:
          columnNumber, remainder = divmod(columnNumber - 1, 26)
          string = chr(65 + remainder) + string
      return string

sol_1 = Solution()
print(sol_1.convertToTitle(28))