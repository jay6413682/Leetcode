'''
Created on Jul 12, 2015

@author: ljiang

'''
class Node:
    def __init__(self,value=None,nxt=None):
        self.nxt=nxt
        self.value=value
    def get_value(self):
        return self.value
    def get_next(self):
        return self.nxt
    
    def set_next(self,new_nxt):
        self.nxt=new_nxt
    
    
class LinkedList:
    def __init__(self,head_node):
        self.head_node=head_node
        
    def insert(self,value):
        new_node=Node(value)
        new_node.nxt=self.head_node
        self.head_node=new_node
    
    def append(self, value):
        new_node = Node(value)
        tail_node = self.traverse()
        tail_node.nxt = new_node
        
    def traverse(self):
        curr = self.head_node
        while curr.nxt != None:
            curr = curr.nxt
        return curr
        
    def size(self):
        current_node=self.head_node
        count=0
        while current_node!=None:
            count+=1
            current_node=current_node.nxt
        return count
    
    def search(self,data):
        current=self.head_node
        while current!=None:
            if current.value==data:
                return current
            current=current.nxt
        return None
    
    def delete(self,data):
        current=self.head_node
        prev_node=None
        while current!=None:
            if current.value==data and current==self.head_node:                
                self.head_node=current.nxt
                current.nxt=None
                break
            
            elif current.value==data:
                prev_node.nxt=current.nxt
                current.nxt=None
                break
            prev_node=current  
            current=current.nxt
