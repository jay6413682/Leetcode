'''
Created on Jul 13, 2015

@author: ljiang
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

from LinkedList import Node,LinkedList

class Merge_Two_Sorted_List_20:
    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2
        
    def merge(self):
        pass
        current1=self.l1.head_node
        current2=self.l2.head_node
        merged_llist=LinkedList(Node())
        merged_llist_current=merged_llist.head_node
        while current1!=None and current2!=None:
            if current1.value>current2.value:
                merged_llist_current.nxt=current1                
                current1=current1.nxt
            else:
                merged_llist_current.nxt=current2
                current2=current2.nxt
            merged_llist_current=merged_llist_current.nxt
                    
        if current1!=None:
            merged_llist_current.nxt=current1
        if current2!=None:
            merged_llist_current.nxt=current2

        merged_llist.delete(None)        
        return merged_llist           
    