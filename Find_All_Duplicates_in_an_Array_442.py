class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """ 原地hash
        类似 https://leetcode.cn/problems/find-all-duplicates-in-an-array/solution/by-ac_oier-0m3c/ 
        不用 if nums[i] not in res:，而是把nums[i]设成负数 再跳过负数，这样效率更高
        通解 见 https://leetcode.cn/problems/first-missing-positive/solution/tong-pai-xu-python-dai-ma-by-liweiwei1419/
        """
        n = len(nums)
        i = 0
        res = []
        while i < n:
            while nums[i] - 1 != i:
                if nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                else:
                    if nums[i] not in res:
                        res.append(nums[i])
                    break
            i += 1
        return res
        """
        # my latest try
        res = set()
        i = 0
        n = len(nums)
        while i < n:
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            if i != nums[i] - 1 and nums[i] == nums[nums[i] - 1]:
                res.add(nums[i])
            i += 1
        return list(res)
        """
