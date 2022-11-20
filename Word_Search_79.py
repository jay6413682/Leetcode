class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """ flood fill dfs：https://leetcode.cn/problems/word-search/solution/zai-er-wei-ping-mian-shang-shi-yong-hui-su-fa-pyth/
        """
        def dfs(i, j, char_search_idx, used):
            rtv = False
            if word[char_search_idx] == board[i][j]:
                if char_search_idx == word_len - 1:
                    # print(i, j)
                    return True
                used[i][j] = True
                directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
                for d in directions:
                    new_i = i + d[0]
                    new_j = j + d[1]
                    if 0 <= new_i <= m - 1 and 0 <= new_j <= n - 1:
                        if used[new_i][new_j]:
                            continue
                        rtv = dfs(new_i, new_j, char_search_idx + 1, used)
                        if rtv == True:
                            return rtv
                used[i][j] = False
            return rtv
        word_len = len(word)
        m = len(board)
        n = len(board[0])
        used = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    found = dfs(i, j, 0, used)
                    if found:
                        return found
        return False