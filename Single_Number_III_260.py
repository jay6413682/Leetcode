

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """ https://leetcode-cn.com/problems/single-number-iii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-5-8/ """
        s = list()
        for num in nums:
            if num not in s:
                s.append(num)
            else:
                s.remove(num)
        return s


class Solution2:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """ 视频：https://leetcode-cn.com/problems/single-number-iii/solution/zhi-chu-xian-yi-ci-de-shu-zi-iii-by-leet-4i8e/
        时间复杂度：O(n)O(n)，我们只需要遍历数组两次。

        空间复杂度：O(1)O(1)，只需要常数的空间存放若干变量。
        """
        # 关键是分成两组，每组再按136解法得出这两个只出现一次的不同数字
        a_xor_b = 0
        for num in nums:
            # 得到两个只出现一次的不同数字的异或结果
            a_xor_b ^= num
        mask = 1
        while mask & a_xor_b != mask:
            # 找到第一位不是0的那个数
            mask <<= 1
        # mask = a_xor_b & (-a_xor_b)
        a = 0
        b = 0
        for num in nums:
            # 根据该位是否为0将所有数分为两组，分别进行异或得到我们想要的两个数字
            if num & mask == mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
        """
        # 下面这种想利用 a ^ b = c ->  a ^ c = b 做法不对，比如 [10,10,5,5,9,6] ， 如果10 ^ 5 = 9 ^ 6 ，就有可能得到10 , 5
        axorb = 0
        for i in nums:
            axorb ^= i
        print(axorb)
        for j in nums:
            b = j ^ axorb
            print(b, j)
            if b in nums:
                res = [j, b]
                break
        return res
        """
