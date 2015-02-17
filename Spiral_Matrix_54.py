'''
Created on Jul 14, 2015

@author: ljiang

Given a matrix of mXn elements (m rows, n columns), return all elements of the matrix in spiral order.
For example, given the following matrix:
[
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

'''
from typing import List


class Solution4:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ 可以模拟螺旋矩阵的方向 https://leetcode-cn.com/problems/spiral-matrix/solution/luo-xuan-ju-zhen-by-leetcode-solution/
        复杂度分析

        时间复杂度：O(mn)O(mn)，其中 mm 和 nn 分别是输入矩阵的行数和列数。矩阵中的每个元素都要被访问一次。

        空间复杂度：O(mn)O(mn)。需要创建一个大小为 m \times nm×n 的矩阵 \textit{visited}visited 记录每个位置是否被访问过。

        """
        if not matrix or not matrix[0]:
            return matrix
        columns, rows = len(matrix[0]), len(matrix)
        total = rows * columns
        # Unfortunately shortening this to something like 5*[5*[0]] doesn't really work because you end up with 5 copies of the same list, so when you modify one of them they all change
        # visited = [[False] * columns] * rows
        visited = [[False] * columns for _ in range(rows)]
        rtv = [0] * total
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_index = 0
        row, column = 0, 0
        for i in range(total):
            rtv[i] = matrix[row][column]
            assumed_row = row + directions[direction_index][0]
            assumed_column = column + directions[direction_index][1]
            visited[row][column] = True
            if not (columns > assumed_column >= 0 and rows > assumed_row >= 0 and not visited[assumed_row][assumed_column]):
                direction_index = (direction_index + 1) % 4
            row += directions[direction_index][0]
            column += directions[direction_index][1]
        return rtv


class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ simulation/按层模拟/iterative：https://leetcode-cn.com/problems/spiral-matrix/solution/cxiang-xi-ti-jie-by-youlookdeliciousc-3/
        时间复杂度：O(n * m)O(n∗m)
        空间复杂度：O(1)O(1)
        """
        m = len(matrix)
        n = len(matrix[0])
        res = []
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        while True:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res


class Solution3:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ simulation/模拟/recursive：https://leetcode-cn.com/problems/spiral-matrix/solution/xiang-jie-xing-zhuang-jie-fa-fang-xiang-3qmhf/
        时间复杂度：O(n * m)O(n∗m)
        空间复杂度：O(1)O(1)
        """
        m = len(matrix)
        n = len(matrix[0])
        res = []
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        def recursive_traverse(matrix, left, right, top, bottom, res):
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                return
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                return
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -=1
            if top > bottom:
                return
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                return
            recursive_traverse(matrix, left, right, top, bottom, res)
        recursive_traverse(matrix, left, right, top, bottom, res)
        return res


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ 我自己的按层模拟/recursive
        https://leetcode-cn.com/problems/spiral-matrix/solution/luo-xuan-ju-zhen-by-leetcode-solution/ """
        if not matrix:
            return matrix
        row_n, col_n = 0, 0
        row_len = len(matrix[0])
        col_len = len(matrix)
        rtv = []
        run = False
        while col_n < row_len:
            rtv.append(matrix[row_n][col_n])
            col_n += 1
            run = True
        if not run:
            return rtv
        else:
            run = False
        col_n = row_len - 1
        row_n = 1
        while row_n < col_len:
            rtv.append(matrix[row_n][col_n])
            row_n += 1
            run = True
        if not run:
            return rtv
        else:
            run = False
        col_n = row_len - 2
        row_n = col_len - 1
        while col_n >= 0 and row_n > 0:
            rtv.append(matrix[row_n][col_n])
            col_n -= 1
            run = True
        if not run:
            return rtv
        else:
            run = False
        row_n = col_len - 2
        col_n = 0
        while row_n > 0:
            rtv.append(matrix[row_n][col_n])
            row_n -= 1
            run = True
        if not run:
            return rtv
        else:
            run = False
        row_n = 1
        new_matrix = []
        while row_n < col_len - 1 and row_n > 0:
            new_matrix.append(matrix[row_n][1:-1])
            row_n += 1
        rtv.extend(self.spiralOrder(new_matrix))
        return rtv


class Spiral_Matrix_35:
    def __init__(self,matrix):
        self.matrix=matrix
        
    def traverse(self):
        n_len=len(self.matrix)
        m_len=len(self.matrix[0])
        row=0
        column=0
        #print n_len
        #print m_len
        result=[]
        while n_len>0 and m_len>0:
            i=0
            while i<m_len:               
                result.append(self.matrix[row][column])
                column+=1 
                i+=1               
            row+=1
            n_len-=1
            column-=1
            if n_len==0: return result
            i=0
            while i<n_len:
                result.append(self.matrix[row][column])
                row+=1
                i+=1
            row-=1
            column-=1
            m_len-=1
            if m_len==0: return result
            i=0
            while i<m_len:
                result.append(self.matrix[row][column])
                column-=1
                i+=1
            row-=1
            n_len-=1
            column+=1
            if n_len==0: return result
            i=0
            while i<n_len:
                result.append(self.matrix[row][column])
                row-=1     
                i+=1 
            m_len-=1
            column+=1
            row+=1     
            if m_len==0: return result
        return result     
                
            
            
                
        
        
