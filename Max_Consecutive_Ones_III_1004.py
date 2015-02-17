class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """ 滑动窗口 sliding window 
        重点：题意转换。把「最多可以把 K 个 0 变成 1，求仅包含 1 的最长子数组的长度」转换为 「找出一个最长的子数组，该子数组内最多允许有 K 个 0 」。经过上面的题意转换，我们可知本题是求最大连续子区间，可以使用滑动窗口方法。滑动窗口的限制条件是：窗口内最多有 K 个 0。
        https://leetcode-cn.com/problems/max-consecutive-ones-iii/solution/fen-xiang-hua-dong-chuang-kou-mo-ban-mia-f76z/ """
        left = right = 0
        zero_counts = 0
        res = 0
        n = len(nums)
        while right < n:
            if nums[right] == 0:
                zero_counts += 1
            while zero_counts > k:
                if nums[left] == 0:
                    zero_counts -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
        """
        # labuladong 模版
        left = right = 0
        window = deque()
        zero_count = 0
        res = 0
        n = len(nums)
        while right < n:
            window.append(nums[right])
            if nums[right] == 0:
                zero_count += 1
            right += 1
            while zero_count > k:
                window.popleft()
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            res = max(res, len(window))
        return res
        """
