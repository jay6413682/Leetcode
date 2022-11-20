class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        回溯/backtracking
        类似 https://leetcode.cn/problems/sudoku-solver/solution/c-by-jian-chi-xue-xi-100tian-au5r/ 的”另一种思路“
        """
        def does_satisfy_rule(row, col, str_num):
            if board[row][col] != '.':
                # 当前是 数字
                if board[row][col] == str_num:
                    # 与num 相等 ，满足条件
                    return True
                else:
                    return False
            if str_num in board[row]:
                # 横着有重复
                return False
            if str_num in [board[i][col] for i in range(9)]:
                # 竖着有重复
                return False
            block_start_i = row // 3 * 3
            block_start_j = col // 3 * 3
            block = []
            for i in range(block_start_i, block_start_i + 3):
                for j in range(block_start_j, block_start_j + 3):
                    block.append(board[i][j])
            if str_num in block:
                # 3 x 3 block里有重复
                return False
            return True

        def dfs(row, col):
            if row == 9 and col == 0:
                #print(board)
                return True

            for num in range(1, 10):
                if does_satisfy_rule(row, col, str(num)):
                    original = board[row][col]
                    board[row][col] = str(num)
                    #print(board)
                    if col == 8:
                        rtv = dfs(row + 1, 0)
                    else:
                        rtv = dfs(row, col + 1)
                    if rtv:
                        return True
                    board[row][col] = original
        dfs(0, 0)
