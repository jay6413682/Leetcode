
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--41/
        """
        """
        x = m
        temp = 0xffffffff
        while x >= m and x <= n:
            temp &= x
            if temp == 0 or x == 2147483647:
                break
            x += 1
        return temp
        """
        # 为了避免超时，由于只要n二进制的位数比m多一位以上，如1010和10000,那么结果必然为0,所以增加几行:
        if len(bin(n)) > len(bin(m)):
            return 0
        res = m
        for i in range(m + 1, n + 1):
            res &= i
            if res == 0:
                break
        return res


class Solution2:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """ https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/solution/ju-hao-li-jie-de-wei-yun-suan-si-lu-by-time-limit/
        https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/solution/shu-zi-fan-wei-an-wei-yu-by-leetcode-solution/
        问题转换为 给定两个整数，我们要找到它们对应的二进制字符串的公共前缀。 
        时间复杂度：O(logn)。算法的时间复杂度取决于 mm 和 nn 的二进制位数，由于 m≤n，因此时间复杂度取决于 nn         的二进制位数。
        空间复杂度：O(1)。我们只需要常数空间存放若干变量。

        """
        counter = 0
        while m < n:
            m >>= 1
            n >>= 1
            counter += 1
        return m << counter


class Solution3:
    """
    https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/solution/shu-zi-fan-wei-an-wei-yu-by-leetcode-solution/
    Brian Kernighan 算法
    X & = (X - 1) 将最低位(LSB)的 1 清零
    https://leetcode-cn.com/leetbook/read/leetcode-cookbook/5c9u92/
    """
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n &= (n - 1)
        return n
