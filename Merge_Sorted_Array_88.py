class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        the merge step of of merge sort
        https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetco-rrb0/
        时间复杂度：O(m+n)O(m+n)。
        指针移动单调递增，最多移动 m+nm+n 次，因此时间复杂度为 O(m+n)O(m+n)。

        空间复杂度：O(m+n)O(m+n)。
        需要建立长度为 m+nm+n 的中间数组 \textit{sorted}sorted。

        """
        """
        # my solution, without new array; slicing, so more time complexity
        i = 0
        j = 0
        while i < m + n and j < n:
            # print(i, j)
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1[i:] = [nums2[j]] + nums1[i:m + n - 1]
                # print(nums1)
                i += 1
                j += 1
        if i == m + n:
            nums1[m + j:] = nums2[j:n]
            # print('out: {}'.format(nums1))
        return nums1
        """
        '''
        # my solution
        i = 0
        j = 0
        nums1_counter = 0
        while j < n:
            if nums1_counter == m:
                nums1[i] = nums2[j]
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
                i += 1
            else:
                nums1_counter += 1
                i += 1
        return nums1
        '''
        i = 0
        j = 0
        merged = []
        while i < m or j < n:
            if i >= m:
                merged.append(nums2[j])
                j += 1
            elif j >= n:
                merged.append(nums1[i])
                i += 1
            elif nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                merged.append(nums2[j])
                j += 1
        # print(merged)
        nums1[:] = merged

