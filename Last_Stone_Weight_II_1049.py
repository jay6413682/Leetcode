class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """ 0/1背包，dynamic programming，dp：将问题彻底切换为 01 背包问题：从 stones 数组中选择，凑成总和不超过 sum/2 的最大价值。
        https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247488868&idx=1&sn=5e54a1d091a8249d3033a28fc299076d&chksm=fd9cbe7bcaeb376d1ee8a753ebc57358e5605fc1a3b51865eb0f758fb3e6e4688e1b0acfa902&scene=178&cur_album_id=1751702161341628417#rd
        """
        sm = sum(stones)
        n = len(stones)
        target = sm // 2
        dp = [[0 for _ in range(target + 1)] for _ in range(n)]
        for i in range(n):
            for j in range(1, target + 1):
                if i == 0:
                    if j >= stones[i]:
                        dp[i][j] = stones[i]
                else:
                    dp[i][j] = dp[i - 1][j]
                    if j >= stones[i]:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - stones[i]] + stones[i])
        # print(dp)
        return sm - dp[n - 1][target] - dp[n - 1][target]