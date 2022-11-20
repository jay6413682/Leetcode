class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """ bit manipulation https://leetcode.cn/problems/power-of-four/solution/4de-mi-by-leetcode-solution-b3ya/
        https://leetcode.cn/leetbook/read/leetcode-cookbook/5ce7xc/ 
        """
        # n & (n - 1)) == 0 : 偶数或 1
        # mask=(01010101010101010101010101010101)2， mask & n 如果 == 0，排除n 是 2 的幂却不是 4 的幂
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
        # mask=(10101010101010101010101010101010)2， mask & n 如果 == 1，排除n 是 2 的幂却不是 4 的幂
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0

        if n <= 0:
            return False
        # n & (n - 1) == 0 表示只有一个1，所以一定是偶数 或 1。
        # 如果 n 是 4 的幂，那么它可以表示成 4^x 的形式，我们可以发现它除以 3 的余数一定为 1，
        # 另外如果 n 是 2 的幂却不是 4 的幂，那么它可以表示成 4^x * 2 的形式，此时它除以 3 的余数一定为 2。
        # 证明 (4**n - 1) % 3 == 0，(1) 4**n - 1 = (2**n + 1) * (2**n - 1)(2) 在任何连续的 3 个数中 (2**n-1)，(2**n)，(2**n+1)，一定有一个数是 3 的倍数。(2**n) 肯定不是 3 的倍数，那么 (2**n-1) 或者 (2**n+1) 中一定有一个是 3 的倍数。所以 4**n-1 一定是 3 的倍数。
        return n & (n - 1) == 0 and (n - 1) % 3 == 0

        if n <= 0:
            return False
        counter = 0
        tmp = n
        while tmp & 1 != 1:
            counter += 1
            tmp >>= 1
        # n & -n 得到lsb 的 1，如果== n 说明 n 是 1000000... , 再判断1后面有 偶数个0
        return counter % 2 == 0 and n & -n == n
