class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """ binary search/二分答案/二维前缀和（Prefix Sum）解法类似 https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/solution/qing-xi-tu-jie-mo-neng-de-qian-zhui-he-by-hlxing/ extra101 的comment 
        https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/solution/yuan-su-he-xiao-yu-deng-yu-yu-zhi-de-zheng-fang-2/ 
        区别在于 我的解中 prefix_sum[i][j] 是包含 mat[i][j] 的前缀和，而其他解 prefix_sum[i][j] 其实对应的是 包含mat[i-1][j-1]的前缀和，这就造成我下面解法要做很多判断
        """
        width = len(mat[0])
        height = len(mat)
        max_side_len = width if width < height else height
        left = 0
        right = max_side_len
        prefix_sum = [[0 for j in range(width)] for i in range(height)]
        
        for i in range(0, height):
            for j in range(0, width):
                if i == 0 and j ==0:
                    prefix_sum[0][0] = mat[0][0]
                elif i == 0:
                    prefix_sum[i][j] = prefix_sum[i][j - 1] + mat[i][j]
                elif j == 0:
                    prefix_sum[i][j] = prefix_sum[i - 1][j] + mat[i][j]
                else:
                    prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + mat[i][j]
        #print(prefix_sum)
        while left < right:
            mid = (left + right + 1) // 2
            s = 0
            found = False
            for i in range(0, height - mid + 1):
                for j in range(0, width - mid + 1):
                    if i == 0 and j == 0:
                        s = prefix_sum[mid - 1][mid - 1]
                    elif i == 0:
                        s = prefix_sum[mid - 1][j + mid - 1] - prefix_sum[mid - 1][j - 1]
                    elif j == 0:
                        s = prefix_sum[i + mid - 1][mid - 1] - prefix_sum[i - 1][j + mid - 1]
                    else:
                        s = prefix_sum[i + mid - 1][j + mid - 1] - prefix_sum[i + mid - 1][j - 1] - prefix_sum[i - 1][j + mid - 1] + prefix_sum[i - 1][j - 1]
                    if s <= threshold:
                        found = True
                        break
                if found:
                    break
            if found:
                left = mid
            else:
                right = mid - 1
        return left

        """ 我的解 超时 binary search/二分答案 复杂度高一些 """
        width = len(mat[0])
        height = len(mat)
        max_side_len = width if width < height else height
        left = 0
        right = max_side_len
        while left < right:
            mid = (left + right + 1) // 2
            s = 0
            found = False
            for i in range(0, height - mid + 1):
                for j in range(0, width - mid + 1):
                    s = 0
                    for k in range(i, i + mid):
                        s += sum(mat[k][j:j + mid])
                    if s <= threshold:
                        found = True
                        break
                if found:
                    break
            if found:
                left = mid
            else:
                right = mid - 1
        return left
