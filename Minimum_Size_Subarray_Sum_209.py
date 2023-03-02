class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """ 我的最新解 sliding window 滑动窗口 超时 根据模版 右侧指针拉动左侧指针 """
        n = len(nums)
        left = right = 0
        res = 0
        while right < n:
            while sum(nums[left:right + 1]) >= target:
                current_len = right - left + 1
                if res == 0:
                    res = current_len
                else:
                    res = current_len if right - left + 1 < res else res
                left += 1
            right += 1
        return res
        """ 我的最新优化解 sliding window 滑动窗口 我的优化解 右侧指针拉动左侧指针 """
        n = len(nums)
        left = right = 0
        res = 0
        s = 0
        while right < n:
            s += nums[right]
            while s >= target:
                current_len = right - left + 1
                if res == 0:
                    res = current_len
                else:
                    res = current_len if right - left + 1 < res else res
                s -= nums[left]
                left += 1
            right += 1
        return res
        
        """ 二分搜索binary search / prefix sum ： https://leetcode.cn/problems/minimum-size-subarray-sum/solution/by-ac_oier-c5jm/
        prefix sum 包括 0 -> le, sums[0] 是 没有元素的时候的 prefix sum，sums[1]是 i=0 时的 prefix sum
        """
        le = len(nums)
        sums = [0]
        for i in range(le):
            sums.append(sums[-1] + nums[i])
        res = le + 1
        for i in range(1, le + 1):
            # left/right/mid ： 找到i 左侧 最大下标 j 使得 sums[j] <= sums[i] - target ,
            exp_prefix_sum = sums[i] - target
            left = 0
            right = i
            while left < right:
                mid = (left + right + 1) // 2
                if sums[mid] <= exp_prefix_sum:
                    left = mid
                else:
                    right = mid - 1
            # 如果sums[left] > exp_prefix_sum 那么 left 不成立
            if sums[left] <= exp_prefix_sum:
                res = min(res, i - left)
        # 如果 res == le + 1，则 没有找到，所以return 0
        if res == le + 1:
            return 0
        return res

        # option 2:
        """ 二分搜索binary search / prefix sum 我的解
        与上面答案的差别在于，prefix sum 不包括 没有元素的时候的 prefix sum
        """
        sums = [nums[0]]
        for i in range(1, le):
            sums.append(sums[-1] + nums[i])
        res = le + 1
        for i in range(le):
            exp_prefix_sum = sums[i] - target
            left = 0
            right = i
            while left < right:
                mid = (left + right + 1) // 2
                if sums[mid] <= exp_prefix_sum:
                    left = mid
                else:
                    right = mid - 1                
            if sums[left] <= exp_prefix_sum:
                res = min(res, i - left)
            elif left == 0 and nums[0] >= target:
                res = 1
                break
            elif left == 0 and sums[i] >= target:
                res = min(res, i + 1)

        if res == le + 1:
            return 0
        return res
                
            

        """ 二分答案，类似 https://leetcode.cn/problems/minimum-size-subarray-sum/solution/209chang-du-zui-xiao-de-zi-shu-zu-c-onlo-jf70/
        我的解是 用 滑动窗口 来求 给定的window size ，window 内 元素的和 能否 >= target
        链接中的解 是先 预处理前缀和，再利用前缀和 求 给定的window size ，window 内 元素的和 能否 >= target
        """
        le = len(nums)
        # option 2:
        sums = [nums[0]]
        for i in range(1, le):
            sums.append(sums[-1] + nums[i])
        def is_window_sum_larger_eq(window_size, nums, target, le):
            if window_size == 0:
                return False
            for i in range(window_size - 1, le):
                if i >= window_size:
                    s = sums[i] - sums[i - window_size]
                else:
                    s = sums[i]
                if s >= target:
                    return True
            return False
        '''
        # option 1:
        def is_window_sum_larger_eq(window_size, nums, target, le):
            if window_size == 0:
                return False
            start = 0
            end = 0
            s = 0
            while end < le:
                s += nums[end]
                if end - start + 1 == window_size:
                    if s >= target:
                        return True
                    s -= nums[start]
                    start += 1
                end += 1
            return False
        '''
        left = 0
        right = le
        while left < right:
            mid = (left + right) // 2
            if is_window_sum_larger_eq(mid, nums, target, le):
                right = mid
            else:
                left = mid + 1
        if left == le and sum(nums) < target:
            return 0
        return left

        """ sliding window/滑动窗口 类似https://leetcode.cn/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode-solutio/
        我的 numbers 总结 模版 
        """
        window_size = 0
        start = 0
        end = 0
        le = len(nums)
        s = 0
        while end < le:
            s += nums[end]
            while s >= target:
                tmp = end - start + 1
                if window_size == 0:
                    window_size = tmp
                elif window_size > tmp:
                    window_size = tmp
                s -= nums[start]
                start += 1
            end += 1
        return window_size
        """ sliding window, 我的第一次解 但是复杂度较高 超时 """
        window_size = 0
        start = 0
        end = 0
        le = len(nums)
        while start < le and end < le:
            if sum(nums[start:end + 1]) < target:
                end += 1
            else:
                tmp = end - start + 1
                if window_size == 0:
                    window_size = tmp
                elif window_size > tmp:
                    window_size = tmp
                start += 1
        return window_size
