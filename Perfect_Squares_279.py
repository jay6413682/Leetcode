class Solution:
    def numSquares(self, n: int) -> int:
        """ dp/背包问题。https://leetcode-cn.com/problems/perfect-squares/solution/gong-shui-san-xie-xiang-jie-wan-quan-bei-nqes/
        会超时
        时间复杂度：预处理出所有可能用到的数字复杂度为 O(\sqrt{n})O( n)，共有 n * \sqrt{n}n∗ n 个状态需要转移，每个状态转移最多遍历 nn 次，因此转移完所有状态复杂度为 O(n^2 * \sqrt{n})O(n 2∗ n)。整体复杂度为 O(n^2 * \sqrt{n})O(n 2∗ n)。
        空间复杂度：O(n * \sqrt{n})O(n∗ n)。

        """
        nums = []
        for i in range(1, 101):
            if i ** 2 <= n:
                nums.append(i ** 2)
            else:
                break
        # print(nums)
        m = len(nums)
        # '''
        # 最大是n
        dp = [[n] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                # print(i, j)
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif nums[i - 1] == j:
                    dp[i][j] = 1
                else:
                    # not select item i
                    # dp[i][j] = dp[i - 1][j]
                    for k in range(0, j // nums[i - 1] + 1):
                        dp[i][j] = min(dp[i][j], dp[i - 1][j - k * nums[i- 1]] + k)
                    '''
                    if j - nums[i - 1] >= 0:
                        yes = dp[i - 1][j - nums[i - 1]] + 1
                        for k in range(2, j // nums[i - 1] + 1):
                            yes = min(yes, dp[i - 1][j - k * nums[i- 1]] + k)
                        # print(j, nums[i - 1], yes, no, j // nums[i - 1] + 1)
                    else:
                        yes = no
                    dp[i][j] = min(no, yes)
                    '''
        # print(dp)
        return dp[m][n]
        '''
        # try no. 2
        i = 1
        nums = []
        while i ** 2 <= n:
            nums.append(i ** 2)
            i += 1
        # print(nums)
        m = len(nums)
        # dp[i][j] 代表考虑前 i 个物品，凑出 j 所使用到的最小元素个数
        # 当没有任何数时，除了 f[0][0] 为 0（花费 0 个数值凑出 0），其他均为无效值 (n 为最大值， n + 1 为无效值)
        dp = [[n + 1] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                else:
                    k = 0
                    while k * nums[i - 1] <= j:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j - k * nums[i - 1]] + k)
                        k += 1
        return dp[m][n]
        '''


class Solution2:
    def numSquares(self, n: int) -> int:
        """ dp/背包问题 / 优化一。https://leetcode-cn.com/problems/perfect-squares/solution/gong-shui-san-xie-xiang-jie-wan-quan-bei-nqes/
        会超时
        时间复杂度：预处理出所有可能用到的数字复杂度为 O(\sqrt{n})O( n)，共有 n * \sqrt{n}n∗ n 个状态需要转移，每个状态转移最多遍历 nn 次，因此转移完所有状态复杂度为 O(n^2 * \sqrt{n})O(n 2∗ n)。整体复杂度为 O(n^2 * \sqrt{n})O(n 2∗ n)。
        空间复杂度：O(n )。

        """
        nums = []
        for i in range(1, 101):
            if i ** 2 <= n:
                nums.append(i ** 2)
            else:
                break
        # print(nums)
        m = len(nums)
        # '''
        # 最大是n
        dp = [[n] * (n + 1) for _ in range(2)]
        for i in range(m + 1):
            for j in range(n + 1):
                # print(i, j)
                if i == 0 and j == 0:
                    dp[i][j] = 0
                # elif nums[i - 1] == j:
                #    dp[i % 2][j] = 1
                else:
                    # not select item i
                    # dp[i][j] = dp[i - 1][j]
                    if i >= 1:
                        for k in range(j // nums[i - 1] + 1):
                            dp[i % 2][j] = min(dp[i % 2][j], dp[(i - 1) % 2][j - k * nums[i - 1]] + k)
                    '''
                    if j - nums[i - 1] >= 0:
                        yes = dp[i - 1][j - nums[i - 1]] + 1
                        for k in range(2, j // nums[i - 1] + 1):
                            yes = min(yes, dp[i - 1][j - k * nums[i- 1]] + k)
                        # print(j, nums[i - 1], yes, no, j // nums[i - 1] + 1)
                    else:
                        yes = no
                    dp[i][j] = min(no, yes)
                    '''
        # print(dp)
        return dp[m % 2][n]


class Solution3:
    def numSquares(self, n: int) -> int:
        """ dp/背包问题 / 优化二。https://leetcode-cn.com/problems/perfect-squares/solution/gong-shui-san-xie-xiang-jie-wan-quan-bei-nqes/
        时间复杂度：共有 n * \sqrt{n}n∗ n个状态需要转移，复杂度为 O(n * \sqrt{n})O(n∗ n)。
        空间复杂度：O(n)O(n)。
        """
        nums = []
        for i in range(1, 101):
            if i ** 2 <= n:
                nums.append(i ** 2)
            else:
                break
        # print(nums)
        m = len(nums)
        # 最大是n
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(m + 1):
            for j in range(n + 1):
                if i >= 1 and j >= nums[i - 1]:
                    dp[j] = min(dp[j], dp[j - nums[i - 1]] + 1)
        # print(dp)
        return dp[-1]
