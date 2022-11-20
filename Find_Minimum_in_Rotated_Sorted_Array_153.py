class Solution1:
    def findMin(self, nums: List[int]) -> int:
        '''
        最新解
        二分查找 binary search 旋转数组
        分析旋转数组的特点
        多次旋转等价于旋转一次；
        只会有一次「转折」，一分为二看，一定有一段是有序的；
        重点理解 1：最大值和最小值「相邻」：即：最大值的右边，如果有的话，一定是最小值；
        重点理解 2：如果两点是「上升」的，那么两点之间一定是「上升」的。
        所以比较mid 和 left 或 right 来确定单调范围
        https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solution/er-fen-fa-fen-zhi-fa-python-dai-ma-java-dai-ma-by-/
        '''
        left = 0
        n = len(nums)
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            '''
            # nums 没有旋转 或者 mid ，right 都在pivot 右侧
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
            '''
            # or: if nums[mid] > nums[right] 一定是 mid 在 pivot 左侧，right 在pivot 右侧
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        '''
        # my solution, 类似 夜猫腾 的comment
        left = 0
        n = len(nums)
        right = n - 1
        # nums[0] < nums[n - 1]：没有rotate，最小值在最左边
        if nums[0] < nums[n - 1]:
            return nums[0]
        while left < right:
            mid = (left + right) // 2
            # nums[mid] < nums[0]: mid 在pivot 右侧, 最小值 在mid 左侧
            # 否则如果mid 在pivot 左侧，则最小值一定在mid 右侧
            if nums[mid] < nums[0]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
        '''
        '''
        # optimization try 2:
        left = 0
        n = len(nums)
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            # 设 由大到小的点为pivot point
            # nums[mid] < nums[left]: left 在 pivot 左边，mid 和 right 在 pivot 右边；最小值在mid 左边
            # nums[right] < nums[0] and nums[left] < nums[0]：left 和 right 都在piviot 右边；最小值在mid 左边
            # nums[0] <= nums[right] <= nums[n - 1]：数组没有rotate，最小值在mid 左边
            if nums[mid] < nums[left] or (nums[right] < nums[0] and nums[left] < nums[0]) or nums[0] <= nums[right] <= nums[n - 1]:
                right = mid
            else:
                left = mid + 1
            
        return nums[left]
        '''
        '''
        # unoptimized try num 1
        left = 0
        n = len(nums)
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            # 设 由大到小的点为pivot point
            # nums[mid] < nums[left]: left 在 pivot 左边，mid 和 right 在 pivot 右边；最小值在mid 左边
            # nums[mid] > nums[right]: mid 在pivot 左边，right 在 pivot 右边，最小值在mid 右边
            # nums[right] < nums[0]：mid left 和 right 都在piviot 右边；最小值在mid 左边
            # nums[right] > nums[n - 1]： mid left 和 right 都在 piviot 左边；最小值在mid 右边
            # nums[0] <= nums[right] <= nums[n - 1]：数组没有rotate，最小值在mid 左边
            if nums[mid] < nums[left]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            elif nums[right] < nums[0]:
                right = mid
            elif nums[right] > nums[n - 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        '''


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
