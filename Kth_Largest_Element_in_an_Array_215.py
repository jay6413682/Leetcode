

class Solution1:
    def quick_select(self, nums, left, right, k, length):
        """ my iterative solution, quick sort, 双指针 https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/partitionfen-er-zhi-zhi-you-xian-dui-lie-java-dai-/
        time complexity: O(n), master theorem； space complexity: O(logn)
        """
        if left == right and left == length - k:
            return left
        mid = (left + right) // 2
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[mid] < nums[left]:
            nums[left], nums[mid] = nums[mid], nums[left]
        if nums[mid] > nums[right]:
            nums[mid], nums[right] = nums[right], nums[mid]
        nums[mid], nums[right - 1] = nums[right - 1], nums[mid]
        pivot = right - 1
        i = left
        j = pivot - 1
        while i <= j:
            while nums[i] <= nums[pivot] and i <= j:
                i += 1
            while nums[j] >= nums[pivot] and i <= j:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[pivot] = nums[pivot], nums[i]
        return i

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        index_to_look = n - k
        while True:
            i = self.quick_select(nums, left, right, k, n)
            if i == index_to_look:
                return nums[i]
            elif i < index_to_look:
                left = i + 1
            else:
                right = i - 1


class Solution:
    def quick_select(self, nums, left, right, k, length):
        """ my recursive solution, quick sort, 双指针 similar to https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/shu-zu-zhong-de-di-kge-zui-da-yuan-su-by-leetcode-/ 但是该解为单指针
        双指针见我的912题解
        time complexity: O(n), master theorem； space complexity: O(logn)
        """
        if left == right and left == length - k:
            return nums[left]
        mid = (left + right) // 2
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[mid] < nums[left]:
            nums[left], nums[mid] = nums[mid], nums[left]
        if nums[mid] > nums[right]:
            nums[mid], nums[right] = nums[right], nums[mid]
        nums[mid], nums[right - 1] = nums[right - 1], nums[mid]
        pivot = right - 1
        i = left
        j = pivot - 1
        while i <= j:
            while nums[i] <= nums[pivot] and i <= j:
                i += 1
            while nums[j] >= nums[pivot] and i <= j:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[pivot] = nums[pivot], nums[i]
        index_to_look = length - k
        if i == index_to_look:
            # print(nums, i)
            return nums[i]
        elif i < index_to_look:
            # print(index_to_look, nums, i + 1, right, k, length)
            return self.quick_select(nums, i + 1, right, k, length)
        else:
            # print(index_to_look, nums, left, i - 1, k, length)
            return self.quick_select(nums, left, i - 1, k, length)
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        return self.quick_select(nums, 0, n - 1, k, n)


import heapq

class Solution3:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ priority queue, heap sort solution; similar to https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/partitionfen-er-zhi-zhi-you-xian-dui-lie-java-dai-/
        复杂度：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/shu-zu-zhong-de-di-kge-zui-da-yuan-su-by-leetcode-/
        https://sisyphus.gitbook.io/project/python-notes/python-priority-queue-heapq 
        时间复杂度：O(n \log n)O(nlogn)，建堆的时间代价是 O(n)O(n)，删除的总代价是 O(k \log n)O(klogn)，因为 k < nk<n，故渐进时间复杂为 O(n + k \log n) = O(n \log n)O(n+klogn)=O(nlogn)。
        """

        '''
        # jerry4free/Jerry Tsek comment: 如果超过一半时，其实可反过来找len-k+1个最小元素，即是第k个最大元素 这样堆的空间复杂度会小
        nums_heap = []
        n = len(nums)
        mid = (n - 1) // 2
        if k <= mid + 1:
            for i in range(k):
                heapq.heappush(nums_heap, nums[i])
            for i in range(k, n):
                if nums_heap[0] < nums[i]:
                    heapq.heapreplace(nums_heap, nums[i])
            return nums_heap[0]
        else:
            for i in range(n - k + 1):
                # https://stackoverflow.com/questions/48255849/how-to-get-the-max-heap-in-python
                heapq.heappush(nums_heap, -1 * nums[i])
            # print(nums_heap)
            for i in range(n - k + 1, n):
                if nums_heap[0] < -1 * nums[i]:
                    heapq.heapreplace(nums_heap, -1 * nums[i])
            return -1 * nums_heap[0]
        '''
        # w4irdo's solution, time complexity is n*lgk
        n = len(nums)
        heap_nums = []
        for num in nums:
            length = len(heap_nums)
            # print(length, k, num, heap_nums)
            if length == k and num <= heap_nums[0]:
                continue
            heapq.heappush(heap_nums, num)
            if length + 1 > k:
                heapq.heappop(heap_nums)
        return heap_nums[0]
        """
        heap_nums = []
        length = len(nums)
        for n in nums:
            heapq.heappush(heap_nums, n)
        i = 0
        while i < length - k + 1:
            res = heapq.heappop(heap_nums)
            # print(res)
            i += 1
        return res
        """


import heapq

class Solution4:

    def sift_down(self, nums, start, end):
        """ max heap """
        x = start + 1
        y = end + 1
        z = 2 * x
        while z <= y:
            if z <= end and nums[z - 1] < nums[z]:
                z += 1
            if nums[x - 1] < nums[z - 1]:
                # swap
                nums[x - 1], nums[z - 1] = nums[z - 1], nums[x - 1]
                x = z
                z = x * 2
            else:
                break

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ priority queue, heap sort solution; similar to https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/shu-zu-zhong-de-di-kge-zui-da-yuan-su-by-leetcode-/
        912题解
        复杂度：https://leetcode-cn.com/problems/sort-an-array/solution/fu-xi-ji-chu-pai-xu-suan-fa-java-by-liweiwei1419/
        或可从其recursive solution 通过master theory 求得
        时间复杂度：时间复杂度稳定在O(nlogn)O(nlogn)，因为在构建堆的时候时间遍历数组对于每个元素需要进行O(logn)O(logn)次比较，时间复杂度是O(nlogn)O(nlogn)。在弹出每个元素重建堆需要O(logn)O(logn)的复杂度，时间复杂度也是O(klogn)O(klogn)，所以整体的时间复杂度是O(nlogn)O(nlogn)
        空间复杂度：O（1）
        """

        n = len(nums)
        sub_roots = n // 2
        # heapify
        for i in range(sub_roots, -1, -1):
            self.sift_down(nums, i, n - 1)
        print(nums)
        for j in range(k):
            # swap
            nums[0], nums[n - j - 1] = nums[n - j - 1], nums[0]
            # 下标 0 位置下沉操作，使得区间 [0, n - j - 2] 堆有序
            self.sift_down(nums, 0, n - j - 2)
            # print(nums)
        return nums[-k]
