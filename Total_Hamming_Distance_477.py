class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # bit manpulation. 按照476题的暴力法超时
        # https://leetcode.cn/problems/total-hamming-distance/solution/jie-xi-dong-tu-yan-shi-by-xiaohu9527-ipxt/
        # https://leetcode.cn/problems/total-hamming-distance/solution/gong-shui-san-xie-ying-yong-cheng-fa-yua-g21t/
        total_hamming_distance = 0
        n = len(nums)
        for i in range(0, 32):
            zero_counts = 0
            for j in nums:
                # 获取 x 的第 n 位值(0 或者 1)，(x >> n) & 1
                # 获取 x 的第 n 位的幂值，x & (1 << (n - 1))
                if j & (1 << i) == 0:  # or (j >> i) & 1 == 0
                    zero_counts += 1
            one_counts = n - zero_counts
            total_hamming_distance += zero_counts * one_counts
        return total_hamming_distance

        total_hamming_distance = 0
        for i in range(0, 32):
            zero_counts = 0
            one_counts = 0
            for j in nums:
                if j & (1 << i) == 0:
                    zero_counts += 1
                else:
                    one_counts += 1
            total_hamming_distance += zero_counts * one_counts
        return total_hamming_distance
