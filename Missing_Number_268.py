class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """ If nums = set(nums) is commented: time complexity is O(n2); space complexity is O(1)
        otherwise, time complexity is O(n); space complexity is O(n)
        Complexity of *in* operator in Python: 
        https://stackoverflow.com/questions/13884177/complexity-of-in-operator-in-python
        solution:
        https://leetcode-cn.com/problems/missing-number/solution/que-shi-shu-zi-by-leetcode/

        """

        # nums = set(nums)
        n = len(nums)
        i = 0
        while i < n + 1:
            if i not in nums:
                return i
            i += 1


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        """ bit manipulation
        https://leetcode-cn.com/problems/missing-number/solution/diu-shi-de-shu-zi-by-leetcode-solution-naow/
        time complexity: O(n), space complexity: O(1)
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
        """
        # my own solution
        n = len(nums)
        missing = 0
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing ^ n
        """


class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        """ 根据高斯求和公式 Gauss sum
        https://leetcode-cn.com/problems/missing-number/solution/diu-shi-de-shu-zi-by-leetcode-solution-naow/

        time complexity: O(n), space complexity: O(1)
        """
        sum = 0
        for num in nums:
            sum += num
        return len(nums) * (len(nums) + 1) // 2 - sum
        '''
        # my solution
        n = len(nums)
        range_total = n * (n + 1) // 2
        res = range_total
        for i in nums:
            res = res - i
        return res
        '''
