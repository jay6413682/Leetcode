class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """ binary search/特殊二分答案 最小化最大值
        https://juejin.cn/post/6864407058662457358 
        类似410 题
        """
        left = max(weights)
        right = sum(weights)
        def split_weights(weights, weight_capacity):
            spent_days = 1
            curr_weight_sum = 0
            for w in weights:
                if curr_weight_sum + w > weight_capacity:
                    spent_days += 1
                    curr_weight_sum = 0
                curr_weight_sum += w
            return spent_days
        while left < right:
            # 运载能力
            mid = (left + right) // 2
            # 运载能力越大，天数越少
            # 运载能力越小，天数越多
            # 负相关
            spent_days = split_weights(weights, mid)
            if spent_days > days:
                # 太多，下一轮搜索区间 [mid + 1, right]
                left = mid + 1
            else:
                # 下一轮搜索区间 [left, mid]
                right = mid
        return left
