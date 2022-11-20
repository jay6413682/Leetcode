class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """ 原地hash
        类似 https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/solution/shou-hua-tu-jie-jiao-huan-shu-zi-zai-ci-kzicg/
        通解 见 https://leetcode.cn/problems/first-missing-positive/solution/tong-pai-xu-python-dai-ma-by-liweiwei1419/
        """
        i = 0
        n = len(nums)
        res = []
        while i < n:
            while nums[i] - 1 != i and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            i += 1
        for i, num in enumerate(nums):
            if num != i + 1:
                res.append(i + 1)
        return res
