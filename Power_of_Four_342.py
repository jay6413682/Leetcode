class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """ bit manipulation https://leetcode.cn/problems/power-of-four/solution/4de-mi-by-leetcode-solution-b3ya/
        https://leetcode.cn/leetbook/read/leetcode-cookbook/5ce7xc/ 
        """
        # n & (n - 1) == 0 : 2^n 或 1
        # mask=(01010101010101010101010101010101)2， mask & n 如果 == 0，排除n 是 2 的幂却不是 4 的幂
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0
        # mask=(10101010101010101010101010101010)2， mask & n 如果 == 1，排除n 是 2 的幂却不是 4 的幂
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0

        if n <= 0:
            return False
        # n & (n - 1) == 0 表示只有一个1，所以n 一定是2 ^ n 或 1。
        # 如果 n 是 4 的幂，那么它可以表示成 4^x 的形式，我们可以发现它除以 3 的余数一定为 1，
        # 另外如果 n 是 2 的幂却不是 4 的幂，那么它可以表示成 4^x * 2 的形式，此时它除以 3 的余数一定为 2。
        # 证明 (4**n - 1) % 3 == 0，(1) 4**n - 1 = (2**n + 1) * (2**n - 1)(2) 在任何连续的 3 个数中 (2**n-1)，(2**n)，(2**n+1)，一定有一个数是 3 的倍数。(2**n) 肯定不是 3 的倍数，那么 (2**n-1) 或者 (2**n+1) 中一定有一个是 3 的倍数。所以 4**n-1 一定是 3 的倍数。
        # 如果 n 是 2 ^ x, 把它代入 右式，(2 ^ x - 1) % 3, 如果 == 0 ，则 (2 ^ (x/2) + 1）* (2 ^ (x/2) - 1）% 3 == 0, 那么 2 ^ (x/2) 一定是 integer，x 一定是偶数，那么 n = 2 ^ 2m，所以 n = 4 ^ m
        if n & (n - 1) == 0 and (n - 1) % 3 == 0:
            return True
        else:
            # 还有 别的 条件能使得 n 是 4 ^ y 吗？
            if n & (n - 1) == 0 and (n - 1) % 3 != 0:
                # (2 ^ y - 1) % 3 != 0 --> (2 ^ (y/2) - 1)(2 ^ (y/2) + 1) % 3 != 0 ---> y 必然是 奇数，否则 一定能被 被 3 整除 ---> 2 ^ y = 2 ^ (2k + 1) = 2 ^ 2k * 2 = 4 ^ k * 2, 一定不是 power of 4
                return False
            elif n & (n - 1) != 0 and and (n - 1) % 3 == 0:
                return False
            else:
                # n & (n - 1) != 0 and and (n - 1) % 3 != 0
                return False
            

        if n <= 0:
            return False
        counter = 0
        tmp = n
        while tmp & 1 != 1:
            counter += 1
            tmp >>= 1
        # n & -n 得到lsb 的 1，如果== n 说明 n 是 1000000... , 再判断1后面有 偶数个0
        return counter % 2 == 0 and n & -n == n
    
        # 这道题最直接的方法就是不停的去除以 4 ，看最终结果是否为 1 https://leetcode.cn/problems/power-of-four/solution/e-you-shi-yi-dao-zhuang-bi-jie-fa-de-suan-fa-ti-2/
        if n <= 0:
            return False
        while n % 4 == 0:
            n = n / 4
        return n == 1
