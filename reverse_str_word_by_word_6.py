'''
Created on May 3, 2015

@author: ljiang
Given an input string s, reverse the string word by word.
For example, given s = "the sky is blue", return "blue is sky the".
'''


def reverse_str_word_by_word_one(strn):
    rv_str = ''
    i = len(strn) - 1
    while i >= 0:
        if (strn[i] != ' ' and i == len(strn) - 1) or\
                (strn[i] != ' ' and strn[i + 1] == ' '):
            end_of_word = i
        elif (strn[i] != ' ' and i == 0) or\
                (strn[i] != ' ' and strn[i - 1] == ' '):
            start_of_word = i
            if len(rv_str) != 0:
                # not the first word
                rv_str += ' '
            rv_str += strn[start_of_word:end_of_word + 1]
        i -= 1
    return rv_str


class reverse_str_word_by_word_6:
    def __init__(self,words):
        self.words=words
        
    def reverse1(self):
        ##@my name is&Lei;my name\tis Lei;my name\nis Lei
        word=""
        word_lst=[]
        reversed_words=""
        for c in self.words:
            if not (c.isalpha() or c==" "):
                return False
        
        else:
            i=0
            for ch in self.words:
                if ch==" ":
                    word_lst.append(word)
                    word=""

                elif ch.isalpha():
                    word=word+ch                
                if i==len(self.words)-1:
                    word_lst.append(word)
                    word=""
                i+=1
            
            for wd in word_lst:
                if wd=="":
                    continue
                else:
                    reversed_words=wd+" "+reversed_words
            if reversed_words[len(reversed_words)-1]==" ":
                reversed_words=reversed_words.strip(' ')
        return reversed_words                    

    def reverse2(self):
        for c in self.words:
            if not (c.isalpha() or c==" "):
                return False
        words_lst=self.words.strip(' \t\n').split()
        reversed_words=""
        for word in words_lst:
            if words_lst.index(word)==0:
                reversed_words=word
            else:
                reversed_words=word+" "+reversed_words
                
        return reversed_words
                
    def reverse3(self):
        for c in self.words:
            if not (c.isalpha() or c==" "):
                return False
        self.words=self.words.strip(' \t\n')
        i=len(self.words)-1
        start=len(self.words)-1
        end=len(self.words)-1
        words_list=[]
        reversed_words=""
        while i >=0:
            if i==0:
                words_list.append(self.words[start:end+1])
                break
            if self.words[i]==" ":
                if start!=end:
                    words_list.append(self.words[start+1:end+1])
                start-=1
                end=start
            else:
                start-=1
            i-=1
        j=0
        for word in words_list:
            if j==0:
                reversed_words=word
            else:
                reversed_words=reversed_words+" "+word
            j+=1
        return reversed_words
    
    #rewrite reverse3
    def reverse4(self):
        for c in self.words:
            if not (c.isalpha() or c==" "):
                return False
        self.words=self.words.strip(' \t\n')
        i=len(self.words)-1
        start=len(self.words)-1
        end=len(self.words)-1
        #words_list=[]
        reversed_words=""
        while i >=0:
            if self.words[i]==" " or i==0:
                if i==0:
                    reversed_words=reversed_words+" "+self.words[start:end+1]
                    break
                if start!=end:
                    #words_list.append(self.words[start+1:end+1])
                    if end==len(self.words)-1:
                        reversed_words=self.words[start+1:end+1]
                    else:
                        reversed_words=reversed_words+" "+self.words[start+1:end+1]
                start-=1
                end=start
            else:
                start-=1
            i-=1
        '''
        j=0
        for word in words_list:
            if j==0:
                reversed_words=word
            else:
                reversed_words=reversed_words+" "+word
            j+=1
        '''
        return reversed_words    
        