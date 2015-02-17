

class Solution:
    def isValid(self, s: str) -> bool:
        """ 我自己的答案 不是很efficeint """
        s_list = list(s)
        prentheses_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        i = 1
        while i < len(s_list):
            if s_list[i] in prentheses_map and prentheses_map[s_list[i]] == s_list[i - 1]:
                s_list.pop(i)
                s_list.pop(i - 1)
                i = 1
            else:
                i += 1
        return not s_list


class Solution2:
    def isValid(self, s: str) -> bool:
        """
        https://leetcode-cn.com/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode-solution/
        时间复杂度：O(n) 其中 n 是字符串 s的长度。

        空间复杂度：O(n)

        """
        stack = []
        prentheses_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for ch in s:
            if ch not in prentheses_map:
                stack.append(ch)
            else:
                if not stack or prentheses_map[ch] != stack.pop():
                    return False
        return not stack
