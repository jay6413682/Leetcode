class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """ binary search / 二分查找 https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/solution/er-fen-cha-zhao-by-liweiwei1419/ 
        类似 33 题，现根据 mid 和 right / left 比较 确定单调区间，然后分情况讨论
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid
            elif nums[mid] < nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
            else:
                if nums[mid] == target:
                    return True
                # 下面是我的解 比较优化, 也可直接 right = right - 1
                if nums[right] != nums[left]:
                    right = mid - 1
                else:
                    right = right - 1
        return True if nums[left] == target else False