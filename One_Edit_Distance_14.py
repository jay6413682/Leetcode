class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        """ Dynamic Programming solution (not recommended): O(n2) runtime, O(n2) space
        https://leetcode-cn.com/problems/edit-distance/solution/edit-distance-by-ikaruga/ """
        n = len(s)
        m = len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        i = 0
        while i <= n:
            j = 0
            while j <= m:
                if i == j == 0:
                    dp[i][j] = 0
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min([dp[i - 1][j - 1] + 1,  dp[i][j - 1] + 1, dp[i - 1][j] + 1])
                j += 1
            i += 1
        return dp[n][m] == 1

    def isOneEditDistanceOne(self, s, t):
        """ O(n) runtime, O(1) space – Simple one-pass:
        solution from the book
        """
        n = len(s)
        m = len(t)
        i = 0
        j = 0
        k = 0
        diff_count = 0

        if abs(n - m) > 1:
            return False
        elif n == m:
            if n == 0:
                return False
            while i < n:
                if s[i] != t[i]:
                    diff_count += 1
                    if diff_count > 1:
                        return False
                i += 1
            if diff_count == 1:
                return True
            return False
        else:
            small, large = (s, t) if n < m else (t, s)
            while j < len(small):
                if small[j] != large[k]:
                    k += 1
                    if k != j + 1:
                        return False
                j += 1
                k += 1
        return True
