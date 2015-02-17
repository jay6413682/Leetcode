from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """  单调栈 monotone stack
        https://leetcode-cn.com/problems/next-greater-element-i/solution/dan-diao-zhan-jie-jue-next-greater-number-yi-lei-w/
        https://leetcode-cn.com/problems/next-greater-element-i/solution/gong-shui-san-xie-yi-ti-shuang-jie-bian-n6nwz/
        """
        # my solution, close to https://leetcode-cn.com/problems/next-greater-element-i/solution/gong-shui-san-xie-yi-ti-shuang-jie-bian-n6nwz/
        stack = deque()
        res = [None] * len(nums1)
        num_j_mapping = {}
        for j, num in enumerate(nums1):
            num_j_mapping[num] = j
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if nums2[i] in num_j_mapping:
                if stack and stack[-1] > nums2[i]:
                    res[num_j_mapping[nums2[i]]] = stack[-1]
                else:
                    res[num_j_mapping[nums2[i]]] = -1
            stack.append(nums2[i])
        return res
        '''
        # 我的解2，需要优化
        stack = []
        sub_res = []
        res = []
        for num1 in nums1:
            j = len(nums2) - 1
            i = nums2.index(num1)
            while j >= i:
                while stack and stack[-1] <= nums2[j]:
                    stack.pop()
                if stack:
                    sub_res.append(stack[-1])
                else:
                    sub_res.append(-1)
                stack.append(nums2[j])
                j -= 1
            res.append(sub_res[-1])
            stack = []
            sub_res = []
        return res
        '''
