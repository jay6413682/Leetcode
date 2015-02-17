'''
Created on Mar 19, 2015

@author: ljiang
'''
from numpy import hsplit


def get_next_two(pattern):
    nxt = [0]
    now = 0
    x = 1
    while x < len(pattern):
        if pattern[now] == pattern[x]:
            nxt.append(now + 1)
            now += 1
            x += 1
        elif now:
            now = nxt[now - 1]
        else:
            x += 1
            nxt.append(0)
    return nxt


def get_next(pattern):
    nxt = []
    for i, _ in enumerate(pattern):
        for count in range(i, 0, -1):
            if pattern[:count] == pattern[i - count + 1:i + 1]:
                nxt.insert(i, count)
                break
        else:
            nxt.append(0)
    return nxt


def str_str_kmp(substr, strn):
    """ https://www.zhihu.com/question/21923021
    阮行止 的答案
    """
    i = 0
    j = 0
    nxt = get_next(substr)
    while i < len(strn):
        if substr[j] == strn[i]:
            j += 1
            i += 1
        else:
            if nxt[j] != 0:
                i += j - nxt[j]
            else:
                i += 1
            j = 0
        if j == len(substr):
            return i - j
    return -1


def str_str_one(substr, strn):
    if not substr not in strn:
        return -1
    return strn.index(substr)


def str_str_two(substr, strn):
    """ ... """
    if not isinstance(substr, str):
        return -1
    if not isinstance(strn, str):
        return -1
    if not substr and not strn:
        return 0
    if len(substr) > len(strn):
        return -1
    ind = 0
    offset = 0
    for i, _ in enumerate(strn):
        for _, schar in enumerate(substr):
            ind = i
            if schar == strn[ind + offset]:
                offset += 1
            else:
                offset = 0
                break
        else:
            return ind
    return -1


def str_str_three(substr, strn):
    if len(substr) > len(strn):
        return -1
    for i in range(len(strn) - len(substr) + 1):
        found = strn[i:i + len(substr)]
        if found == substr:
            return i
    return -1


def create_hash_val(strn, prime_num, base=26):
    """ To deal with integer overflow
    Has to mod to the prime number to lower the hash value at the expense of raise the rate of
    collision: https://www.youtube.com/watch?v=BfUejqd07yo&ab_channel=StableSort
    instead of choose multiplier 10 choose multipler 26 https://www.youtube.com/watch?v=BQ9E-2umSWc&ab_channel=TECHDOSE; also use ord value for each char
    the larger the prime, the less rate of collision

    1. instead of doing ord(chrt), do ord(chrt) - ord(a) + 1; this guarantees corresponding value of each char does not collide but making the value smaller thus less likely to be integer overflow
    (only pandas/numpy can overflow, so python shouldn't care); also less likely to cause collision;
    2. why mod prime number not other number? e.g. if x mode 2*103 prime number; if x == 1 or x == 2 , both give same mod outcome
    3. In other language which adopts fixed precison https://mortada.net/can-integer-operations-overflow-in-python.html
    in order to avoid integer overflow, the max num of prime number is the prime num closest to 2^64; this also saves a little memory even in python
    """
    real_hs = 0
    for i, chrt in enumerate(strn[::-1]):
        real_hs += pow(base, i) * (ord(chrt) - ord('a') + 1)
    return real_hs, real_hs % prime_num


def update_hash_val(old_hash, old_strn, new_char, prime_num, base=26):
    """ old hash for previous sub string, new strn is old strn moving one char to the right
    https://brilliant.org/wiki/rabin-karp-algorithm/
    in the link above, when look at Let’s use Rabin-Karp’s rolling hash to hash the alphabet. example
    consider the sum without mod prime number as the hash value. mod prime number is just a way to make the 
    hash smaller.
    H(“bcd”)=H(“abcd”)−H(“a___”) = H(“abc_”) + H("d") −H(“a___”) = H("abc") * 26 - H('a') * (26**3) +  H("d")
        = (MOD_H('abc') + X * Prime_numer) * 26 - ... = MOD_H('abc') * 26 + X * Prime_numer * 26 - ...
    MOD_H("bcd") = (MOD_H('abc') * 26 + X * Prime_numer * 26 - ...) % Prime_numer = (MOD_H('abc') * 26 - H('a') * (26**3) +  H("d")) % Prime_numer
    the old_hash passed in here is the mod hash not the real hash; the real (long) hash may cause integer overflow or occupy too much memory
    mod hash and long hash are equivalent:
    >>create_hash_val('ddd', 103)
    >>(2812, 31)
    >>update_hash_val(2812, 'ddd', 'd', 103)
    >>(2812, 31)
    >>update_hash_val(31, 'ddd', 'd', 103)
    >>(-69494, 31)

    If two string has same mod hash but different real hash, using mod hash to update hash val generates
    same mod and real hash; use real hash to update hash val generates same mod hash but different
    real hash

    >>create_hash_val('dlb', 103)
    >>(3018, 31)
    >>create_hash_val('ddd', 103)
    >>(2812, 31)
    >>update_hash_val(31, 'dlb', 'd', 103)
    >>(-69494, 31)
    >>update_hash_val(31, 'ddd', 'd', 103)
    >>(-69494, 31)
    >>update_hash_val(3018, 'dlb', 'd', 103)
    >>(8168, 31)
    >>update_hash_val(2812, 'ddd', 'd', 103)
    >>(2812, 31)
    In the collison case above, mod hash does not work correctly, but such case a rare; and will be handled when if substr_hash == target_hash:
    """
    raw_hash = (old_hash * base - (ord(old_strn[0]) - ord('a') + 1) * (base ** len(old_strn))) + ord(new_char) - ord('a') + 1
    return raw_hash, (raw_hash) % prime_num


def str_str_rolling_hash(strn, substr):
    """ Rabin–Karp algorithm (same as rolling hash)"""
    len_strn = len(strn)
    len_substr = len(substr)
    # larger the better , the closer to 2^64 the better
    prime_num = 103
    # base is 26 assuming all char are alphabetics
    base = 26
    substr_hash = create_hash_val(substr, prime_num, base)
    i = 0
    target_str = strn[i:i + len_substr]
    target_hash = create_hash_val(target_str, prime_num, base)

    while i < (len_strn - len_substr + 1):
        if substr_hash == target_hash:
            j = 0
            while j < len_substr:
                if target_str[j] != substr[j]:
                    break
                j += 1
            else:
                return i
        i += 1
        target_hash = update_hash_val(target_hash, target_str, strn[i + len_substr -1], prime_num, base)
        target_str = strn[i:i + len_substr]
    return -1



import itertools
class Str_Str_5:
    def __init__(self,needle,haystack):
        self.needle=needle
        self.haystack=haystack
    
    #brute force method 1, O(n^2)    
    def strStr(self):
        if len(self.needle)>10 or len(self.haystack)>10:
            return False
        if len(self.needle)==0:
            return 0
        if len(self.haystack)==0 and len(self.needle)==0:
            return 0     
        i=0
        j=0
        haystack_height=[]
        while i<len(self.haystack):
            while j<len(self.needle):
                if self.needle[j]!=self.haystack[i]:
                    break
                else:
                    j+=1
                    haystack_height.append(i)
                    break
            i+=1
        if len(haystack_height)!=len(self.needle):
            return False
        else:
            for i in xrange(0,len(haystack_height)-1):
                if haystack_height[i]-haystack_height[i+1]!=-1:
                    return False
            else:
                return haystack_height[0]
            
    #brute force 2; O(n^2)
    def strStr2(self):
        for i in itertools.count():
            for j in itertools.count():
                if j==len(self.needle):
                    return i
                if i+j==len(self.haystack):
                    return False
                if self.needle[j]!=self.haystack[i+j]:
                    break
    
    #brute force 4: O(n^2); the logic is almost the same as brute force 2
    def strStr5(self):
        for i in xrange(0,len(self.haystack)+1):
            for j in xrange(0,len(self.needle)+1):
                if j == len(self.needle):
                    return i
                if i+j==len(self.haystack):
                    return False

                if self.haystack[i+j]!=self.needle[j]:
                    break
               
        return False
                             
    #brute force 3; slice makes copies so the space complexity is high
    def strStr3(self):
        for i in xrange(0,len(self.haystack)-len(self.needle)+1):
            if self.haystack[i:i+len(self.needle)]==self.needle:
                return i
        return False
    
    #Rabin-Karp algorithm
    def strStr4(self):
        if len(self.needle)>10 or len(self.haystack)>10:
            return False
        if len(self.needle)==0:
            return 0
        if len(self.haystack)==0 and len(self.needle)==0:
            return 0     
        
        if len(self.haystack)<len(self.needle):
            return False
        def rollingHash(strg,length):
            hs=0
            for i in xrange(0,length):
                hs+=(255**i)*ord(strg[length-i-1])
            return hs
        
        def update(strg,hs,indx,length):
            if indx+length == len(strg):
                return
            y=ord(strg[indx])
            z=(255**(length-1))*y
            x=hs-z
            hs=x*255+ord(strg[indx+length])
            #hs=(hs-ord(strg[indx])*(255**(length-1)))*255+ord(strg[indx+length])
            return hs
                        
        needle_hash=rollingHash(self.needle, len(self.needle))
        haystack_hash=rollingHash(self.haystack, len(self.needle))
        length=len(self.needle)
        for j in xrange(0,len(self.haystack)-len(self.needle)+1):            
            if haystack_hash==needle_hash:
                return j
            haystack_hash=update(self.haystack,haystack_hash,j,length)        
        return False
            
        
                    