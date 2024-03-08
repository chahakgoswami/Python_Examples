class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s ==None or len(s) ==0:
            return 0
        wordSet = set()
        left =0
        right =1
        n = len(s)
        wordSet.add(s[0])
        max_len = 0
        while(right< n):
            if s[right] not in wordSet:
               wordSet.add(s[right]) 
               right+=1
               max_len = max(len(wordSet),max_len)
            else:
                wordSet.remove(s[left])
                left+=1

        return max_len


sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))


