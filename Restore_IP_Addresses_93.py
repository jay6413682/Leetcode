class Solution:
    """ 回溯 backtracking : https://leetcode.cn/problems/restore-ip-addresses/solution/hui-su-suan-fa-hua-tu-fen-xi-jian-zhi-tiao-jian-by/ """
    def restoreIpAddresses(self, s: str) -> List[str]:
        le = len(s)
        def dfs(start_i, path, res, depth):
            # 由于 ip 段最多就 4 个段，因此这棵三叉树最多 4 层
            if depth == 4:
                # 已经选了 4 个 sub fields 但是 数字没有选完 
                if len(''.join(path)) < le:
                    return
                else:
                    res.append('.'.join(path))
                    return
            for sub_len in range(1, 4):
                # 剩余位数不够凑出 需要的 sub fields
                if le - start_i < 4 - depth:
                    return
                # 剩余位数 太多
                if le - start_i > (4 - depth) * 3:
                    return

                curr_sub_end = start_i + sub_len
                # 末尾 已经超过 最大值
                if curr_sub_end > le:
                    return
                curr_sub = s[start_i:curr_sub_end]
                curr_sub_int = int(curr_sub)
                # 现在选的数已经大于255
                if curr_sub_int > 255:
                    return
                # 现在选的数 以0 开始 但不是0
                if curr_sub.startswith('0') and curr_sub != '0':
                    return
                path.append(curr_sub)
                dfs(curr_sub_end, path, res, depth + 1)
                path.pop()
        res = []
        dfs(0, [], res, 0)
        return res
