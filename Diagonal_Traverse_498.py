class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """ 画图举例总结规律，模拟 simulation：类似https://leetcode.cn/problems/diagonal-traverse/solution/dui-jiao-xian-bian-li-fen-xi-ti-mu-zhao-zhun-gui-l/
        我有把我画的图照相
        """
        res = []
        m = len(mat)
        n = len(mat[0])
        # 对角线number
        diag_line_no = 0
        while diag_line_no <= m + n - 2:
            # print("line: {}".format(diag_line_no))
            x = 0
            y = 0
            if diag_line_no % 2 == 0:
                # 左下到右上，x变小，y变大
                if diag_line_no <= m - 1:
                    x = diag_line_no
                else:
                    x = m - 1
                y = diag_line_no - x
                while y <= n - 1 and y <= diag_line_no:
                    # y 最大不能超过 n - 1 或 对角线 number
                    # print(x, y)
                    res.append(mat[x][y])
                    x -= 1
                    y += 1
            else:
                # 右上到左下，y变小，x变大
                if diag_line_no <= n - 1:
                    y = diag_line_no
                else:
                    y = n - 1
                x = diag_line_no - y
                while x <= m - 1 and x <= diag_line_no:
                    # x 最大不能超过 m - 1 或 对角线 number
                    # print(x, y)
                    res.append(mat[x][y])
                    y -= 1
                    x += 1
            diag_line_no += 1
        return res
        """
        # optimization solution
        res = []
        m = len(mat)
        n = len(mat[0])
        diag_line_no = 0
        while diag_line_no <= m + n - 2:
            axis_1 = 0
            axis_2 = 0
            if diag_line_no % 2 == 0:
                upper_limit_1 = m - 1
                upper_limit_2 = n - 1
            else:
                upper_limit_1 = n - 1
                upper_limit_2 = m - 1
            if diag_line_no <= upper_limit_1:
                axis_1 = diag_line_no
            else:
                axis_1 = upper_limit_1
            axis_2 = diag_line_no - axis_1
            while axis_2 <= upper_limit_2 and axis_2 <= diag_line_no:
                if diag_line_no % 2 == 0:
                    res.append(mat[axis_1][axis_2])
                else:
                    res.append(mat[axis_2][axis_1])
                axis_1 -= 1
                axis_2 += 1
            diag_line_no += 1
        return res
        """

                