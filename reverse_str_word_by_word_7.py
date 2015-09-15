
'''
Similar to Question [6. Reverse Words in a String], but with the following constraints:
The input string does not contain leading or trailing spaces and the words are always separated by a single space
Could you do it in-place without allocating extra space?

challenge: Rotate an array to the right by k steps in-place without allocating extra space. For instance, with k = 3, the array [0, 1, 2, 3, 4, 5, 6] is rotated to [4, 5, 6, 0, 1, 2, 3].
'''

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
        