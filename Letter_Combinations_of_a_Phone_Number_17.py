class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """ 回溯 backtrack 类似 https://leetcode.cn/problems/letter-combinations-of-a-phone-number/solution/hui-su-sou-suo-wu-xian-shi-hui-su-yan-du-you-xian-/ 只是他的解没有path append pop，而是直接传 组装后的string
        
        """
        def get_chars(digit):
            digit_chars_map = {
                2: ['a', 'b', 'c'],
                3: ['d', 'e', 'f'],
                4: ['g', 'h', 'i'],
                5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'],
                7: ['p', 'q', 'r', 's'],
                8: ['t', 'u', 'v'],
                9: ['w', 'x', 'y', 'z'],
            }
            return digit_chars_map.get(digit)
            # below is incorrect because 7 and 9 maps to 4 chars instead of 3
            # return [chr(ord(char) + 3 * (digit - 2)) for char in ['a', 'b', 'c']]
        if not digits:
            return []
        results = []
        le = len(digits)
        def dfs(start_i, path, results):
            if start_i == le:
                results.append(''.join(path))
                return
            digit = int(digits[start_i])
            chars = get_chars(digit)
            for char in chars:
                path.append(char)
                dfs(start_i + 1, path, results)
                path.pop()
        dfs(0, [], results)
        return results
