class Solution:
    def findComplement(self, num: int) -> int:
        # bit manipulation
        # https://leetcode.cn/leetbook/read/leetcode-cookbook/5c9u92/
        one_bit = 1
        while one_bit <= num:
            one_bit <<= 1
        # (1 << n) - 1 得到 000...0001111...
        # 将 x 第 n - 1 位开始取反，x ^ ((1 << n) - 1)
        # x ^ 11111……1111 = ~x
        return (one_bit - 1) ^ num

        # ~0 << n 得到 111...1110000...
        # 将 x 最右边的 n 位清零， x & ( ~0 << n )
        ones = ~0
        while ones & num > 0:
            ones <<= 1
        # x ^ 11111……1111 = ~x
        return ~ones ^ num

        # my solution: 
        # x ^ 11111……1111 = ~x
        # 00000...1111 ^ num: 后几位取反
        res = num ^ (2 ** 31 - 1)
        i = 30
        while i >= 0:
            # 获取 x 的第 n 位的幂值，x & (1 << (n - 1))
            if (1 << i) & res == 0:
                # 从左到右扫，扫到0停止
                break
            else:
                # 从左到右扫，扫到1 转成 0
                res ^= (1 << i)
            i -= 1
        return res

        # https://leetcode.cn/problems/number-complement/solution/tong-ge-lai-shua-ti-la-jian-dan-gao-xiao-k0p9/
        # 找到最高位的1，左移一位并-1，异或
        highbit = 1;
        x = num;
        while (x != 0):
            # 找最低位（最右边）的 1
            highbit = x & (-x)
            # 打掉最低位（最右边）的1
            x = x & (x - 1)
        return num ^ ((highbit << 1) - 1)

        # https://leetcode.cn/problems/number-complement/solution/shu-zi-de-bu-shu-by-leetcode-solution-xtn8/
        # 找到最高位的1，左移一位并-1，异或
        highbit = 0
        for i in range(1, 30 + 1):
            if num >= (1 << i):
                highbit = i
            else:
                break
        mask = (1 << (highbit + 1)) - 1
        return num ^ mask
