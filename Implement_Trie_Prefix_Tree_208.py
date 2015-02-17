class TrieNode:
    def __init__(self):
        self.is_end = False
        self.next = [None for _ in range(26)]

class Trie:

    """ Trie，prefix tree 前缀树，字典树：https://www.pythonf.cn/read/123752 
    标准解法，不需要dict，我觉得比较好记：https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/trie-tree-de-shi-xian-gua-he-chu-xue-zhe-by-huwt/ 
    时间复杂度：insert、search、startsWith：O(N)
    空间复杂度：insert：O(N)；search、startsWith：O(1)
    （https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/208-shi-xian-trie-qian-zhui-shu-zi-dian-j6rpu/）
    时间复杂度：初始化为 O(1)O(1)，其余操作为 O(|S|)O(∣S∣)，其中 |S|∣S∣ 是每次插入或查询的字符串的长度。

    空间复杂度：O(|T|\cdot\Sigma)O(∣T∣⋅Σ)，其中 |T|∣T∣ 为所有插入字符串的长度之和，\SigmaΣ 为字符集的大小，本题 \Sigma=26Σ=26。
    （https://leetcode-cn.com/problems/implement-trie-prefix-tree/solution/shi-xian-trie-qian-zhui-shu-by-leetcode-ti500/）

    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()



    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if node.next[i] is None:
                node.next[i] = TrieNode()
            node = node.next[i]
        node.is_end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            i = ord(ch) - ord('a')
            if node.next[i] is None:
                return False
            node = node.next[i]
        return node.is_end is True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            i = ord(ch) - ord('a')
            if node.next[i] is None:
                return False
            node = node.next[i]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)