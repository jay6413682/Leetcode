'''
Created on Jul 16, 2015

@author: ljiang
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
􏰀 push(x) – Push element x onto stack.
􏰀 pop() – Removes the element on top of the stack.
􏰀 top() – Get the top element.
􏰀 getMin() – Retrieve the minimum element in the stack.

'''


class MinStack:
    """
    solution 1 of
    https://leetcode-cn.com/problems/min-stack/solution/zui-xiao-zhan-by-leetcode-solution/
    needs to create a new stack thus needs more space
    时间复杂度：对于题目中的所有操作，时间复杂度均为 O(1)O(1)。因为栈的插入、删除与读取操作都是 O(1)O(1)，我们定义的每个操作最多调用栈操作两次。

    空间复杂度：O(n)O(n)，其中 nn 为总操作数。最坏情况下，我们会连续插入 nn 个元素，此时两个栈占用的空间为 O(n)O(n)。

    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.data_stack = []


    def push(self, x: int) -> None:
        self.data_stack.append(x)
        if not self.min_stack or (self.min_stack and self.min_stack[-1] >= x):
            self.min_stack.append(x)

    def pop(self) -> None:
        popped = self.data_stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.data_stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1]


class MinStack2:
    """ solution 2 of video of
    https://leetcode-cn.com/problems/min-stack/solution/zui-xiao-zhan-by-leetcode-solution/
    time complexity: O(1)
    space complexity: O(n)
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x: int) -> None:
        if not self.stack or self.stack[-1][1] > x:
            self.stack.append((x, x))
        else:
            self.stack.append((x, self.stack[-1][1]))

    def pop(self) -> None:
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




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