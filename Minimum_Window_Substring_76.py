from _collections import deque, defaultdict
class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        """ my solution, sliding window， double pointers 通解 https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
        上面的通解原来应该是labuladong的模版 ，但是被删除了。。。我找到之后update 了numbers sheet
        某些思路类似https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/ 这个例子for loop 移动右指针；我的例子for loop移动左指针，套用上面的模版
        我们会用j扫描一遍S，也会用i扫描一遍S，最多扫描2次S，所以时间复杂度是O(n)O(n)，
        空间复杂度o(n)
        """
        # in the substring, map between char and how many needed to make substring include every char in t
        need = defaultdict(int)
        for ch in t:
            need[ch] += 1
        # in the substring, how many char in t needed to include every char in t
        need_count = len(t)
        end = 0
        res = ''
        n = len(s)
        # deque is more efficient
        substring = deque()
        for ch in s:
            # move end pointer to right, until the end of string or need count is 0
            while end < n and need_count > 0:
                if s[end] in need:
                    # need_count only - 1 when there are no such char in the substring
                    if need[s[end]] > 0:
                        need_count -= 1
                    need[s[end]] -= 1
                substring.append(s[end])
                end += 1
                # print(substring, need_count, need)

            # now, either end == n or t is in substring == true; need calculate the res
            if need_count == 0:
                if not res:
                    res = ''.join(substring)
                else:
                    res = res if len(res) <= len(substring) else ''.join(substring)
                # print(res)
            # pop left most char, later move the left pointer one step to the right
            popped = substring.popleft()
            # for the popped left most char, need_count only + 1 when the char will be needed
            if popped in need:
                need[popped] += 1
                if need[popped] > 0:
                    need_count += 1
            # print(res, substring, need_count, need)
        return res



class Solution:
    def is_s2_in_s1(self, s1, s2):
        s1 = s1.copy()
        for ch in s2:
            if ch not in s1:
                return False
            s1.remove(ch)
        return True

    def minWindow(self, s: str, t: str) -> str:
        """ My solution, 超时，sliding window, double pointers
        根据基本模版写成 https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
        """
        end = 0
        res = ''
        n = len(s)
        substring = deque()
        for ch in s:
            # move end pointer to right
            while end < n and not self.is_s2_in_s1(substring, t):
                substring.append(s[end])
                end += 1
            # now, either end == n or is_s2_in_s1 == true; need calculate the res
            if self.is_s2_in_s1(substring, t):
                if not res:
                    res = ''.join(substring)
                else:
                    res = res if len(res) <= len(substring) else ''.join(substring)
                # print(res)
            substring.popleft()
            # print(res, substring)
        return res


class Solution3:
    def minWindow(self, s: str, t: str) -> str:
        """ 超时，sliding window，改变window size """
        n = len(s)
        t_list = list(t)
        res = s
        for i in range(n):
            l = r = l_pointer = r_pointer = mid_window = i
            l_stop = False
            r_stop = False
            if s[mid_window] in t_list:
                t_list.remove(s[mid_window])
                if mid_window == 0:
                    l_stop = True
                if mid_window == n - 1:
                    r_stop = True
            while t_list:
                if l != r:
                    if s[l] in t_list and not l_stop:
                        l_pointer = l
                        t_list.remove(s[l])
                    if s[r] in t_list and not r_stop:
                        r_pointer = r
                        t_list.remove(s[r])
                    if l == 0:
                        l_stop = True
                    if r == n - 1:
                        r_stop = True
                if l == 0 and r == n - 1 and t_list:
                    return ''
                if l > 0:
                    l -= 1
                if r < n - 1:
                    r += 1
                # print(l, r, l_pointer, r_pointer)
            res = s[l_pointer: r_pointer + 1] if r_pointer - l_pointer + 1 < len(res) else res
            # print(res)
            t_list = list(t)
        return res
