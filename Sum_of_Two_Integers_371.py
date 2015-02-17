

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
        a = a & 0xffff
        b = b & 0xffff
        # print(bin(a), bin(b))
        carry = ((a & b) << 1) & 0xffff
        raw_sum = a ^ b
        # print(bin(raw_sum), bin(carry))
        while carry:
            temp_sum = raw_sum ^ carry
            carry = ((raw_sum & carry) << 1) & 0xffff
            raw_sum = temp_sum
            # print(bin(sum_res), bin(carry))
        # if raw_sum >= 0x8000 it is at least 最高位是1，所以是负数
        return raw_sum if raw_sum < 0x8000 else ~(raw_sum ^ 0xffff)
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

