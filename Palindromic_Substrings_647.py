class Solution:
    def countSubstrings(self, s: str) -> int:
        """ dp, 画表法，類似https://leetcode-cn.com/problems/palindromic-substrings/solution/shou-hua-tu-jie-dong-tai-gui-hua-si-lu-by-hyj8/
        https://leetcode-cn.com/problems/palindromic-substrings/solution/liang-dao-hui-wen-zi-chuan-de-jie-fa-xiang-jie-zho/
        https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns#Minimum-(Maximum)-Path-to-Reach-a-Target
        解释遍历顺序：https://leetcode-cn.com/problems/palindromic-substrings/solution/dai-ma-sui-xiang-lu-dai-ni-xue-tou-dpzi-vidge/
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for j in range(n):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = True
                    count += 1
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                elif j - i > 1 and dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
        return count


class Solution1:
    def countSubstrings(self, s: str) -> int:
        """ 中心拓展 lei-yu-xiao-hong
        泪雨潇虹comment : https://leetcode-cn.com/problems/palindromic-substrings/solution/hui-wen-zi-chuan-by-leetcode-solution/ 
        https://leetcode-cn.com/problems/palindromic-substrings/solution/jian-dan-de-dong-tai-gui-hua-si-xiang-by-tinylife/
        """
        n = len(s)
        res = 0
        def expand(j, k):
            counter = 0
            while j >= 0 and k < n:
                if s[j] == s[k]:
                    counter += 1
                else:
                    return counter
                j -= 1
                k += 1
            return counter
        for i in range(n):
            res += expand(i, i)
            res += expand(i, i + 1)
        return res
