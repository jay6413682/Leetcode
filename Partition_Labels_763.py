class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 解法 1
        # greedy 贪心 https://leetcode.cn/problems/partition-labels/solution/zui-jian-dan-jie-shi-bi-guan-jie-hao-dong-duo-liao/
        char_max_index_map = {}
        for i, char in enumerate(s):
            char_max_index_map[char] = i
        # print(char_max_index_map)
        curr_partition_start, curr_partition_end = 0, 0
        res = []
        for i, char in enumerate(s):
            curr_partition_end = max(char_max_index_map[char], curr_partition_end)
            if curr_partition_end == i:
                # print(curr_partition_end, i, char_max_index_map[char], char)
                res.append(curr_partition_end - curr_partition_start + 1)
                curr_partition_start = curr_partition_end + 1
        return res

        # 解法 2
        # 统计字符串中所有字符的起始和结束位置，记录这些区间，将区间按左边界从小到大排序，找到边界将区间划分成组，互不重叠。找到的边界就是答案。
        # https://programmercarl.com/0763.%E5%88%92%E5%88%86%E5%AD%97%E6%AF%8D%E5%8C%BA%E9%97%B4.html#%E6%80%9D%E8%B7%AF
        # 记录每个字母出现的区间
        chars_range = [[None, None] for _ in range(26)]
        for i in range(len(s)):
            char_index = ord(s[i]) - ord('a')
            if chars_range[char_index][0] is None:
                chars_range[char_index][0] = i
            chars_range[char_index][1] = i
        # 去除字符串中未出现的字母所占用区间
        filtered_chars_range = []
        for r in chars_range:
            if r[0] is not None:
                filtered_chars_range.extend(r)
        # 按照左边界从小到大排序
        filtered_chars_range.sort(key=lambda x: x[0])
        # 记录当前 partition 的左右边界
        curr_partition_start, curr_partition_end = filtered_chars_range[0], filtered_chars_range[1]
        res = 0
        for r in filtered_chars_range:
            # # 一旦下一区间左边界大于当前右边界，即可认为出现分割点
            if r[0] == curr_partition_end + 1:  # if hash[i][0] > right
                res.append(curr_partition_end - curr_partition_start + 1)
                curr_partition_start = r[0]  # curr_partition_end + 1
            # # 实时更新当前partition 右边界
            curr_partition_end = max(curr_partition_end, r[1])
        # # 最右侧区间（字符串长度为1时的特殊情况也包含于其中）
        res.append(curr_partition_end - curr_partition_start + 1)
        return res

        # my solution: 从左到右尽量多的插入 分隔，然后确定某字母的范围，尝试在该范围 左右 加分隔
        n = len(s)
        # s 尾部 加 dummy _ 占位，用来 在 s 的末尾 加分隔 ，也就是在 _ 左侧加分隔
        s += '_'
        partitions = []
        visited = set()
        for i in range(n):
            if s[i] not in visited:
                # 已经 试过 的跳过
                visited.add(s[i])
                for j in range(n, -1, -1):
                    if s[j] == s[i]:
                        # 判断 i, j + 1 的 左侧 能不能 插入 partitions
                        if not partitions:
                            # 已知的 分隔是 空的 ，i, j + 1 的 左侧可以 加 分隔
                            partitions.extend([i, j + 1])
                        else:
                            start, end = 0, 1
                            to_pop = []
                            to_add = [i, j + 1]
                            while end < len(partitions):
                                # 从左到右 i 和 j + 1 与 已有的分隔 比较
                                if i >= partitions[start] and j + 1 <= partitions[end]:
                                    # 如果 i 和 j + 1 左侧 在 已有 的 分隔 内，如果 再 插入 分隔 在 i 或 j + 1 左侧 则会 分隔 相同的字母，不满足条件
                                    #print(i, j + 1, 'do nothing', partitions)
                                    # 这种情况 不要 加入 分隔
                                    to_add = []
                                    break
                                elif partitions[end] > i >= partitions[start] and j + 1 > partitions[end]:
                                    # 如果 i 在 end 左侧，j + 1 在 end 右侧，把end 从 已有分隔中去掉，并且 把 i 从 要加入的 分隔中去掉 
                                    to_pop.append(end)
                                    to_add = [j + 1]
                                    end += 1
                                elif i >= partitions[end]:
                                    # 乳沟 i 在 end 右侧 ，继续比较 已有分隔中 后面的其他分隔 
                                    start += 1
                                    end += 1
                            # 将分隔中该去掉的去掉，该加入的加入
                            for x in to_pop:
                                partitions.pop(x)
                            partitions.extend(to_add)
                            partitions.sort()
                        break
        res = []
        #print(partitions)
        # 通过分隔的index 来确定 每个分隔的 字符串片段的长度
        for i in range(len(partitions) - 1):
            distance = partitions[i + 1] -  partitions[i]
            if distance != 0:
                res.append(distance)
        return res
