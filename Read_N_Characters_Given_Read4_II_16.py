"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""
file_content = ['a', 'b']


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    """ This is copied from https://www.cnblogs.com/lightwindy/p/8481805.html """
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1
 
    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i


class SolutionOne:
    def __init__(self):
        self.buf4 = [''] * 4
        self.num_chars_to_read_next_time = 0
        self.eof = False
    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        num_chars_read = 0
        # deal with chars left over last time
        if self.num_chars_to_read_next_time > 0:
            new_real_buf4 = []
            for i in self.buf4:
                if i != '':
                    new_real_buf4.append(i)
            buf[:] = new_real_buf4[-1 * self.num_chars_to_read_next_time:]
            num_chars_read = self.num_chars_to_read_next_time
            self.num_chars_to_read_next_time = 0
        # if need call read4
        while self.eof is False and num_chars_read < n:
            num_chars_read4 = read4(self.buf4)
            if num_chars_read4 < 4:
                self.eof = True
                if n < num_chars_read4:
                    num_chars_to_read_this_time = n
                    self.num_chars_to_read_next_time = num_chars_read4 - n
                else:
                    num_chars_to_read_this_time = num_chars_read4
                    self.num_chars_to_read_next_time = 0
            else:
                num_chars_to_read_this_time = num_chars_read4 if num_chars_read4 < n - num_chars_read else n - num_chars_read
                self.num_chars_to_read_next_time = 4 - num_chars_to_read_this_time

            buf[num_chars_read:] = self.buf4[:num_chars_to_read_this_time]
            num_chars_read += num_chars_to_read_this_time
        return num_chars_read


class SolutionTwo:
    """ https://github.com/BruceWeng/Leetcode-Python/blob/master/158.%20Read%20N%20Characters%20Given%20Read4%20II%20-%20Call%20multiple%20times.py """
    def __init__(self):
        self.buff4Ptr = 0
        self.buff4Cnt = 0
        self.buff4 = [" "] * 4

    """
    @param {str[]} buf: Destination buffer
    @param {int} n: Maximum number of characters to read
    @return {str} The number of characters read
    """
    def read(self, buf, n):
        ptr = 0
        while ptr < n:
            if self.buff4Ptr == 0:
                self.buff4Cnt = Reader.read4(self.buff4)
            if self.buff4Cnt == 0:
                break
            while self.buff4Ptr < self.buff4Cnt and ptr < n:
                buf[ptr] = self.buff4[self.buff4Ptr]
                self.buff4Ptr += 1
                ptr += 1
            if self.buff4Ptr >= self.buff4Cnt:
                self.buff4Ptr = 0

        return ptr
