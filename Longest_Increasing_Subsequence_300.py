class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        动态规划/dynamic programming: https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
        时间复杂度：O(N^2)O(N 2)，这里 NN 是数组的长度，我们写了两个 for 循环，每个 for 循环的时间复杂度都是线性的；
        空间复杂度：O(N)O(N)，要使用和输入数组长度相等的状态数组，因此空间复杂度是 O(N)O(N)。

        """
        n = len(nums)
        # dp[i] 表示：以 nums[i] 结尾 的最长「上升子序列」的长度。注意：这个定义中 nums[i] 必须被选取，且必须是这个子序列的最后一个元素；
        dp = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """ O(n log(n)) 复杂度，想到 logn 要二分法
        详解： https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
        推导过程：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/yi-bu-yi-bu-tui-dao-chu-guan-fang-zui-you-jie-fa-x/

        """
        n = len(nums)
        # tails[i] : 长度为i + 1 的递增子序列的最小尾数
        # tails 是严格上升数组
        tails = deque([nums[0]])
        for i in range(1, n):
            if nums[i] > tails[-1]:
                tails.append(nums[i])
            else:
                # 在有序数组 tail 中查找第 1 个等于大于 num[i] 的那个数，试图让它变小；就是 最后的left
                left = 0
                right = len(tails) - 1
                while left < right:
                    mid = (left + right) // 2
                    if nums[i] > tails[mid]:
                        left = mid + 1
                    else:
                        right = mid
                tails[left] = nums[i]
        return len(tails)

