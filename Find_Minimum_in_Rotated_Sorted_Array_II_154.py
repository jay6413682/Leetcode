class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search,二分查找 旋转数组 https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/solution/er-fen-fa-fen-zhi-fa-python-dai-ma-by-liweiwei1419/
        left = 0
        n = len(nums)
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                '''
                # [1,1,3,1]这种情况 会一直往左边找，找到左侧的最小值 而不是右侧的
                right = right - 1
                '''
                # 相反下面我的方法，会找到最右侧的最小值 效率比较高
                if nums[right] >= nums[right - 1]:
                    right = right - 1
                else:
                    return nums[right]
        return nums[left]