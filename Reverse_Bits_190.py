class Solution:
    def reverseBits(self, n: int) -> int:
        # bit manipulation/ 位运算 https://leetcode.cn/leetbook/read/leetcode-cookbook/5cm9cv/
        i = 32
        res = 0
        while i > 0:
            current_bit = n & 1
            # res += current_bit * (2 ** (i - 1))
            res = res << 1 | n & 1
            n >>= 1
            i -= 1
        return res


class Solution2:
    def reverseBits(self, n: int) -> int:
        """ 优化解 O（1） 分而治之 bit manipulation: https://leetcode.cn/problems/reverse-bits/solution/fu-xue-ming-zhu-xun-huan-yu-fen-zhi-jie-hoakf/
        0x55555555; // 01010101010101010101010101010101
        0x33333333; // 00110011001100110011001100110011
        0x0f0f0f0f; // 00001111000011110000111100001111
        0x00ff00ff; // 00000000111111110000000011111111
        ...
        """
        n = (n >> 16) | (n << 16);
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1);
        return n;
