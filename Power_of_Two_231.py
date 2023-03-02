class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # bit manipulation
        # https://leetcode.cn/problems/power-of-two/solution/2de-mi-by-leetcode-solution-rny3/
        # negative number cannot be power of 2
        # 一个数 n 是 2 的幂，当且仅当 n 是正整数，并且 n 的二进制表示中仅包含 1 个 1。
        while n > 0:
            if n == 1:
                return True
            if n % 2 == 1:
                return False
            n = n // 2
        return False
        # X & (X - 1) 将最低位(LSB)的 1 清零
        if n > 0 and n & (n - 1) == 0:
            return True
        return False
        # X & -X 得到最低位(LSB)的 1
        if n > 0 and n & -n == n:
            return True
        return False
        # 我们只需要判断 nn 是否是 最大 power of 2 的约数即可。
        if n > 0 and 2 ** 30 % n == 0:
            return True
        return False
