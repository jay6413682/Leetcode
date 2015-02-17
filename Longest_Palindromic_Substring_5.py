""" https://leetcode.com/problems/longest-palindromic-substring/solution/ """


def longest_common_substring(s1: str, s2: str) -> str:
    """ https://zhuanlan.zhihu.com/p/68409952
    similar to https://leetcode-cn.com/problems/longest-common-subsequence/solution/dong-tai-gui-hua-zhi-zui-chang-gong-gong-zi-xu-lie/
    prefix empty char to every string
    未优化
    时间复杂度：两层循环 O(n²)O(n²)。

    空间复杂度：一个二维数组 O(n²)O(n²)。
    """
    i = 0
    j = 0
    s1n = len(s1)
    s2n = len(s2)
    # Unfortunately shortening this to something like 5*[5*[0]] doesn't really work because you end up with 5 copies of the same list, so when you modify one of them they all change
    table = [[0] * (s1n + 1) for _ in range(s2n + 1)]
    lcs = ''
    while i <= s1n:
        j = 0
        while j <= s2n:
            if i == 0 or j == 0:
                table[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                # the if statement below is only needed for this particular case
                # check https://leetcode-cn.com/problems/longest-palindromic-substring/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-bao-gu/
                # 解法 2: 最长公共子串
                if s2n - (j - 1) - 1 + table[i][j] - 1 == i - 1:
                    raw_lcs = s2[j - table[i][j] : j]
                    lcs = raw_lcs if len(raw_lcs) > len(lcs) else lcs
            else:
                table[i][j] = 0
            j += 1
        i += 1
    return lcs


def is_palindrome(s: str) -> bool:
    i = 0
    n = len(s)
    while i < n // 2:
        if s[i] != s[n - 1 - i]:
            return False
        i += 1
    return True


class Solution(object):

    def expand_from_center(self, s: str, left: int, right: int) -> tuple:
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindromeFour(self, s: str) -> str:
        """ https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/ """
        start = end = 0
        n = len(s)
        for i in range(n):
            left1, right1 = self.expand_from_center(s, i, i)
            left2, right2 = self.expand_from_center(s, i, i + 1)
            end, start = (right1, left1) if (right1 - left1 > end - start) else (end, start)
            end, start = (right2, left2) if (right2 - left2 > end - start) else (end, start)
        return s[start: end + 1]

    def longestPalindromeThree(self, s: str) -> str:
        """ check https://leetcode-cn.com/problems/longest-palindromic-substring/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-bao-gu/ """
        n = len(s)
        i = n - 1
        reversed_s = ''
        while i >= 0:
            reversed_s += s[i]
            i -= 1
        return longest_common_substring(s, reversed_s)

    def longestPalindromeOne(self, s: str) -> str:
        """
        Brutal Force: Time complexity : O(n3).
        Space complexity :  O(1). 
        """
        longest_p_substr = ''
        n = len(s)
        b = 0
        e = 0
        while b < n:
            e = b
            while b <= e <= n:
                if is_palindrome(s[b : e]):
                    longest_p_substr = s[b:e] if len(s[b:e]) > len(longest_p_substr) else longest_p_substr
                e += 1
            b += 1
        return longest_p_substr

    def longestPalindromeTwo(self, s: str) -> str:
        """ Dynamic programming, 动态规划: https://leetcode-cn.com/problems/longest-palindromic-substring/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-bao-gu/
        优化过，但不是空间最优化解法，但是好理解，不要看空间最优化解法了，不好理解
        This gives us a runtime complexity of O(n2) and uses O(n2) space to store the table.
        """
        n = len(s)
        table = []
        for i in range(n):
            table.append(n * [None])
        i = n - 1
        longest_p_substr = ''
        while i >= 0:
            j = i
            while n > j >= i:
                if i == j:
                    table[i][j] = True
                elif j == i + 1:
                    table[i][j] = (s[i] == s[j])
                else:
                    table[i][j] = (table[i + 1][j - 1] and s[i] == s[j])
                if table[i][j]:
                    longest_p_substr = s[i : j + 1] if len(s[i : j + 1]) >= len(longest_p_substr) else longest_p_substr
                j += 1
            i -= 1
        return longest_p_substr
