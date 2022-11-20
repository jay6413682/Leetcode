

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """ inversion pair, 逆序对，归并排序 ：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/ 视频 
        注意：其实有两种方法：方法1 左边大时，数出每一个数前面有多少个数比它大（下面我的写法），方法二，左边小时 数出每一个数后面有多少个数比它小 https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/bao-li-jie-fa-fen-zhi-si-xiang-shu-zhuang-shu-zu-b/ 
        """
        count = 0
        def merge_sort(nums, left, right):
            # special case
            nonlocal count
            if left == right:
                return
            mid = (left + right) // 2
            # divide
            merge_sort(nums, left, mid)
            merge_sort(nums, mid + 1, right)

            if nums[mid] <= nums[mid + 1]:
                return
            
            i = left
            j = mid + 1
            tmp = nums.copy()
            k = i
            while i <= mid and j <= right:
                if nums[i] > nums[j]:
                    # 左大
                    tmp[k] = nums[j]
                    j += 1
                    count += (mid - i + 1)
                    #print('>',count, k,j, left, mid, right, (j - (mid + 1)))
                else:
                    # 左小
                    tmp[k] = nums[i]
                    i += 1
                k += 1
            current_i = i
            while i <= mid:
                tmp[k] = nums[i]
                k += 1
                i += 1
            while j <= right:
                tmp[k] = nums[j]
                k += 1
                j += 1
            for i in range(left, right + 1):
                nums[i] = tmp[i]
            #print(nums)
        if not nums:
            return count
        merge_sort(nums, 0, len(nums) - 1)
        #print(nums)
        return count
        '''
        # my solution... hard to implement
        count = 0
        def merge_sort(nums, left, right):
            # special case
            nonlocal count
            if left == right:
                return
            mid = (left + right) // 2
            # divide
            merge_sort(nums, left, mid)
            merge_sort(nums, mid + 1, right)

            if nums[mid] <= nums[mid + 1]:
                return
            
            i = left
            j = mid + 1
            tmp = nums.copy()
            k = i
            go_left = False
            while i <= mid and j <= right:
                if nums[i] > nums[j]:
                    # 左大
                    tmp[k] = nums[j]
                    if go_left is False:
                        count += (j - mid)
                    else:
                        count += 1
                    j += 1
                    go_left = True
                    #print('>',count, k,j, left, mid, right, (j - (mid + 1)))
                else:
                    # 左小
                    tmp[k] = nums[i]
                    if go_left is False:
                        count += (j - (mid + 1))
                    if go_left:
                        go_left = False
                    
                    #print('<',count, k,j, left, mid, right, (j - (mid + 1)))
                    i += 1
                k += 1
            current_i = i
            while i <= mid:
                tmp[k] = nums[i]
                k += 1
                i += 1
                if i > current_i + 1:
                    count += (right - mid)
                    #print(count, left, mid, right, right - mid)
            while j <= right:
                tmp[k] = nums[j]
                k += 1
                j += 1
            for i in range(left, right + 1):
                nums[i] = tmp[i]
            #print(nums)
        if not nums:
            return count
        merge_sort(nums, 0, len(nums) - 1)
        #print(nums)
        return count
        '''    