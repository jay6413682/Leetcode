class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # 二分查找 binary search 山脉数组 https://leetcode.cn/problems/peak-index-in-a-mountain-array/solution/gong-shui-san-xie-er-fen-san-fen-cha-zhi-5gfv/ 根据arr[i] 与 arr[i+1] 大小确定 单调范围 画图辅助
        left = 0
        n = len(arr)
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # binary search 二分查找 比较mid 和 right / left 也可以 但是时间复杂度比较高
        n = len(arr)
        left = 1
        right = n - 2
        while left < right:
            mid = (left + right + 1) // 2
            if arr[mid] < arr[left]:
                right = mid - 1
            else:
                left = left + 1
        '''
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[right]:
                left = mid + 1
            else:
                right = right - 1
        '''
        return left
