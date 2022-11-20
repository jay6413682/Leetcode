class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ 二分查找 binary search (二分答案)
        https://leetcode.cn/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/
        n + 1 个整数，放在长度为 n 的数组里，根据「抽屉原理」，至少会有 1 个整数是重复的；
        使用「二分查找」查找一个整数，这是「二分查找」的典型应用，经常被称为「二分答案」。
        央视《幸运 52》节目的「猜价格游戏」，就是「二分答案」。玩家猜一个数字，如果猜中，游戏结束，如果主持人说「猜高了」，应该猜一个更低的价格，如果主持人说「猜低了」，应该猜一个更高的价格。

        """
        left = 1
        right = len(nums) - 1
        # 在 [1..n] 查找 nums 中重复的元素
        while left < right:
            mid = (left + right) // 2
            counter = 0
            # nums 中小于等于 mid 的元素的个数
            for num in nums:
                if num <= mid:
                    counter += 1
            if counter > mid:
                # 如果 1 <= nums <= mid 的元素的个数 大于 mid, 根据「抽屉原理」，至少会有 1 个整数是重复的；
                # 下一轮搜索的区间 [left..mid]
                right = mid
            else:
                # count <= mid, -count >= -mid
                # 下一轮搜索的区间 [mid + 1..right]
                # [mid + 1..right] 中有 right - mid 个整数
                # [mid + 1..right] 在 nums 出现 len - count 次, right + 1 = len
                # len - count >= right + 1 - mid > right - mid
                # 根据「抽屉原理」，至少会有 1 个整数是重复的；
                left = mid + 1
        return left
