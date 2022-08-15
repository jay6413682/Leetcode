

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """ 暴力法 https://leetcode.cn/problems/maximum-product-of-word-lengths/solution/zui-da-dan-ci-chang-du-cheng-ji-by-leetc-lym9/ """
        len_product = 0
        i = 0
        n = len(words)
        while i < n:
            j = i + 1
            while j > i and j < n:
                prod = len(words[i]) * len(words[j])
                if prod > len_product and not set(words[i]) & set(words[j]):
                    len_product = prod
                j += 1
            i += 1
        return len_product


from collections import defaultdict

class Solution2:
    def maxProduct(self, words: List[str]) -> int:
        """位运算 bit manipulation 状态压缩 https://leetcode-cn.com/problems/maximum-product-of-word-lengths/solution/zui-da-dan-ci-chang-du-cheng-ji-by-leetc-lym9/ """
        mask_len_map = defaultdict(int)
        for word in words:
            mask = 0
            for char in word:
                count = ord(char) - ord('a')
                mask |= 1 << count
            mask_len_map[mask] = max(len(word), mask_len_map[mask])
        max_prod = 0
        for mask in mask_len_map:
            for another_mask in mask_len_map:
                # 使用位掩码可以在常数时间内判断两个单词是否包含公共字母：(x & y) == 0。
                if mask & another_mask == 0:
                    max_prod = max(max_prod, mask_len_map[mask] * mask_len_map[another_mask])
        return max_prod
