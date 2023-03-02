class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """ bit manipulation / 位运算 https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/solution/li-yong-yi-huo-yun-suan-de-xing-zhi-tan-xin-suan-f/
        重点看@ ̶.̶G̶F̶u̶＇̶ 、̶ ̶| 的回复
        """
        res = 0
        # 每个数最多32 位
        i = 32
        mask = 0
        temp_max = 0
        while i >= 0:
            # 从最左边一位开始 mask
            mask |= (1 << i)
            # prefix set 包含masked bits of 所有numbers，set 的话做 a ^ temp_max in prefix_set 复杂度比较低
            prefix_set = set()
            for num in nums:
                prefix_set.add(num & mask)
            # 假设 临时当前 前缀XOR 最大值：当前bit 为 1，左侧bits 为已知的前缀XOR最大值
            temp_prefix_max = res | (1 << i)
            for a in prefix_set:
                # 如果 a ^ max = b 成立 ，max 表示当前得到的“最大值”，那么一定有 a ^ b = max 成立
                if a ^ temp_prefix_max in prefix_set:
                    res = temp_prefix_max
                    break
                # 如果prefix_set 不存在这种 b 的话，那么当前位就为 0，因为下一个循环 temp_prefix_max = res | (1 << i) 就把下一位 设成 1了，当前位没做任何事。res实际为从左到右扫 直到当前 bit 的 prefix XOR 最大值
            i -= 1
        return res


class TrieNode:
    def __init__(self):
        self.next = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, num):
        i = 30
        curr_node = self.root
        while i >= 0:
            curr_bit = (num >> i) & 1
            if not curr_node.next[curr_bit]:
                curr_node.next[curr_bit] = TrieNode()
            curr_node = curr_node.next[curr_bit]
            i -= 1
    def search_max_xor(self, num):
        i = 30
        curr_node = self.root
        res = 0
        while i >= 0:
            a = (num >> i) & 1
            b = 1 - a
            if curr_node.next[b]:
                res |= (1 << i)
                curr_node = curr_node.next[b]
            else:
                res |= (0 << i)
                curr_node = curr_node.next[a]
            i -= 1
        return res


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """ trie,二进制前缀树, greedy algorithm 讲解：https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/solution/python3-qiao-miao-li-yong-qian-zhui-shu-0alcy/
        答案：https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-bmjdg/
        时间复杂度：O(n)O(n)
        空间复杂度：O(n)O(n)
        """
        trie = Trie()
        res = 0
        for num in nums:
            trie.insert(num)
            res = max(res, trie.search_max_xor(num))
        return res
