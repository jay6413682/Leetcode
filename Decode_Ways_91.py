class Solution1:
    def numDecodings(self, s: str) -> int:
        """ dynamic programming https://leetcode-cn.com/problems/decode-ways/solution/c-wo-ren-wei-hen-jian-dan-zhi-guan-de-jie-fa-by-pr/ 冲鸭的回覆
        """
        n = len(s)
        dp = [0] * (n + 1)
        if int(s[0]) == 0:
            return 0
        dp[0] = 1
        dp[-1] = 1

        # print(dp)
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            elif s[i - 1] == '1' or (s[i - 1] == '2' and int(s[i]) <= 6):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-2]


class Solution2:
    def numDecodings(self, s: str) -> int:
        """ dp优化解 https://leetcode-cn.com/problems/decode-ways/solution/c-wo-ren-wei-hen-jian-dan-zhi-guan-de-jie-fa-by-pr/
        Iris_bupt的图示；零却囚的解法
        """
        last_one = 1 # n - 1
        last_two = 1 # n - 2
        if s[0] == '0':
            return 0
        i = 1
        while i < len(s):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    temp = last_two
                else:
                    return 0
            elif s[i - 1] == '1' or (s[i - 1] == '2' and 1 <= int(s[i]) <= 6):
                temp = last_one + last_two
            else:
                temp = last_one
            last_two = last_one
            last_one = temp
            i += 1
        return last_one


class Solution3:
    counter = 0
    def numDecodings(self, s: str) -> int:
        """
        回溯法/back tracking 复杂度太高超时
        类似https://leetcode-cn.com/problems/decode-ways/solution/hui-su-dong-tai-gui-hua-by-xxbryce/
        """
        num_ch_mapping = {
            '1': 'A',
            '2' : 'B',
            '3' : 'C',
            '4' : 'D',
            '5' : 'E',
            '6' : 'F',
            '7' : 'G',
            '8' : 'H',
            '9' : 'I',
            '10' : 'J',
            '11' : 'K',
            '12' : 'L',
            '13' : 'M',
            '14' : 'N',
            '15' : 'O',
            '16' : 'P',
            '17' : 'Q',
            '18' : 'R',
            '19' : 'S',
            '20' : 'T',
            '21' : 'U',
            '22' : 'V',
            '23' : 'W',
            '24' : 'X',
            '25' : 'Y',
            '26': 'Z'
        }
        def dfs(path, start, s, n):
            if ''.join(path) == s:
                # print(path)
                self.counter += 1
                return
            if s[start] in num_ch_mapping:
                path.append(s[start])
                dfs(path, start + 1, s, n)
                path.pop()
            if start == n - 1:
                return
            first_two_chs = s[start: start + 2]
            # print('first_two_chs' + first_two_chs)
            if first_two_chs in num_ch_mapping:
                path.append(first_two_chs)
                dfs(path, start + 2, s, n)
                path.pop()
        dfs(deque(), 0, s, len(s))
        return self.counter


class Solution4:
    def numDecodings(self, s: str) -> int:
        """
        my own dp solution. 麻烦但直观。 https://leetcode-cn.com/problems/decode-ways/solution/c-wo-ren-wei-hen-jian-dan-zhi-guan-de-jie-fa-by-pr/ 思路
        """
        n = len(s)
        dp = [0] * n
        if int(s[0]) == 0:
            return 0
        dp[0] = 1
        if n > 1:
            if (s[0] != '1' and s[0] != '2') and s[1] == '0':
                return 0
            elif s[:2] == '10' or s[:2] == '20':
                dp[1] = 1
            elif int(s[:2]) <= 26:
                dp[1] = 2
            else:
                dp[1] = 1

        # print(dp)
        for i in range(2, len(s)):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            elif s[i - 1] == '1' or (s[i - 1] == '2' and int(s[i]) <= 6):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]
