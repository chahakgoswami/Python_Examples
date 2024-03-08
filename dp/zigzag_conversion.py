from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        charMap = {}
        count = 1
        isUp = False
        output = ""

        for i in range(0, len(s)):
            ch = s[i]
            if count in charMap.keys():
                list = charMap.get(count)
                list.append(ch)
                charMap[count] = list
            else:

                list = []
                list.append(ch)
                charMap[count] = list
            if not isUp:
                count += 1
            else:
                count -= 1

            if count == numRows:
                isUp = True
            elif count == 1:
                isUp = False

        for key in charMap.keys():
            charMap[key]
            for i in range(0, len(charMap[key])):
                output += (charMap[key][i])

        return output


sol = Solution()

print(sol.convert("PAYPALISHIRING", 3))
