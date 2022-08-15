from typing import List

class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ 单调栈，类似 https://leetcode.cn/problems/next-greater-element-i/solution/dong-hua-yan-shi-dan-diao-zhan-496xia-yi-ql65/ 和 https://leetcode.cn/problems/next-greater-element-i/solution/gong-shui-san-xie-yi-ti-shuang-jie-bian-n6nwz/

        如果正序遍历，每一个循环，stack 中的数是 nums[i] 左侧比它大的 数，同时单调递减：这个更好理解, 记这个
        如果逆序遍历，每一个循环，stack 中的数是 nums[i] 右侧比它大的 数，同时单调递减：在头脑中想象，栈就是从右向左由高到低排队的人（相当于栈中数字左右翻转），当nums[i] 大于队中矮的人（栈顶元素），矮人弹出，直到队中都比它高，它再入栈 
        
        """
        def sequential_get_next_greater_element_map(nums):
            stack = []
            # num -> index of next greater element
            mapping = {}
            for i in range(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    popped_i = stack.pop()
                    mapping[nums[popped_i]] = i
                stack.append(i)
            return mapping

        def reversal_get_next_greater_element_map(nums):
            stack = []
            # num -> index of next greater element
            mapping = {}
            for i in range(len(nums) - 1, -1, -1):
                while stack and nums[stack[-1]] <= nums[i]:
                    stack.pop()
                if stack:
                    mapping[nums[i]] = stack[-1]
                stack.append(i)
            return mapping

        #next_greater_element_map = sequential_get_next_greater_element_map(nums2)
        next_greater_element_map = reversal_get_next_greater_element_map(nums2)
        # print(next_greater_element_map)
        res = []
        for num in nums1:
            nums2_i = next_greater_element_map.get(num)
            # print(nums2_i)
            if nums2_i:
                res.append(nums2[nums2_i])
            else:
                res.append(-1)
        return res


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
