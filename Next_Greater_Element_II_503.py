from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """ monotone stack/单调栈
        double the given nums: https://leetcode-cn.com/problems/next-greater-element-i/solution/dan-diao-zhan-jie-jue-next-greater-number-yi-lei-w/ not efficient """
        n = len(nums)
        nums = 2 * nums
        i = 2 * n - 1
        stack = []
        res = []
        while i >= 0:
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res.insert(0, stack[-1])
            else:
                res.insert(0, -1)
            stack.append(nums[i])
            i -= 1
        return res[:n]


class Solution2:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """ https://leetcode-cn.com/problems/next-greater-element-i/solution/dan-diao-zhan-jie-jue-next-greater-number-yi-lei-w/ """
        stack = []
        n = len(nums)
        res = [-1] * n
        i = 2 * n - 1
        while i >= 0:
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            if stack:
                res[i % n] = stack[-1]
            else:
                res[i % n] = -1
            stack.append(nums[i % n])
            i -= 1
        return res
        """
        # my try number 2
        n = len(nums)
        res = [None] * n
        stack = deque()
        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            res[i % n] = stack[-1] if stack else -1
            stack.append(nums[i % n])
        return res
        """

