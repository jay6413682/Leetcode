class Solution2:
    def myPow(self, x: float, n: int) -> float:
        """ 分治法，my solution, recursive， 优化Solution3 类似https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/
        时间复杂度：O(\log n)O(logn)，即为递归的层数。

        空间复杂度：O(\log n)O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间。

        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        elif n > 0:
            return half * half * x
        else:
            half = self.myPow(x, -1 * n // 2)
            return 1 / (half * half * x)


class Solution4:
    def myPow(self, x: float, n: int) -> float:
        """ iterative
        假设  n 可以写成 二进制表示 bk bk-1 … b1 b0
        也就是说x ^ n 可以写成 x ^ (2 ^ 0 * b0) * x ^ (2 ^ 1 * b1)  * x ^ (2 ^ 2 * b2)  * x ^ (2 ^ 3 * b3)  … 
        也就是 x ^ (1 * b0) * x ^ (2 * b1)  * x ^ (4 * b2)  * x ^ (8 * b3)  …
        所以 如果 b 位 是0，result * 1 ，如果 b 位 是1，result * 乘数，在b0 这一位，乘数 是 1，在 b1这一位，乘数 是 x ^ 2, 在 b2这一位，乘数 是 x ^ 4, … 其实 就是 上 一位 乘数 再 乘以 它 自己

        只需记住 https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/ 的公式
        圖解與解法：https://leetcode-cn.com/problems/powx-n/solution/ba-zhi-shu-bu-fen-kan-zuo-er-jin-zhi-shu-python-da/

        时间复杂度：O(\log n)O(logn)，即为对 nn 进行二进制拆分的时间复杂度。

        空间复杂度：O(1)O(1)。
        """
        power = n if n >= 0 else n * -1
        to_multiply = 1
        res = 1
        start = False
        while power:
            b = power & 1
            if not start:
                to_multiply = x
            else:
                to_multiply *= to_multiply
            if b == 1:
                res *= to_multiply
            power >>= 1
            start = True
        return res if n >= 0 else 1 / res


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """ My solution. iterative, 超时 """
        i = 0
        res = 1
        if n > 0:
            while i < n:
                res *= x
                i += 1
        elif n < 0:
            while i > n:
                res *= x
                i -= 1
            res = 1 / res
        return res


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        """ My solution. recursive, 超时 """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        return self.myPow(x, n - 1) * x if n > 0 else self.myPow(x, n + 1) * 1 / x


class Solution3:
    def myPow(self, x: float, n: int) -> float:
        """ 二分法，my solution，超时 """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        if n % 2 == 0:
            return self.myPow(x, n // 2) * self.myPow(x, n // 2) 
        elif n > 0:
            return self.myPow(x, n // 2) * self.myPow(x, n // 2) * x
        else:
            return self.myPow(x, (n + 1) // 2) * self.myPow(x, (n + 1) // 2) * 1 / x
