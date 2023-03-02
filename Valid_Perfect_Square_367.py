class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """ binary search
        https://leetcode-cn.com/problems/valid-perfect-square/solution/ceng-ceng-di-jin-zhu-bu-zui-you-de-si-chong-jie-fa/
        时间复杂度：\mathcal{O}(\log N)O(logN)。
        空间复杂度：\mathcal{O}(1)O(1)。
        """
        left = 1
        right = num
        while left < right:
            mid = (left + right + 1) // 2
            if mid * mid > num:
                right = mid - 1
            else:
                left = mid
        return True if left * left == num else False


class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        """ 牛顿迭代法
        https://leetcode-cn.com/problems/valid-perfect-square/solution/you-xiao-de-wan-quan-ping-fang-shu-by-le-wkee/
        有局限，若最终近似解|xm - xm-1| > 1 有可能错误解；例如jerryluan 在https://leetcode-cn.com/problems/valid-perfect-square/solution/ceng-ceng-di-jin-zhu-bu-zui-you-de-si-chong-jie-fa/ 的提问
        求出 切线 的 方程 y - ( xi ^2 - num ) = 2 * xi * (x - xi)
        当 y 是 0 时，得到 x 的方程。然后 x 不断 缩小到 要么等于x的平方 恰好等于 num， 要么 小于num终止
        """
        xk = num
        while xk * xk > num:
            # print(xk)
            xk = (num + xk * xk) // 2 // xk
        print(xk)
        return True if xk * xk == num else False
        '''
        # or better
        x0 = num
        while True:
            x1 = (x0 + num / x0) / 2
            if x0 - x1 < 1e-6:
                break
            x0 = x1
        x0 = int(x0)
        return x0 * x0 == num
        '''
        '''
        # my try
        prev = 0
        curr = num
        while abs(curr - prev) > 10 ** -7:
            prev = curr
            curr = (num + curr ** 2) / (2 * curr)
            #print(curr, prev)
        #print(int(curr))
        #print(abs(int(curr) ** 2))
        if curr - floor(curr - 0.5) <= 1:
            int_curr = ceil(curr)
        else:
            int_curr = floor(curr)
        #print(int_curr, curr)
        return abs(int_curr - curr) <= 10 ** -7
        '''


class Solution3:
    def isPerfectSquare(self, num: int) -> bool:
        """ 数学法math
        公式：1+3+5+7+...(2N−1)=N^2
        https://leetcode-cn.com/problems/valid-perfect-square/solution/ceng-ceng-di-jin-zhu-bu-zui-you-de-si-chong-jie-fa/
        推导方法：
        (n+1)^2 - n^2 = 2n + 1
        (n)^2 - (n-1)^2 = 2n - 1
        ...
        2^2 - 1 ^ 2 = 4 - 1 = 3
        1 - 0 = 2 - 1 = 1
        so (n + 1)^2 = 1 + 3 + 5 .. + 2n + 1
        so n^2 = 1 + 3 ... + 2n -1
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return True if num == 0 else False
