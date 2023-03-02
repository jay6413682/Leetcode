

class Solution:
    def getSum(self, a: int, b: int) -> int:
        """ bit manipulation, my latest try """
        i = 0
        carry = 0
        res = 0
        while i < 12:
            curr_a_bit = (a >> i) & 1
            curr_b_bit = (b >> i) & 1
            # print(curr_a_bit, curr_b_bit)
            curr_bit = curr_a_bit ^ curr_b_bit ^ carry
            res |= (curr_bit << i)
            if curr_a_bit & curr_b_bit == 1 or curr_a_bit & carry == 1 or curr_b_bit & carry == 1:
                carry = 1
            else:
                carry = 0
            i += 1
        # print(res, bin(res), bin(a), bin(b))
        # 不用把 第 13 位 i = 12 时 carry 加上 result, 因为 这一位 判断 正 负 不需要
        if res >= 2 ** 11:
            # 举例：最大和2000 ，res < 2 ^ 11, 最小和 -2000， res > 2 ^ 11
            # 如果 和 是 0，比如 1 和 -1， res = 0
            # 如果和 是 -1，比如 1 和 -2， res > 2 ^ 11
            res = (~res) ^ 0b111111111111
        return res


class Solution:
    """ https://leetcode-cn.com/problems/sum-of-two-integers/solution/python-wei-yun-suan-yi-xie-keng-by-lih/
    将无符号整型结果根据范围判定,映射为有符号整型：比如
    1. 结果 与 0b1111 异或
    2. 对异或结果按位取反
        ~(a ^ 0xF)
    解释不错但是python 解法就算了：https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-xiang-jie-yi-ji-zai-python-zhong-xu-y/
    还有一种python 解法也可以理解 但是理解上面这种就可以了： https://leetcode-cn.com/problems/sum-of-two-integers/solution/liang-zheng-shu-zhi-he-by-leetcode-solut-c1s3/
    """
    def getSum(self, a: int, b: int) -> int:
        # my solution:
        # 转化为无符号整数, 注意 如果 a 或 b 是 负数，比如 a 是 -1 (补码 0xffff...ffff ) , & 0xffff 就转化为 0x0000...0000ffff保留低位, 假设b是 0，a + b是0x0000...0000ffff，由于大于最大和2000，所以必然是负数，所以先^ 0xffff -> 0x0000...00000000, 再取反 -> 0xffff...ffff
        # 选择0xffff （0xfff就够了其实） 的原因是可以保留负数的高位的1s，比如 a 如果为正数最大1000，那么-1 & 0xffff 后得到的0x0000...0000ffff 由于大于1000所以必然是负数，所以最后可以通过~(raw_sum ^ 0xffff)，先低位取反，再全部取反 -> 最终效果是低位不变 （原本最开始低位就保留了，全是1），高位取反（变回1）
        a = a & 0xfff # 0xffff is ok too
        b = b & 0xfff
        # print(bin(a), bin(b))
        carry = ((a & b) << 1) & 0xfff  # 把左侧溢出0xfff 的1 去掉，因为无论 怎样 a + b 都不会超出0xfff，而且carry 相当于一个加数，跟a，b 一样
        raw_sum = a ^ b
        # print(bin(raw_sum), bin(carry))
        while carry:
            # 如果进位结果仍不是0，不断地跟 进位结果 做 无进位加法
            temp_sum = raw_sum ^ carry
            # 同时跟进位结果 算出 是否仍需 进位
            carry = ((raw_sum & carry) << 1) & 0xfff # 如果不& 0xfff，carry 有可能变成0x1000(a = -1, b = 1), 此时raw_sum 为0x000，下一步temp_sum就变成 0x1000。。。
            raw_sum = temp_sum
            # print(bin(sum_res), bin(carry))
        # a+b 最大 2000 < 2 ** 11, if raw_sum >= 0x800 (2 ** 11) it is at least 最高位是1，所以是负数
        return raw_sum if raw_sum < 0x800 else ~(raw_sum ^ 0xfff)
        '''
        a &= 0xffffffff
        b &= 0xffffffff
        while b:
            carry = a & b
            a ^= b
            b = carry << 1 & 0xffffffff
        return a if a < 0x80000000 else ~(a ^ 0xffffffff)
        '''


class Solution:
    """ My own solution, not really working """
    def getSum(self, a: int, b: int) -> int:
        sum = 0
        mask = 1
        new_a = a & 0xffffffff
        new_b = b & 0xffffffff
        carry = 0
        negative = False
        counter = 0
        while new_a != 0 or new_b != 0:
            x = mask & a
            y = mask & b
            z = mask & carry
            if (x != 0 and y != 0) or (x != 0 and z != 0) or (z != 0 and y != 0):
                carry = mask << 1
            else:
                carry = 0
            this_bit = x ^ y ^ z
            if counter == 31 and this_bit >> 31 == 1:
                negative = True
            sum |= this_bit
            new_a >>= 1
            new_b >>= 1
            mask <<= 1
            counter += 1
        negative_mask = 0xffffffff
        if carry != 0:
            sum |= carry
            if negative:
                negative_mask = 0x1ffffffff
            else:
                sum ^= 1 << counter
        return sum if negative is False else ~(sum ^ negative_mask)
        """
        # my solution 2, similar to https://leetcode-cn.com/problems/sum-of-two-integers/solution/gong-shui-san-xie-shi-yong-wei-yun-suan-4hpb7/
        # not working for negative number yet
        sum_res = 0
        carry = 0
        shift = 1
        while a or b or carry:
            bit_a = a & 1
            bit_b = b & 1
            if bit_a and bit_b:
                if carry:
                    sum_bit = 1
                else:
                    sum_bit = 0
                carry = 1
            else:
                tmp_bit = (bit_a ^ bit_b)
                if tmp_bit and carry:
                    sum_bit = 0
                    carry = 1
                else:
                    sum_bit = tmp_bit ^ carry
                    carry = 0
            temp_shift = shift
            while temp_shift != 1:
                sum_bit <<= 1
                temp_shift >>= 1
            shift <<= 1
            sum_res |= sum_bit
            a >>= 1
            b >>= 1
            # print(sum_res)
        return sum_res
        
        """

