class Solution2:
    def myPow(self, x: float, n: int) -> float:
        """ 二分法，my solution, recursive， 优化Solution3 类似https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/
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
