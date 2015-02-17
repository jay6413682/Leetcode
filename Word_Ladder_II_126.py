# graph
# 图论

from typing import List


class Solution:
    """
    https://leetcode-cn.com/problems/word-ladder-ii/solution/yan-du-you-xian-bian-li-shuang-xiang-yan-du-you--2/
    """
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def bfs(beginWord, endWord, wordList, successors):
            # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里
            words_set = set(wordList)
            final = False
            if endWord not in words_set:
                return final
            if beginWord in words_set:
                words_set.remove(beginWord)
            queue = [beginWord]
            visited = set()
            # next_level_visited 是需要的 看解法中的图
            next_level_visited = set()
            while queue:
                queue_words_len = len(queue)
                i = 0
                while i < queue_words_len:
                    curr_word = queue.pop(0)
                    curr_word_list = list(curr_word)
                    for j, c in enumerate(curr_word_list):
                        for k in range(0, 26):
                            replace_char = chr(ord('a') + k)
                            curr_word_list[j] = replace_char
                            next_word = ''.join(curr_word_list)
                            if next_word == curr_word:
                                continue
                            if next_word in words_set and next_word not in visited:
                                if next_word == endWord:
                                    final = True
                                # 避免下层元素重复加入队列
                                if next_word not in next_level_visited:
                                    next_level_visited.add(next_word)
                                    queue.append(next_word)
                                successors[curr_word].add(next_word)
                        curr_word_list[j] = c
                    i += 1
                if final:
                    break
                # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里
                visited |= next_level_visited
                next_level_visited = set()
            return final

        def dfs(beginWord, endWord, successors, path, res):
            if beginWord == endWord:
                res.append(path[:])
                return
            if beginWord not in successors:
                return
            successors_words = successors[beginWord]
            for word in successors_words:
                path.append(word)
                dfs(word, endWord, successors, path, res)
                path.pop()

        # 第 1 步：使用广度优先遍历得到后继结点列表 successors
        # key：字符串，value：广度优先遍历过程中 key 的后继结点列表
        successors = defaultdict(set)
        final = bfs(beginWord, endWord, wordList, successors)
        if not final:
            return []
        res = []
        path = [beginWord]
        # 第 2 步：基于后继结点列表 successors ，使用回溯算法得到所有最短路径列表
        dfs(beginWord, endWord, successors, path, res)
        return res
        """
        # try no. 2
        def path_exists(beginWord, endWord, wordList, successors_map):
            does_path_exist = False
            queue = deque([beginWord])
            word_set = set(wordList)
            if endWord not in word_set:
                return does_path_exist
            visited = set([beginWord])
            next_level_visited = set()
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
                            if next_word == curr_word:
                                # curr work cannot be the same as next word
                                continue
                            if next_word in word_set:
                                if next_word == endWord:
                                    does_path_exist = True
                                if next_word not in visited:
                                    if next_word not in next_level_visited:
                                        # 下一层word 不能重复计入queue
                                        next_level_visited.add(next_word)
                                        queue.append(next_word)
                                    # curr word下一层word不能在上一层已经visited的words中；且不能重复； 但是可以在curr word同一层前面已经visited的word 的下一层words中出现过 比如："red" "tax" ["ted","tex","red","tax","tad","den","rex","pee"] 的tex
successors_map[curr_word].add(next_word)
                                # print(curr_word, next_word, word_set, successors_map)
                        curr_word_list[i] = orig_char
                visited |= next_level_visited
                next_level_visited = set()
            return does_path_exist
        successors_map = defaultdict(set)
        if not path_exists(beginWord, endWord, wordList, successors_map):
            return []
        # print(successors_map)
        def get_paths(beginWord, endWord, successors_map, res, path):
            if beginWord == endWord:
                res.append(list(path))
                return
            if beginWord not in successors_map:
                return
            successors = successors_map[beginWord]
            for nxt in successors:
                path.append(nxt)
                # print(nxt, endWord, path)
                get_paths(nxt, endWord, successors_map, res, path)
                path.pop()

        res = []
        get_paths(beginWord, endWord, successors_map, res, deque([beginWord]))
        return res

        """
