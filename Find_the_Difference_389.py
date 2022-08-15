class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # bit manipulation https://leetcode.cn/leetbook/read/leetcode-cookbook/5c7vu1/
        x = s + t
        res = 0
        for c in x:
            res ^= ord(c)
        return chr(res)
