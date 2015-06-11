'''
Created on Jun 10, 2015

@author: ljiang
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

'''
class atoi_8:
    def __init__(self):
        pass
    
    def atoi(self,strg):
        i=0
        intg=0
        strg=strg.strip(" ")
        sign=1
        if strg=="":
            return 0
        if strg[0]=="-" and strg[1].isdigit():
            sign=-1
            intg=sign*int(strg[1])
            i+=2

                
        #strg=strg.strip("-")
        while i < len(strg):
            if strg[i]==" ":
                return 0

            elif strg[i].isdigit():
                if i==0:
                    intg=int(strg[i])
                else:
                    if ((intg>0 and intg<214748364) or (intg==214748364 and int(strg[i])<=7)): 
                        intg=intg*10+int(strg[i])
                    elif ((intg<0 and intg>-214748364) or (intg==-214748364 and int(strg[i])<=8)):    
                        intg=intg*10-int(strg[i])
                    else:
                        return 0
            else:
                return intg            
            i+=1
        
        
        return intg