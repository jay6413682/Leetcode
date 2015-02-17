# graph
# 图论


from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """ undirected graph 无向图 广度优先遍历
        https://leetcode-cn.com/problems/word-ladder/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you-2/ 視頻
        双向广度优先遍历/bidirectional bfs 只需了解
        下面解答的图很好
        https://leetcode-cn.com/problems/word-ladder/solution/shou-hua-tu-jie-127-dan-ci-jie-long-bfsde-dian-x-2/
        """
        # 第 1 步：先将 wordList 放到哈希表里，it makes "in" more efficient
        words_set = set(wordList)
        if len(words_set) == 0 or endWord not in words_set:
            return 0
        if beginWord in words_set:
            words_set.remove(beginWord)
        # 第 2 步：图的广度优先遍历，必须使用队列和表示是否访问过的 visited 哈希表
        queue = [beginWord]
        visited = set(beginWord)
        # 第 3 步：开始广度优先遍历，包含起点，因此初始化的时候步数为 1
        step = 1
        while queue:
            current_queue_size = len(queue)
            i = 0
            while i < current_queue_size:
                word = queue.pop(0)
                word_list = list(word)
                for j, c in enumerate(word_list):
                    for k in range(0, 26):
                        word_list[j] = chr(ord('a') + k)
                        new_word = ''.join(word_list)
                        if new_word == endWord:
                            return step + 1
                        if new_word in words_set and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)
                    # 恢復
                    word_list[j] = c
                i += 1
            step += 1
        return 0
        """
        # second try; similar to https://leetcode-cn.com/problems/word-ladder/solution/shou-hua-tu-jie-127-dan-ci-jie-long-bfsde-dian-x-2/
        queue = deque([beginWord])
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        shortest_vertices = 1
        while queue:
            n = len(queue)
            for _ in range(n):
                curr_word = queue.popleft()
                curr_word_list = list(curr_word)
                for i in range(len(curr_word_list)):
                    orig_char = curr_word_list[i]
                    for rep in range(0, 26):
                        curr_word_list[i] = chr(ord('a') + rep)
                        next_word = ''.join(curr_word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                shortest_vertices += 1
                                return shortest_vertices
                            queue.append(next_word)
                            word_set.remove(next_word)
                    curr_word_list[i] = orig_char
            shortest_vertices += 1
        return 0
        """
