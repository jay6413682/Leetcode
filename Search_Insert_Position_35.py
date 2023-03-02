'''
Created on Jul 21, 2015

@author: ljiang
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples. [1,3,5,6],5->2 [1,3,5,6], 2->1 [1,3,5,6], 7->4 [1,3,5,6], 0->0

'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """ 我的最新解 binary search/二分查找，类似34题，https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/solution/si-lu-hen-jian-dan-xi-jie-fei-mo-gui-de-er-fen-cha/1437835/
        看我Numbers里总结的模版！
        """
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            '''
            情况 1：如果当前 mid 看到的数值严格小于 target，那么 mid 以及 mid 左边的所有元素就一定不是「插入元素的位置」，因此下一轮搜索区间是 [mid + 1..right]，下一轮把 left 移动到 mid + 1 位置，因此设置 left = mid + 1；
情况 2：否则，如果 mid 看到的数值大于等于 target，那么 mid 可能是「插入元素的位置」，mid 的右边一定不存在「插入元素的位置」。如果 mid 的左边不存在「插入元素的位置」，我们才可以说 mid 是「插入元素的位置」。因此下一轮搜索区间是 [left..mid]，下一轮把 right 移动到 mid 位置，因此设置 right = mid。
说明：上面的两点中，「情况 2」其实不用分析得那么细致， 因为只要「情况 1」的区间分析是正确的，「情况 2」一定是「情况 1」得到的区间的反面区间。
            '''
            # mid 不可能 为 len(nums)，否则left 一定 已经 == right 了 比如 1,2,3 , mid = 2, right = 3, left = 2, 无论nums[mid] < target 还是 nums[mid] >= target, left 都会 == right，然后break the loop
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """ 模版一，binary search: O(logn); O(1) """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        模版二，binary search, binary search 通解详解:
        题目要我们返回第 1 个 大于等于 目标元素 2 的下标（分析出这一点非常重要），
        https://leetcode-cn.com/problems/search-insert-position/solution/te-bie-hao-yong-de-er-fen-cha-fa-fa-mo-ban-python-/
        O(logn);log(1)
        right 也可 初始化成 len(nums)，因为这也是可能结果，是搜索范围
        """
        if nums[-1] < target:
            return len(nums)
        left = 0
        right = len(nums) - 1
        # 在区间 nums[left..right] 里查找第 1 个大于等于 target 的元素的下标
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            # nums[mid] >= target，正好满足条件
            else:
                right = mid
        return right


class Solution3:
    """ 我的解，类似solution 2  这个方法不好因为最后还要判断; 看不懂就算了 """ 
    def searchInsert(self, nums: List[int], target: int) -> int:
        # less than the smallest
        if target < nums[0]:
            return 0
        left = 0
        right = len(nums) - 1
        # 在区间 nums[left..right] 里查找第 1 个大于等于 target 的元素的下标
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            # nums[mid] <= target
            else:
                left = mid
        # if there is nums[mid] == target
        if nums[left] == target:
            return left
        # if there is no nums[mid] == target
        return left + 1


class Search_Insert_Position_48:
    def __init__(self,lst,target):
        self.lst=lst
        self.target=target
    def search_and_insert(self):
        pass
        left=0
        right=len(self.lst)-1
        mid=(left+right)/2
        
        while left<right:
            if self.lst[mid] == self.target:
                return mid
            elif self.target<self.lst[mid]:
                right=mid
            elif self.target>self.lst[mid]:
                left=mid+1
            mid=(left+right)/2
                
        if self.lst[mid]>self.target:
            return mid
        else:
            return mid+1
            
                
            