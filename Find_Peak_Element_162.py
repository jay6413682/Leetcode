# search
# 搜索


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """ binary search
        https://leetcode-cn.com/problems/find-peak-element/solution/xun-zhao-feng-zhi-by-leetcode-solution-96sj/
        时间复杂度 : O\big(log_2(n)\big)O(log 2(n))。 每一步都将搜索空间减半。因此，总的搜索空间只需要 log_2(n)log 
        2(n) 步。其中 nn 为 numsnums 数组的长度。
        空间复杂度 : O(1)O(1)。 只使用了常数空间。
        证明 ： https://leetcode-cn.com/problems/find-peak-element/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-qva7v/
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        """ binary search
        https://leetcode-cn.com/problems/find-peak-element/solution/xun-zhao-feng-zhi-by-leetcode/
        时间复杂度 : O\big(log_2(n)\big)O(log2(n))。每一步都将搜索空间减半。因此，总的搜索空间只需要 log_2(n)log2(n) 步。其中 nn 为 numsnums 数组的长度。
        空间复杂度: O\big(log_2(n)\big)O(log 
2(n))。每一步都将搜索空间减半。因此，总的搜索空间只需要 log_2(n)log2(n) 步。于是，递归树的深度为 log_2(n)log 2(n)。

        """
        def search(nums, left, right):
            if left == right:
                return left
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
            return search(nums, left, right)
        return search(nums, 0, len(nums) - 1)


class Solution3:
    def findPeakElement(self, nums: List[int]) -> int:
        """ My own sliding window solution... O(n) less efficient """
        n = len(nums)
        if n == 1:
            return 0
        for i in range(n):
            if 1 <= i <= n - 2 and nums[i - 1] < nums[i] and nums[i] > nums[i + 1] or\
                    i == 0 and nums[i] > nums[i + 1] or\
                        i == n - 1 and nums[i - 1] < nums[i]:
                return i
