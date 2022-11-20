# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """ binary search 二分查找 山脉数组 https://leetcode.cn/problems/find-in-mountain-array/solution/shi-yong-chao-hao-yong-de-er-fen-fa-mo-ban-python-/  """
        left = 0
        n = mountain_arr.length()
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        pivot = left
        #print(pivot)
        right = pivot
        left = 0
        while left < right:
            mid = (left + right) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val < target:
                left = mid + 1
            else:
                right = mid
        if mountain_arr.get(left) == target:
            return left
        left = pivot + 1
        right = n - 1
        while left < right:
            mid = (left + right + 1) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val < target:
                right = mid - 1
            else:
                left = mid
        if mountain_arr.get(left) == target:
            return left
        return -1
