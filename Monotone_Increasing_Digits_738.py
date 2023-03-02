class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        """ 贪心 greedy  由后向前 找顶点 顶点-1 后面全变9 https://programmercarl.com/0738.%E5%8D%95%E8%B0%83%E9%80%92%E5%A2%9E%E7%9A%84%E6%95%B0%E5%AD%97.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC """
        n_list = list(str(n))
        le = len(n_list)
        i = le - 1
        while i >= 0:
            if i + 1 <= le - 1 and int(n_list[i]) > int(n_list[i + 1]):
                n_list[i] = str(int(n_list[i]) - 1)
                n_list[i + 1:] = '9' * (le - i - 1)
            i -= 1
        #print(n_list)
        return int(''.join(n_list))
