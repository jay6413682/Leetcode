class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        """ my own solution. 快速幂 超时 """
        # convert b to int
        n = len(b)
        multi = 1
        b_int = 0
        for i in range(n - 1, -1, -1):
            b_int += b[i] * multi
            multi *= 10
        # print(b_int)
        res = 1
        # start = False
        multi = a
        while b_int:
            if b_int & 1 == 1:
                res *= multi
            b_int >>= 1
            multi *= multi
        res %= 1337
        return res


class Solution:
    def fast_pow(self, a, k):
        """ 快速幂，以及乘法的模运算 """
        multi = a
        res = 1
        while k:
            if k & 1 == 1:
                res = ((res % 1337) * (multi % 1337)) % 1337
            multi = ((multi % 1337) * (multi % 1337)) % 1337
            k >>= 1
        return res

    def superPow(self, a: int, b: List[int]) -> int:
        """ 数学 math 快速幂 exponentiating by squaring 递归 https://leetcode.cn/problems/super-pow/solution/you-qian-ru-shen-kuai-su-mi-suan-fa-xiang-jie-by-l/ """
        if not b:
            return 1
        n = len(b)
        last_digit = b.pop()
        left = self.fast_pow(a, last_digit)
        right = self.fast_pow(self.superPow(a, b), 10)
        return (left * right) % 1337
