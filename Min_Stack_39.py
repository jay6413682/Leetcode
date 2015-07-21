'''
Created on Jul 16, 2015

@author: ljiang
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
􏰀 push(x) – Push element x onto stack.
􏰀 pop() – Removes the element on top of the stack.
􏰀 top() – Get the top element.
􏰀 getMin() – Retrieve the minimum element in the stack.

'''
from Stack import Stack
class Min_Stack_39:
    def __init__(self):
        self.stk=Stack()
        self.minstk=Stack()
        
    def push(self,x):
        self.stk.push(x)
        if self.minstk.size()==0:
            self.minstk.push(x)
        else:
            for i in self.minstk.items:
                if x<i:
                    self.minstk.push(x)
            
    
    def pop(self):
        poped_item=self.stk.pop()
        if poped_item==self.minstk.peek():
            return self.minstk.pop()
    
    def top(self):
        return self.stk.peek()
    
    
    def getMin(self):
        return self.minstk.peek()