class Solution:
    def hammingWeight(self, n: int) -> int:
        # bit manipulation, https://leetcode.cn/problems/number-of-1-bits/solution/wei-1de-ge-shu-by-leetcode-solution-jnwf/ 
        # solution 1:
        res = 0
        while n > 0:
            res += n & 1
            n >>= 1
        return res
        # solution 2: optmized, X & = (X - 1) 将最低位(LSB)的 1 清零
        counter = 0
        while n > 0:
            n = n & (n - 1)
            counter += 1
        return counter
