

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ BladeXaver:
        楼主，您好，看了您的这个题解好久了，ones 的推导过程理解了，twos 的推导过程还是不明白，主要集中在twos 推导图中第二个状态          图，实在不是很明白，为啥从01 开始，为啥是01到00，希望能得到楼主的解答，非常感谢！！！

        哈喽，因为 ones 和 twos 并不是同时计算的，是先计算出 ones 的下一状态，在这个 ones 的基础上计算 twos 。 因此，分析            twos 的状态转移 要把 ones “向前推一个状态”，也就是本文对于 twos 的状态转移图修改~
        我的思考：
        图中 在（two不变如何算one）算完one = one ^ n & ~two 之后 00 -> 01, 01 -> 00, 10 -> 10. 下一步如何将 01 -> 01, 00 -> 10, 10 -> 00从而完成状态转换（one不变如何算two）呢？如果你比较 00 -> 01, 01 -> 00, 10 -> 10 和 01 -> 01, 00 -> 10, 10 -> 00；区别就是 把one 和 two 交换，two不变如何算one和one不变如何算two方法完全一样，所以要求 two 完全可以用一样的方法
        小明：
        感谢楼主的解答，有一点疑问，解法1最终返回结果ones 为什么是我们要找的数字呀？

        哈喽，文中解法一首句话 如下图所示，对于所有数字中的某二进制位 1 的个数，存在 3 种状态，即对 3 余数为 0, 1, 2 。 即运用位运算统计 数字二进制各位 对3取余的数值
        
        遍历完所有数字后，各二进制位都处于状态 00和状态 01 （取决于 “只出现一次的数字” 的各二进制位是 1 还是 0,如果是1 正好状态为 01，如果是0 状态正好是00），而此两状态是由 one 来记录的（此两状态下 twos 恒为 0），因此返回 ones 即可。

        https://leetcode-cn.com/problems/single-number-ii/solution/single-number-ii-mo-ni-san-jin-zhi-fa-by-jin407891/ 
        真值表通解：
        https://leetcode-cn.com/problems/single-number-ii/solution/luo-ji-dian-lu-jiao-du-xiang-xi-fen-xi-gai-ti-si-l/
        真值表 -> 逻辑表达式： https://zhuanlan.zhihu.com/p/154529095
        异或逻辑表达式：X ^ Y = ~X & Y | X & ~Y: https://baike.baidu.com/item/%E5%BC%82%E6%88%96/10993677
        """
        twos, ones = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        """ 
        hash set solution: https://leetcode-cn.com/problems/single-number-ii/solution/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetcode/
        space complexity : o(n)
        """
        return (3 * sum(set(nums)) - sum(nums)) // 2


class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        """ 
        hash map solution: https://leetcode-cn.com/problems/single-number-ii/solution/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetcode/
        """
        num_counter_map = {}
        for num in nums:
            if num not in num_counter_map:
                num_counter_map[num] = 1
            else:
                num_counter_map[num] += 1
                if num_counter_map[num] == 3:
                    print('deleting {}'.format(num_counter_map[num]))
                    del num_counter_map[num]
        return list(num_counter_map.keys())[0]


class Solution4:
    def singleNumber(self, nums: List[int]) -> int:
        """
        位操作2: https://leetcode-cn.com/problems/single-number-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--31/
        python 位运算： https://www.cnblogs.com/Neeo/articles/10536202.html
        python 负数存储：https://blog.csdn.net/HWQlet/article/details/106321324
        https://www.zhihu.com/question/314455297
        why ~(single_num ^ 0xffffffff) ?
        if single_num is : 1111....1101, because the 32bit is 1, it is actually supposed to be a negative number (-3) (补码), but because how python store negative number - it has unlimited bits, so it is still treated as a very large positive number; so we need actually convert it to be a negative number：
        以下为补码运算：
        0000...00001111....1101 ^ 0000..0000011111...1111 = 000000...0010
        ~000000...0010 = 1111...1101 
        因为1111...1101为负数，它的原码为10000...0011 --> -3

        """
        i = 0
        single_num = 0
        negative = False
        while i < 32:
            counter = 0
            for num in nums:
                if num >> i & 1 == 1:
                    counter += 1
            if counter % 3 != 0:
                if i == 31:
                    negative = True
                mask = 1 << i
                single_num |= mask
            i += 1
        return single_num if not negative else ~(single_num ^ 0xffffffff)
        """
        # 与上面方法类似
        # 通解：https://leetcode-cn.com/problems/single-number-ii/solution/single-number-ii-mo-ni-san-jin-zhi-fa-by-jin407891/
        res = 0
        bit_counters = [0] * 32
        for num in nums:
            for i in range(32):
                bit_counters[i] += (num & 1)
                num >>= 1
        # print(bit_counters)
        for j in range(31, -1 , -1):
            # res 只能左移31 次
            res <<= 1
            res |= bit_counters[j] % 3
            
        return res if bit_counters[-1] % 3 != 1 else ~(res ^ 0xffffffff)
        """


class Solution5:
    def singleNumber(self, nums: List[int]) -> int:
        """ 
        通用方法:
        https://leetcode-cn.com/problems/single-number-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--31/
        """
        x1, x2 = 0, 0
        for num in nums:
            x2 ^= x1 & num
            x1 ^= num
            mask = ~(x2 & x1)
            x1 &= mask
            x2 &= mask
        return x1


import math
class Solution6:
    def singleNumber(self, nums: List[int]) -> int:
        """ 
        通用方法:
        https://leetcode-cn.com/problems/single-number-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--31/
        不太懂 算了
        """
        # somehow the method below does not return correct value...
        k = 3
        p = 1
        m = math.ceil(math.log(k, 2))
        x = [0] * m
        temp = p
        return_x_counter = 0
        while temp > 0:
            temp &= 1
            return_x_counter += 1
            if temp:
                break
            temp >>= 1
        for num in nums:
            j = m - 1
            while j > 0:
                i = j
                temp = x[i - 1]
                while i > 0:
                    x[j] = temp & x[i - 1]
                    temp = x[j]
                    i -= 1
                x[j] = x[j] & num
                x[j] ^= x[j]
                j -= 1
            x[0] ^= num
            temp = k
            mask = 1
            counter = 0
            while temp > 0:
                temp &= 1
                counter += 1
                if temp:
                    mask &= x[-1 * counter]
                else:
                    mask &= ~x[-1 * counter]
                temp >>= 1
            mask = ~mask
            l = m - 1
            while l >= 0:
                x[l] &= mask
                l -= 1
        return x[-1 * return_x_counter]

        """
        # another generic solution: @ranmocy https://leetcode.com/problems/single-number-ii/discuss/43368/Constant-space-solution/42363/ 
        # 不太懂 算了
        if nums == None: return 0
        x = [0, 0, 0]
        x[0] = ~0
        i = 0
        while i < len(nums):
            t = x[2]
            j = 2
            while j > 0:
                x[j] = (x[j-1] & nums[i]) | (x[j] & ~nums[i])
                j -= 1
            x[0] = (t & nums[i]) | (x[0] & ~nums[i])
            i += 1
        return x[1]
        """
