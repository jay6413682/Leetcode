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
        '''
        # my lates try
        i = 31
        res = 0
        while i >= 0:
            j = 31 - i
            bit_i = (n >> i) & 1
            bit_j = (n >> j) & 1
            res |= bit_j << i
            res |= bit_i << j
            i -= 1
        return res
        '''


class Solution2:
    def reverseBits(self, n: int) -> int:
        """ 优化解 O（1） 分而治之 bit manipulation: https://leetcode.cn/problems/reverse-bits/solution/fu-xue-ming-zhu-xun-huan-yu-fen-zhi-jie-hoakf/
        0x55555555; // 01010101010101010101010101010101
        0x33333333; // 00110011001100110011001100110011
        0x0f0f0f0f; // 00001111000011110000111100001111
        0x00ff00ff; // 00000000111111110000000011111111
        ...
        """
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n
        """ divde and conquer. my solution """
        #print(n)
        list_n = []
        for i in range(31, -1, -1):
            curr = (n >> i) & 1
            list_n.append(curr)
        #print(list_n)
        def div_conq(list_n, start, end):
            if start == end:
                return
            mid = (start + end) // 2
            list_n[start:end + 1] = list_n[mid + 1:end + 1] + list_n[start:mid + 1]
            div_conq(list_n, start, mid)
            div_conq(list_n, mid + 1, end)
        div_conq(list_n, 0, len(list_n) - 1)
        #print(list_n)
        res = 0
        for i in range(31, -1, -1):
            res |= (list_n[31 - i] << i)
        return res
