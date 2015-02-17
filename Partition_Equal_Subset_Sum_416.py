class Solution:
    """ backtrack回溯；超時 similar to https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/fen-ge-deng-he-zi-ji-hui-su-he-dong-tai-gui-hua-ji/
    但是上面的答案链接答案是错的
    """
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(remaining, nums, start, length):
            if remaining == 0:
                return True
            elif remaining < 0:
                return False
            for i in range(start, length):
                if nums[i] > total / 2:
                    return False
                if dfs(remaining - nums[i], nums, i + 1, length):
                    return True
            return False
        total = sum(nums)
        if total % 2 == 1:
            return False
        nums_sort = sorted(nums, reverse=True)
        return dfs(total / 2, nums_sort, 0, len(nums))


class Solution2:
    """ dp/背包问题 未优化： https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/gong-shui-san-xie-bei-bao-wen-ti-shang-r-ln14/
    价值最大化类型，不是很好理解，solution3比较好理解
    时间复杂度：targettarget 为数组总和的一半，nn 数组元素个数。为共有 n * targetn∗target 个状态需要被转移，复杂度为 O(n * target)O(n∗target)
    空间复杂度：O(n * target)O(n∗target)

    """
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = [[0] * (target + 1) for _ in range(n)]
        for i in range(n):
            for j in range(target + 1):
                if i == 0:
                    dp[i][j] = nums[i] if j >= nums[i] else 0
                else:
                    if j >= nums[i]:
                        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
                    else:
                        dp[i][j] = dp[i - 1][j]
        # print(dp)
        return dp[n - 1][target] == target
    

class Solution3:
    """ 01 背包问题 dp/背包问题 未优化： https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/gong-shui-san-xie-bei-bao-wen-ti-xia-con-mr8a/
    时间复杂度：targettarget 为数组总和的一半，nn 数组元素个数。为共有 n * targetn∗target 个状态需要被转移，复杂度为 O(n * target)O(n∗target)
    空间复杂度：O(n * target)O(n∗target)

    我们可以通过将一个背包问题的「状态定义」从最多不超过 XX 容量修改为背包容量恰好为 XX，同时再把「有效值构造」出来，也即是将物品下标调整为从 1 开始，设置 dp[0][0]dp[0][0] 为初始值。

    这其实是另外一类「背包问题」，它不对应「价值最大化」，对应的是「能否取得最大/特定价值」。这样的「背包问题」同样具有普遍性。

    """
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        dp = [[False] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(target + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i > 0:
                    # print('{} {}'.format(i, j))
                    if j >= nums[i - 1]:
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                    else:
                        dp[i][j] = dp[i - 1][j]
        # print(dp)
        return dp[n][target]
