class Solution:
    def findMin(self, nums: List[int]) -> int:
        """ binary search
        https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-5irwp/
        时间复杂度：时间复杂度为 O(\log n)O(logn)，其中 nn 是数组 \textit{nums}nums 的长度。在二分查找的过程中，每一步会忽略一半的区间，因此时间复杂度为 O(\log n)O(logn)。

        空间复杂度：O(1)O(1)。
        详解：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/er-fen-cha-zhao-wei-shi-yao-zuo-you-bu-dui-cheng-z/
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # if nums[mid] == nums[left]:
            #    print('1 mid: {}, {}, {}'.format(nums[mid], nums[left], nums[right]))
            #    return nums[mid] if nums[mid] < nums[right] else nums[right]
            # elif nums[mid] == nums[right]:
            #    print('2 mid: {}, {}, {}'.format(nums[mid], nums[left], nums[right]))
            #    return nums[mid] if nums[mid] < nums[left] else nums[left]
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
            # elif nums[mid] < nums[right]:
                right = mid
        return nums[left]
