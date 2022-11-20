class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """ 回溯 backtrack 类似 https://leetcode.cn/problems/letter-case-permutation/solution/shen-du-you-xian-bian-li-hui-su-suan-fa-python-dai/ 我没有把string 转化成数组 也可以
        """
        le = len(s)
        def dfs(pre_str, res, depth, start_i):
            if depth == le:
                res.append(pre_str)
                return
            curr_chr = s[start_i]
            if curr_chr.isalpha():
                dfs(pre_str + curr_chr.upper(), res, depth + 1, start_i + 1)
                dfs(pre_str + curr_chr.lower(), res, depth + 1, start_i + 1)
            else:
                dfs(pre_str + curr_chr, res, depth + 1, start_i + 1)
        res = []
        dfs('', res, 0, 0)
        return res