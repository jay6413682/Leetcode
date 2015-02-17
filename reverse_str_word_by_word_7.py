
'''
Similar to Question [6. Reverse Words in a String], but with the following constraints:
The input string does not contain leading or trailing spaces and the words are always separated by a single space
Could you do it in-place without allocating extra space?

challenge: Rotate an array to the right by k steps in-place without allocating extra space. For instance, with k = 3, the array [0, 1, 2, 3, 4, 5, 6] is rotated to [4, 5, 6, 0, 1, 2, 3].
'''


def reverse_lst(strn_list):
    i = 0
    while i < len(strn_list) // 2:
        strn_list[i], strn_list[len(strn_list) - 1 - i] = strn_list[len(strn_list) - 1 -i], strn_list[i]
        i += 1
    return strn_list


def reverse_words_one(strn):
    strn = ''.join(reverse_lst(list(strn)))
    i = 0
    word_started = False
    word_end = 0
    word_start = 0
    while i < len(strn):
        if strn[i] == ' ':
            word_end = i - 1
            word_started = False
            new_word = ''.join(reverse_lst(list(strn[word_start:word_end + 1])))
            strn = strn.replace(strn[word_start:word_end + 1], new_word, 1)
        else:
            if not word_started:
                word_start = i
            word_started = True
        i += 1
    return strn


def rotate_array(a_list, k):
    """
    Rotate an array to the right by k steps in-place without allocating extra space. For instance, with k = 3, the array [0, 1, 2, 3, 4, 5, 6] is rotated to [4, 5, 6, 0, 1, 2, 3].
    """
    reversed_list = reverse_lst(a_list)
    return reverse_lst(reversed_list[:k]) + reverse_lst(reversed_list[k:])


class reverse_str_word_by_word_7:
    def __init__(self):
        pass
    
    def reverse_string(self,strg):
        i=0
        strg=list(strg)
        while i<len(strg)/2:
            strg[i],strg[len(strg)-i-1]=strg[len(strg)-i-1],strg[i]
            i+=1
        return "".join(strg)
    
    def reverse_words(self,words):
        
        words=self.reverse_string(words)
        for word in words.split(" "):
            
            new_word=self.reverse_string(word)
            words=words.replace(word,new_word,1)
            
        return words

    def rotate_words(self,words,k):
        words=self.reverse_string(words)
        words=self.reverse_string(words[:k])+self.reverse_string(words[k:len(words)])
        return words
        