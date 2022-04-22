class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        """ https://leetcode-cn.com/problems/binary-search/solution/er-fen-cha-zhao-by-leetcode-solution-f0xw/
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ https://leetcode-cn.com/problems/binary-search/solution/python-di-gui-xie-fa-by-zedong/
        master theory:
        time complexity: log(n); space complexity: stack, log(n)
        """
        def binary_search(nums, target, start, end):
            if start > end:
                return -1
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(nums, target, start, mid - 1)
            else:
                return binary_search(nums, target, mid + 1, end)
        return binary_search(nums, target, 0, len(nums) - 1)
