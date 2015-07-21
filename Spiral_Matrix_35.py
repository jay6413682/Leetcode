'''
Created on Jul 14, 2015

@author: ljiang

Given a matrix of mXn elements (m rows, n columns), return all elements of the matrix in spiral order.
For example, given the following matrix:
[
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

'''

class Spiral_Matrix_35:
    def __init__(self,matrix):
        self.matrix=matrix
        
    def traverse(self):
        n_len=len(self.matrix)
        m_len=len(self.matrix[0])
        row=0
        column=0
        #print n_len
        #print m_len
        result=[]
        while n_len>0 and m_len>0:
            i=0
            while i<m_len:               
                result.append(self.matrix[row][column])
                column+=1 
                i+=1               
            row+=1
            n_len-=1
            column-=1
            if n_len==0: return result
            i=0
            while i<n_len:
                result.append(self.matrix[row][column])
                row+=1
                i+=1
            row-=1
            column-=1
            m_len-=1
            if m_len==0: return result
            i=0
            while i<m_len:
                result.append(self.matrix[row][column])
                column-=1
                i+=1
            row-=1
            n_len-=1
            column+=1
            if n_len==0: return result
            i=0
            while i<n_len:
                result.append(self.matrix[row][column])
                row-=1     
                i+=1 
            m_len-=1
            column+=1
            row+=1     
            if m_len==0: return result
        return result     
                
            
            
                
        
        
