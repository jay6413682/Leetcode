class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # 二分答案 binary search https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/solution/er-fen-cha-zhao-ding-wei-chu-shu-by-liweiwei1419/ 
        # 最大是数组中最大的那个数，因为除数如果再大，整除以后每个数都得 1（上取整的缘故）；最小可以是 1。
        ma = max(nums)
        mi = 1
        left = mi
        right = ma
        while left < right:
            mid = (left + right) // 2
            s = 0
            for num in nums:
                # s += (num + mid - 1) // mid
                s += ceil(num / mid)
            if s > threshold:
                left = mid + 1
            else:
                right = mid
        return left