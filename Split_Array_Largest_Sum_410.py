class Solution:
    res = float(inf)
    def splitArray(self, nums: List[int], m: int) -> int:
        """ binary search 特殊二分答案 最大值极小化 https://leetcode.cn/problems/split-array-largest-sum/solution/er-fen-cha-zhao-by-liweiwei1419-4/
        from numbers sheet: 目标变量和另一个变量有相关关系（一般是线性关系），目标变量的性质不好推测，但是另一个变量的性质相对容易推测（满足某种意义上的单调性）。这样的问题的判别函数通常会写成一个函数的形式。
        如果设置「数组各自和的最大值」很大，那么必然导致分割数很小；
        如果设置「数组各自和的最大值」很小，那么必然导致分割数很大。
        目标变量 largest sum
        另一个变量 : splits
        """
        # 计算「子数组各自的和的最大值」的上下界
        left = max(nums)
        right = sum(nums)
        def split_nums(nums, max_sum):
            # greedy algorithm，贪心算法
            # nums 原始数组
            # max_sum 子数组各自的和的最大值
            # return 满足不超过「子数组各自的和的最大值」的分割数
            # 至少是一个分割
            splits = 1
            # 当前区间的和
            curr_sum = 0
            for num in nums: 
                # 尝试加上当前遍历的这个数，如果加上去超过了「子数组各自的和的最大值」，就不加这个数，另起炉灶
                # 并在 num 之前加 split
                if curr_sum + num > max_sum:
                    curr_sum = 0
                    splits += 1
                curr_sum += num
            return splits
        # 使用「二分查找」确定一个恰当的「子数组各自的和的最大值」，
        # 使得它对应的「子数组的分割数」恰好等于 m
        while left < right:
            mid = (left + right) // 2
            splits = split_nums(nums, mid)
            # 如果分割数太多，说明「子数组各自的和的最大值」太小，此时需要将「子数组各自的和的最大值」调大
            # 下一轮搜索的区间是 [mid + 1, right]
            if splits > m:
                left = mid + 1
            else:
                right = mid
        return left
        """ dynamic programming/dp/动态规划 超时: https://leetcode.cn/problems/split-array-largest-sum/solution/er-fen-cha-zhao-by-liweiwei1419-4/ """
        le = len(nums)
        dp = [[float(inf) for _ in range(m + 1)] for _ in range(le)]
        # prefix sum 优化 前缀和
        presums = [nums[0]]
        for i in range(1, le):
            presums.append(presums[i - 1] + nums[i])
        presums = [sum(nums[:i + 1]) for i in range(le)]
        for i in range(le):
            for k in range(m + 1):
                #print(i, k, dp)
                if k == 1:
                    dp[i][k] = presums[i]
                if k >= 2:
                    for j in range(k - 2, i):
                        dp[i][k] = min(dp[i][k], max(dp[j][k - 1], presums[i] - presums[j]))
        #print(dp)
        return dp[le - 1][m]
        """ 我的解 回溯法 backtracking 超时 """
        le = len(nums)
        def dfs(start_i, cuts_left, nums, length, sums):
            # backtracking
            # cut after start_i
            if cuts_left == 0:
                #print(start_i)
                x = sums + [sum(nums[start_i:])]
                # print(x)
                ma = max(x)
                if ma < self.res:
                    self.res = ma
                return
            if cuts_left > 0 and start_i == length - 1:
                return
            for cut_index in range(start_i, length - 1):
                s = sum(nums[start_i:cut_index + 1])
                if s > self.res:
                    return
                sums.append(s)
                dfs(cut_index + 1, cuts_left - 1, nums, length, sums)
                sums.pop()
        dfs(0, m - 1, nums, le, [])
        #print(res)
        return self.res
