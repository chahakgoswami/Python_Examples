def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        lcs_matrix = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    lcs_matrix[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    lcs_matrix[i][j] = 1 + lcs_matrix[i - 1][j - 1]
                else:
                    lcs_matrix[i][j] = max(lcs_matrix[i - 1][j], lcs_matrix[i][j - 1])

        return lcs_matrix[n][m]
        
