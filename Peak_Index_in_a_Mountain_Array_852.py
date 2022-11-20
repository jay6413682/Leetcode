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