from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]

        for i in range(0,len(s)):
            ch = s[i]
            if not stack:
                if self.isOpposite(ch):
                    return False
                else:
                    stack.append(ch)
            else:
                if self.isOpposite(ch):
                    if self.oppositeOf(stack[len(stack)-1]) == ch:
                        stack.pop()
                    else:
                        return False
                    
                else:
                    stack.append(ch)

        return not stack
    def isOpposite(self, char:chr)->bool:
        if char == ')' or char =='}' or char == ']':
            return True
        return False
    def oppositeOf(self,char:chr) ->chr:
         if char == '(':
            return ')'
         elif char == '{':
            return '}'
         elif char =='[':
            return ']'
         return '' 

sol = Solution()
print(sol.isValid("{}()"))


