from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """ 暴力法，o(n^3) 复杂度 不推荐 """
        i = 0
        n = len(nums)
        while i < n - 2:
            j = i + 1
            while i < j < n - 1:
                k = j + 1
                while j < k < n:
                    if nums[i] < nums[k] < nums[j]:
                        return True
                    k += 1
                j += 1
            i += 1
        return False


class Solution1:
    def find132pattern(self, nums: List[int]) -> bool:
        """ 超出时间限制，暴力法：https://leetcode-cn.com/problems/132-pattern/solution/fu-xue-ming-zhu-cong-bao-li-qiu-jie-dao-eg78f/
        时间复杂度：O(N^2)O(N 2)
        空间复杂度：O(1)O(1)
        """
        n = len(nums)
        numsi = nums[0]
        for j in range(1, n):
            for k in range(j + 1, n):
                if nums[j] > nums[k] > numsi:
                    return True
            numsi = min(numsi, nums[j])
        return False


class Solution2:
    def find132pattern(self, nums: List[int]) -> bool:
        """ 单调栈 https://leetcode-cn.com/problems/132-pattern/solution/xiang-xin-ke-xue-xi-lie-xiang-jie-wei-he-95gt/
        Azson comment：官方题解讲得太多了，没看懂，这个看懂了 说下理解，就是单调栈维护的是3，max_k维护的是2，枚举的是1， max_k来源与单调栈，所以其索引一定大于栈顶的元素，但其值一定小于栈顶元素，故栈顶元素就是3，即找到了对“32”。 于是当出现nums[i] < max_k时，即找到了"12"，这个时候一定会有3个元素的，而栈顶3必定大于2，故也大于1，即满足“132”
        利用了单调栈，但是并不是 求next greater value，这是单调栈不同的一种应用
        """
        stack = deque()
        k = - 10 ** 9 - 1
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                k = max(stack.pop(), k)
            stack.append(nums[i])
        return False

        # my latest try
        n = len(nums)
        # stack ：非绝对单调递减栈，j 值 为stack[0]
        stack = []
        # k 值
        max_k_val = float(-inf)
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                max_k_val = max(nums[stack.pop()], max_k_val)
            if stack and nums[i] < max_k_val:
                return True
            stack.append(i)
        return False

        # 跟方法三一样，只是k 从前往后loop
        n = len(nums)
        mi = [nums[0]]
        for num in nums[1:]:
            mi.append(min(mi[-1], num))
        # mi: 前缀最小值, i 来自其中
        # stack：绝对单调递减栈 for j
        stack = []
        # k 值
        for k in range(1, n):
            while stack and nums[stack[-1]] <= nums[k]:
                stack.pop()
            # stack[-1] -> j
            if stack and nums[k] > mi[stack[-1] - 1]:
                return True
            stack.append(k)
        return False


class Solution3:
    def find132pattern(self, nums: List[int]) -> bool:
        """ 单调栈monotone stack 只用来解决Next Greater Element 问题
        https://leetcode-cn.com/problems/132-pattern/solution/132mo-shi-by-leetcode-2/ 的图解
        https://leetcode-cn.com/problems/132-pattern/solution/zhan-jie-fa-chao-xiang-xi-ti-jie-by-siyy/ 的图与文字
        https://github.com/labuladong/fucking-algorithm/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%B3%BB%E5%88%97/%E5%8D%95%E8%B0%83%E6%A0%88.md ：单调栈模版
        vector<int> nextGreaterElement(vector<int>& nums) {
            vector<int> res(nums.size()); // 存放答案的数组
            stack<int> s;
            // 倒着往栈里放
            for (int i = nums.size() - 1; i >= 0; i--) {
                // 判定个子高矮
                while (!s.empty() && s.top() <= nums[i]) {
                    // 矮个起开，反正也被挡着了。。。
                    s.pop();
                }
                // nums[i] 身后的 next great number
                res[i] = s.empty() ? -1 : s.top();
                // 
                s.push(nums[i]);
            }
            return res;
        }
        """
        mi = [nums[0]]
        for num in nums[1:]:
            mi.append(min(mi[-1], num))
        print(mi)
        stack = []
        j = len(nums) - 1
        while j >= 0:
            if nums[j] > mi[j]:
                while stack and stack[-1] <= mi[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
            j -= 1
        return False
