class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """ greedy 贪心 my own solution similar to https://leetcode.cn/problems/wiggle-subsequence/solution/python3-yi-tu-sheng-qian-yan-by-v12de-ao-72b1/
        也可用动态规划
        """
        res = 0
        i = 1
        pre_direction = 0
        curr_direction = 0
        while i < len(nums):
            if nums[i] > nums[i - 1]:
                curr_direction = 1
                if curr_direction != pre_direction:
                    res += 1
                    pre_direction = curr_direction
            elif nums[i] < nums[i - 1]:
                curr_direction = -1
                if curr_direction != pre_direction:
                    res += 1
                    pre_direction = curr_direction
            i += 1
        res += 1
        return res
