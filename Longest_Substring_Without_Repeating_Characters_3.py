'''
Created on Jun 11, 2015

@author: ljiang

Given a string, find the length of the longest substring without repeating characters. 
'''

class Solution3:
    """ 滑动窗口sliding window通解，双指针double pointers.
    https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
    时间复杂度：O(N)O(N)，其中 NN 是字符串的长度。左指针和右指针分别会遍历整个字符串一次。

    空间复杂度：O(|\Sigma|)O(∣Σ∣)，其中 \SigmaΣ 表示字符集（即字符串中可以出现的字符），|\Sigma|∣Σ∣ 表示字符集的大小。在本题中没有明确说明字符集，因此可以默认为所有 ASCII 码在 [0, 128)[0,128) 内的字符，即 |\Sigma| = 128∣Σ∣=128。我们需要用到哈希集合来存储出现过的字符，而字符最多有 |\Sigma|∣Σ∣ 个，因此空间复杂度为 O(|\Sigma|)O(∣Σ∣)。

    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        end = 0
        res = 0
        n = len(s)
        # 左指针一个一个往右移
        for c in s:
            # move end pointer to the right until found dup char
            while end < n and s[end] not in substring:
                substring.add(s[end])
                end += 1
            # now found dup char
            res = max(res, len(substring))
            # remove left most element from non repeating substring
            substring.remove(c)
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ Fasted solution：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-jie-suan-fa-3-wu-zhong-fu-zi-fu-de-zui-chang-z/
        e.g. abcdefghdhij
        moving i one char by one char
        saving the index
        moving max len substr start : 0 (proposed max len 4) -> 4 (proposed max len 5) -> 7 (proposed max len 2)
        """
        char_i_map = {}
        start = max_len = 0
        for i, chrt in enumerate(s):
            if chrt in char_i_map:
                proposed_start = char_i_map[chrt] + 1
                if proposed_start > start:
                    start = proposed_start
            proposed_max_len = i - start + 1
            max_len = proposed_max_len if proposed_max_len > max_len else max_len
            char_i_map[chrt] = i
        return max_len


class SolutionPlus:
    """ 此解为下面链接优化解，hash table 哈希表 滑动窗口 双指针
    https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-jie-suan-fa-3-wu-zhong-fu-zi-fu-de-zui-chang-z/
    马祖晖评论解
    时间复杂度：O(n)O(n)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # character to index mapping
        ch_index_mapping = {}
        res = 0
        start = 0
        for i, ch in enumerate(s):
            if ch in ch_index_mapping:
                # 马祖晖的评论：这段代码是用来规避哈希表查询到在滑动窗口左边的重复字符的。例如，在"tmmzuxt"这个字符串中，遍历到最后一步时，最后一个字符't'和第一个字符't'是相等的。 如果没有max函数锁定住滑动窗口的左边界，start就会弹回去第一个't'的索引0处，最后输出的最长无重复子串会变成"mmzuxt"。
                # 如果当前字母是和start 指针前面的某字母一样，不改变start 指针；否则改成前相同字母index + 1
                proposed_start = ch_index_mapping[ch] + 1
                start = max(proposed_start, start)
                # start 沒變，res 才会更大
                if start != proposed_start:
                    res = max(i - start + 1, res)
            else:
                # start 没变，res 才会更大
                res = max(i - start + 1, res)
            ch_index_mapping[ch] = i

        return res




class SolutionTwo:
    def lengthOfLongestSubstring(self, s: str) -> int:
        end = 0
        n = len(s)
        char_index_map = {}
        max_len = 0
        start = 0
        while end < n:
            if s[end] in char_index_map:
                end = start = char_index_map[s[end]] + 1
                char_index_map = {}
            char_index_map[s[end]] = end
            end += 1
            max_len = max_len if max_len > end - start else end - start
        return max_len


class Longest_Substring_Without_Repeating_Characters_10:
    def __init__(self):
        pass
    
    def Longest_Substring_Without_Repeating_Characters(self,strg):
        max_sub_string=""
        i=0
        max_len=0
        while i <len(strg):
            if strg[i] in max_sub_string:
                strg=strg.replace(max_sub_string[:max_sub_string.index(strg[i])+1],'',1)
                i=0#max_sub_string.index(strg[i])+1
                max_sub_string=strg[i]
            else:
                max_sub_string+=strg[i]
                if len(max_sub_string)>max_len:
                    max_len=len(max_sub_string)                
            i+=1

            
        return max_len
    
    
    def Longest_Substring_Without_Repeating_Characters_2(self,strg):
        i=0
        j=0
        max_sub_string=""
        max_len=0
        while i<len(strg):
            if strg[i] in max_sub_string:
                j+=max_sub_string.index(strg[i])+1
                i=j
                max_sub_string=strg[j]
            else:
                max_sub_string=strg[j:i+1]
                if len(max_sub_string)>max_len:
                    max_len=len(max_sub_string) 
            i+=1
                
        
        return max_len
        