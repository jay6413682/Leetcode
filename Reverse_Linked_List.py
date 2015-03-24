'''
Created on Mar 23, 2015

@author: ljiang
'''

class Node:
    def __init__(self,value,nxt):
        self.value=value
        self.nxt=nxt

#Reverse the linked list recursively
def reverse(node,last):
    if node == None:
        return last
    nxt=node.nxt
    node.nxt=last
    return reverse(nxt,node)

#Reverse the linked list iteratively
def reverse2(node):
    last=None
    current=node
    while current!=None:
        nxt=current.nxt
        current.nxt=last
        last=current
        current=nxt
    return last

        
        


n0=Node(4,None)
n1=Node(3,n0)
n2=Node(2,n1)
n3=Node(1,n2)
n4=Node(0,n3)

'''
node=reverse(n4,None)
while node != None:
    print node.value
    node=node.nxt
'''    
node2=reverse2(n4)
while node2 != None:
    print node2.value
    node2=node2.nxt    