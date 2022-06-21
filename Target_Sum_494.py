class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """ dp, 背包优化， 解释类似https://leetcode.cn/problems/target-sum/solution/huan-yi-xia-jiao-du-ke-yi-zhuan-huan-wei-dian-xing/ 解法类似lwb0214 comment
        但要注意，target和j - nums[i - 1] 为负的情况
        其他解法见：https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247488724&idx=1&sn=68b106ec37730b9ce3988195ae45ac7b&chksm=fd9cbfcbcaeb36dd59df2aa48f530b22897e20bf824e99f4d68ac09e8521b8cfc3b22bb44927&scene=178&cur_album_id=1751702161341628417#rd
        """
        sm = 0
        for num in nums:
            sm += num
        if sm < abs(target):
            return 0
        if (target + sm) % 2 != 0:
            return 0
        
        positive_sum = (target + sm) // 2
        n = len(nums)
        dp = [[0 for _ in range(positive_sum + 1)] for _ in range(n + 1)]
        # dp 定义为前个数，选择的数之和为j 的 方案数
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(positive_sum + 1):
                # dp[i - 1][j] 不选i
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    # dp[i - 1][j - nums[i - 1]] 选i
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
        return dp[n][positive_sum]
