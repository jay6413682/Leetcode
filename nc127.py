class Solution:
    """ dp，longest common substring: https://www.nowcoder.com/practice/f33f5adc55f444baa0e0ca87ad8a6aac
    类似 https://zhuanlan.zhihu.com/p/68409952 （求所有substring，本题只有一个）
    输出最长公共子串很简单，只需要判断table[i][j]是否等于最长公共子串的长度即可，然后沿着对角线往左上角找大于等于1的数字即可；

    如果table[i][j] == lcs_len（lcs_len指最长公共子串长度），则把这个字符放入LCS中，并跳入table[i-1][j-1]中继续进行判断；
    直到table[i][j] < 1为止；倒序输出LCS放入set中。
    """
    def LCS(self , str1: str, str2: str) -> str:
        # write code here
        n = len(str1)
        m = len(str2)
        max_len = 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[j - 1] == str2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
        # print(dp)
        res = ''
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if dp[i][j] == max_len:
                    ii = i
                    jj = j
                    while dp[ii][jj] > 0:
                        res = str1[jj - 1] + res
                        ii -= 1
                        jj -= 1
                    return res
