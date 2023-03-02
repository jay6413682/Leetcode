class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ 二分查找 binary search 我最新的解 mid与left right 都比较的写法，比較麻煩 """
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid] <= nums[right]:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            if nums[mid] < nums[left]:
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            if nums[mid] > nums[right]:
                if nums[mid] < target or target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        print(left)
        if nums[left] == target:
            return left
        return -1


class Solution5:
    def search(self, nums: List[int], target: int) -> int:
        """ 最新解，二分查找 binary search. 利用 局部单调性，逐步缩小搜索区间。
        https://leetcode.cn/problems/search-in-rotated-sorted-array/solution/er-fen-fa-python-dai-ma-java-dai-ma-by-liweiwei141/
        moffysto的解
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # 形成mid -- target -- right 的单调区间
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                # 形成left -- target -- mid 的单调区间
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
        return left if nums[left] == target else -1
        '''
        # my latest try, compare mid with left
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
        #print(left)
        if nums[left] == target:
            return left
        return -1
        '''
                

class Solution4:
    """
    My own solution, 根据模版二：https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
    """
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            # print(left, right, mid)
            if nums[left] < nums[mid]:
                # 下面这些判断很难一次得出，应该写出所有可能性，再合并
                """
                if target < nums[mid] and target > nums[right]:
                    right = mid - 1
                elif target >= nums[mid]:
                    left = mid
                elif target < nums[mid] and target <= nums[right]:
                    if target < nums[left]:
                        left = mid
                    else:
                        right = mid - 1
                """
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid
            else:
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid] and target > nums[right]:
                    right = mid - 1
                else:
                    left = mid
        if nums[left] == target:
            return left
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ 对于有序或部分有序，基本使用二分搜索及其变种；非排除法，left <= right
        binary search: https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/
        视频为recursive 解：https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/ 
        wangzhen：
        将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
        此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环. 
        复杂度分析

        时间复杂度： O(\log n)O(logn)，其中 nn 为 \textit{nums}nums 数组的大小。整个算法时间复杂度即为二分查找的时间复杂度 O(\log n)O(logn)。

        空间复杂度： O(1)O(1) 。我们只需要常数级别的空间存放变量。

        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # mid左侧有序
            if nums[mid] > nums[left]:
                # target的值在左半边
                if target > nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # mid 右侧有序
            else:
                # target的值在右半边
                if target > nums[mid] and target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        """ my own solution; 类似binary search: https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/
        复杂度分析

        时间复杂度： O(\log n)O(logn)，其中 nn 为 \textit{nums}nums 数组的大小。整个算法时间复杂度即为二分查找的时间复杂度 O(\log n)O(logn)。

        空间复杂度： O(1)O(1) 。我们只需要常数级别的空间存放变量。

        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[mid] > target:
                if nums[mid] < nums[left]:
                    right = mid - 1
                elif target > nums[left]:
                    right = mid - 1
                else:
                # elif target < nums[left]:
                    left = mid + 1
            else:
                if nums[mid] > nums[left]:
                    left = mid + 1
                elif target < nums[right]:
                    left = mid + 1
                else:
                # elif target > nums[right]:
                    right = mid - 1 
        return -1


class Solution3:
    def findMinIndex(self, nums: List[int]) -> int:
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
        return left

    def bin_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
            

    def search(self, nums: List[int], target: int) -> int:
        """ 思路一/方法一：https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/duo-si-lu-wan-quan-gong-lue-bi-xu-miao-dong-by-swe/ """
        min_index = self.findMinIndex(nums)
        left = 0
        right = len(nums) - 1
        if target == nums[right]:
            return right
        elif target < nums[right]:
            raw_index = self.bin_search(nums[min_index:], target)
            if raw_index == -1:
                return raw_index
            return min_index + raw_index
        else:
            return self.bin_search(nums[:min_index], target)
