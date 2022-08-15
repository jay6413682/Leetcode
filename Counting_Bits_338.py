class Solution:
    def countBits(self, n: int) -> List[int]:
        # dynamic programming O(n)
        # https://leetcode.cn/problems/counting-bits/solution/hen-qing-xi-de-si-lu-by-duadua/ 
        # https://leetcode.cn/problems/counting-bits/solution/yi-bu-bu-fen-xi-tui-dao-chu-dong-tai-gui-3yog/
        # 奇数：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。
        # 偶数：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。因为最低位是 0，除以 2 就是右移一位，也就是把那个 0 抹掉而已，所以 1 的个数是不变的

        arr = [None] * (n + 1)
        arr[0] = 0
        for i in range(0, n + 1):
            if i % 2 == 0:
                arr[i] = arr[i // 2]
            else:
                arr[i] = arr[i - 1] + 1
        return arr

        # i & (i - 1)去掉最右1
        arr = []
        for i in range(0, n + 1):
            count = 0
            while i > 0:
                i &= (i - 1)
                count += 1
            arr.append(count)
        return arr
