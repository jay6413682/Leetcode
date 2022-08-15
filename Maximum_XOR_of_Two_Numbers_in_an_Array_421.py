class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """ bit manipulation / 位运算 https://leetcode.cn/problems/maximum-xor-of-two-numbers-in-an-array/solution/li-yong-yi-huo-yun-suan-de-xing-zhi-tan-xin-suan-f/
        重点看@ ̶.̶G̶F̶u̶＇̶ 、̶ ̶| 的回复
        """
        res = 0
        # 每个数罪对32 位
        i = 32
        mask = 0
        temp_max = 0
        while i >= 0:
            # 从最左边一位开始 mask
            mask |= (1 << i)
            # prefix set 包含masked bits of 所有numbers，set 的话做 a ^ temp_max in prefix_set 复杂度比较低
            prefix_set = set()
            for num in nums:
                prefix_set.add(num & mask)
            # 假设 临时当前 前缀XOR 最大值：当前bit 为 1，左侧bits 为已知的前缀XOR最大值
            temp_prefix_max = res | (1 << i)
            for a in prefix_set:
                # 如果 a ^ max = b 成立 ，max 表示当前得到的“最大值”，那么一定有 a ^ b = max 成立
                if a ^ temp_prefix_max in prefix_set:
                    res = temp_prefix_max
                    break
                # 如果prefix_set 不存在这种 b 的话，那么当前位就为 0，因为下一个循环 temp_prefix_max = res | (1 << i) 就把下一位 设成 1了，当前位没做任何事。res实际为从左到右扫 直到当前 bit 的 prefix XOR 最大值
            i -= 1
        return res
