class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """ 其实就是longest common substring的变体
        dp[i][j] ：长度为i，末尾项为A[i-1]的子数组/子字符串，与长度为j，末尾项为B[j-1]的子数组/子字符串，二者的最大公共后缀子数组/子字符串长度。
        如果 A[i-1] != B[j-1]， 有 dp[i][j] = 0
        如果 A[i-1] == B[j-1] ， 有 dp[i][j] = dp[i-1][j-1] + 1
        https://leetcode.cn/problems/maximum-length-of-repeated-subarray/solution/zhe-yao-jie-shi-ken-ding-jiu-dong-liao-by-hyj8/
        https://zhuanlan.zhihu.com/p/68409952 
        """
        n = len(nums1)
        m = len(nums2)
        max_len = 0
        '''
        # before optimization
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[j - 1] == nums2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
        '''
        # after optimization
        dp = [0 for _ in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if nums1[j - 1] == nums2[i - 1]:
                    dp[j] = dp[j - 1] + 1
                    if dp[j] > max_len:
                        max_len = dp[j]
                else:
                    dp[j] = 0
        return max_len
