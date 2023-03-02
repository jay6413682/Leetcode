class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ 满足要求的最优解 快慢指针 链表 linked list https://leetcode.cn/problems/find-the-duplicate-number/solution/287xun-zhao-zhong-fu-shu-by-kirsche/ 
        时间复杂度：O(n)O(n)。「Floyd 判圈算法」时间复杂度为线性的时间复杂度。

        空间复杂度：O(1)O(1)。我们只需要常数空间存放若干变量。
        """
        slow_pointer = nums[0]
        fast_pointer = nums[nums[0]]
        while slow_pointer != fast_pointer:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]
        third_pointer = 0
        while slow_pointer != third_pointer:
            slow_pointer = nums[slow_pointer]
            third_pointer = nums[third_pointer]
        return slow_pointer


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ 二分查找 binary search (二分答案)
        https://leetcode.cn/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/
        n + 1 个整数，放在长度为 n 的数组里，根据「抽屉原理」，至少会有 1 个整数是重复的；
        使用「二分查找」查找一个整数，这是「二分查找」的典型应用，经常被称为「二分答案」。
        央视《幸运 52》节目的「猜价格游戏」，就是「二分答案」。玩家猜一个数字，如果猜中，游戏结束，如果主持人说「猜高了」，应该猜一个更低的价格，如果主持人说「猜低了」，应该猜一个更高的价格。
        时间复杂度：O(n\log n)O(nlogn)，其中 nn 为 \textit{nums}nums 数组的长度。二分查找最多需要二分 O(\log n)O(logn) 次，每次判断的时候需要O(n)O(n) 遍历 \textit{nums}nums 数组求解小于等于 \textit{mid}mid 的数的个数，因此总时间复杂度为 O(n\log n)O(nlogn)。
        空间复杂度：O(1)O(1)。我们只需要常数空间存放若干变量。

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
                # 或者这么想，[1 -> mid] 中 <= mid 的个数 <= mid, 那么 [mid + 1 -> n] 就有 >= (n + 1) - mid 个数，这个数 > [mid + 1 -> n]的不同数字个数 n - (mid + 1) + 1, 根据抽屉原理，重复数一定在 mid + 1 -> n
                left = mid + 1
        return left


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ bit manipulation https://leetcode.cn/problems/find-the-duplicate-number/solution/xun-zhao-zhong-fu-shu-by-leetcode-solution/
        时间复杂度：O(n\log n)O(nlogn)，其中 nn 为 \textit{nums}nums 数组的长度。O(\log n)O(logn) 代表了我们枚举二进制数的位数个数，枚举第 ii 位的时候需要遍历数组统计 xx 和 yy 的答案，因此总时间复杂度为 O(n\log n)O(nlogn)。

        空间复杂度：O(1)O(1)。我们只需要常数空间存放若干变量。

        """
        n = len(nums)
        max_possible_num = n - 1
        bit_count = 0
        while max_possible_num != 0:
            max_possible_num >>= 1
            bit_count += 1
        #print(bit_count)
        res = 0
        while bit_count > 0:
            s_num = s_i = 0
            which_bit = 1 << (bit_count - 1)
            for i, num in enumerate(nums):
                s_i += which_bit & i
                s_num += which_bit & num
            if s_num > s_i:
                res |= which_bit
            bit_count -= 1
        return res

