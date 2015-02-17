class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """ DP优化解/非背包 https://leetcode-cn.com/problems/maximum-product-subarray/solution/dpfang-fa-xiang-jie-by-yang-cong-12/
        时间复杂度：程序一次循环遍历了 nums，故渐进时间复杂度为 O(n)O(n)。

        空间复杂度：优化后只使用常数个临时变量作为辅助空间，与 nn 无关，故渐进空间复杂度为 O(1)O(1)。

        """
        res = curr_max = curr_min = nums[0]
        for num in nums[1:]:
            cmin = curr_min
            cmax = curr_max
            if num < 0:
                curr_max = max(cmin * num, num)
                curr_min = min(cmax * num, num)
            else:
                curr_max = max(cmax * num, num)
                curr_min = min(cmin * num, num)
            res = max(curr_max, res)
        return res
        """
        # unoptimized solution:
        n = len(nums)
        # 两个DP分别定义为以i结尾的子数组的最大积与最小积: must include item i
        max_dp = [None] * n
        min_dp = [None] * n
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        for i in range(1, n):
            max_dp[i] = max(max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i], nums[i])
            min_dp[i] = min(max_dp[i - 1] * nums[i], min_dp[i - 1] * nums[i], nums[i])
        # print(max_dp)
        return max(max_dp)
        """
        """
        # if checking maximum product sub elements?
        n = len(nums)
        dp = [None] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] * nums[i], dp[i - 1], nums[i])
        print(dp)
        return dp[-1]
        """


class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        """ https://leetcode-cn.com/problems/maximum-product-subarray/solution/duo-chong-si-lu-qiu-jie-by-powcai-3/
        checkout Yves's comment
        /*
        * 以0为分界成一段一段分析
        * 在一段中负数的个数要么为偶数要么为奇数
        * 倘若负数的个数为偶数，那么直接相乘必然是最大值，因为偶数个负数相乘为正数
        * 倘若负数有奇数个，设为n个的话，那么n-1个负数则为偶数个
        * 那么这个减一因为是连续的子序列，所以要么是不包含最左边的负数，要么是不包含最右边的负数，只有这两种情况
        * 那么只需要从左往右遍历一次，从右往左遍历一次，求最大值就可以了
        * 注意为0的时候，虽然product要设置回1，但是有可能最大值就是0(每段都只有1个负数)，那么需要判断下answer是否更新为0
        */
        """
        product = 1
        res = -10
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                product = 1
                if res < 0:
                    res = 0
                continue
            product *= nums[i]
            res = max(res, product)
        product = 1
        for i in range(n - 1, -1, -1):
            if nums[i] == 0:
                product = 1
                if res < 0:
                    res = 0
                continue
            product *= nums[i]
            res = max(res, product)
        return res
