class Solution3:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # my latest solution
        # binary search/ 二分查找 https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solution/si-lu-hen-jian-dan-xi-jie-fei-mo-gui-de-er-fen-cha/1437835/ 
        # to avoid right < 0, which is invalid
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        # 找target 第一次出现的位置
        res = []
        while left < right:
            mid = (left + right) // 2
            """
            情况 1 ：当 nums[mid] < target 时

            mid 一定不是 target 第一次出现的位置；
            由于数组有序，mid 的左边一定比 nums[mid] 还小，因此 mid 的左边一定不是 target 第一次出现的位置；
            mid 的右边比 nums[mid] 还大，因此 mid 的右边 有可能 存在 target 第一次出现的位置。
            因此下一轮搜索区间是 [mid + 1..right]，此时设置 left = mid + 1；

            情况 2 ：当 nums[mid] == target 时

            mid 有可能是 target 第一次出现的位置；
            mid 的左边也有可能是 target 第一次出现的位置；
            mid 的右边一定不是 target 第一次出现的位置。
            因此下一轮搜索区间在 [left..mid]，此时设置 right = mid。

            情况 3 ：当 nums[mid] > target 时

            mid 一定不是 target 第一次出现的位置；
            mid 的右边也一定不是 target 第一次出现的位置；
            mid 的左边有可能是 target 第一次出现的位置，因此下一轮搜索区间在 [left..mid - 1]，此时设置 right = mid - 1。
            重点在这里：把情况 ② 和情况 ③ 合并，即当 nums[mid] >= target 的时候，下一轮搜索区间是 [left..mid]，此时设置 right = mid。这样做是因为：只有当区间分割是 [left..mid] 和 [mid + 1..right] 的时候，while(left < right) 退出循环以后才有 left == right 成立。

            这里 有一个例子，说明如果分成三个部分，退出循环以后 left 与 right 不能重合；
            """
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return [-1, -1]
        l_bound = left
        # optimization: 搜索 l_bound -> len(nums) - 1
        right = len(nums) - 1
        # 找target 最后一次出现的位置
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        r_bound = right
        res = [l_bound, r_bound]
        return res


class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """ binary search, 模版一
        https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/da-jia-bu-yao-kan-labuladong-de-jie-fa-fei-chang-2/
        模版三本质和模版一一样，不要记
        """
        start, end = -1, -1
        if not nums:
            return [start, end]
        n = len(nums)
        def get_start_index(nums, target):
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                # cannot do nums[mid] == target
                # because it will cause infinite loop
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            if left != n and nums[left] == target:
                return left
            return -1
        def get_end_index(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            if right != -1 and nums[right] == target:
                return right
            return -1
        start = get_start_index(nums, target)
        if start != -1:
            end = get_end_index(nums, target)
        return [start, end]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """ 模版2: https://leetcode-cn.com/leetbook/read/binary-search/xerqxt/
        视频解：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/zai-pai-xu-shu-zu-zhong-cha-zhao-yuan-su-de-di-3-4/
        时间复杂度： O(\log n)O(logn) ，其中 nn 为数组的长度。二分查找的时间复杂度为 O(\log n)O(logn)，一共会执行两次，因此总时间复杂度为 O(\log n)O(logn)。

        空间复杂度：O(1)O(1) 。只需要常数空间存放若干变量。
        为何 (left + right + 1) // 2:
        自己的一点见解，分享一下 在下一次迭代区间不包含mid,即[left, mid-1] 或者[mid+1, right] 这种情况下，是不需要关注mid的取值问题的，因为无论是上取，还是下取，都不会有死循环的发生。反之，如果下一次迭代区间包含mid，就要注意了， 假如是[left, mid], 此时left 需要下取， 因为mid如果上取，假如判断条件一直卡在mid = (left + mid + 1)/2 == mid， 就会死循环。类似的， 如果是[mid, right],此时需要上取
        https://leetcode-cn.com/leetbook/read/learning-algorithms-with-leetcode/xs41qg/
        """
        start, end = -1, -1
        if not nums:
            return [start, end]
        def get_start_index(nums, target):
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            if nums[left] == target:
                return left
            return -1
        def get_end_index(nums, target):
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] == target:
                    left = mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            if nums[right] == target:
                return right
            return -1
        start = get_start_index(nums, target)
        if start != -1:
            end = get_end_index(nums, target)
        return [start, end]
