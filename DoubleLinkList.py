'''
Created on Sep 15, 2015

@author: ljiang
'''
class Node(object):
    '''
    Node of double linked list
    '''
    #pylint: disable-msg=R0904
    #pylint: disable-msg=R0903
    def __init__(self, value = None, prev = None, nxt = None):
        self.value = value
        self.prev = prev
        self.nxt = nxt

class DoubleLinkedList(object):
    def __init__(self, count = 0, head = Node(), tail = Node()):
        self.count = count
        self.head = head
        self.tail = tail
    def add_first_value(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.count+=1
    def add_node_tail(self, value):
        if self.count == 0:
            self.add_first_value(value)
        else:
            self.tail.nxt = Node(value, self.tail)
            self.tail = self.tail.nxt
            self.count+=1
    def add_node_head(self,value):
        if self.count == 0:
            self.add_first_value(value)
        else:
            new_node = Node(value, None, self.head)
            self.head.prev = new_node
            self.head = new_node
            self.count+=1
    def del_node(self, value):
        if self.count == 0:
            return False
        if self.count == 1:
            if self.head.value != value:
                return False
            else:
                self.__init__()
        elif self.count > 1:
            current = self.head
            while current != None:
                if current == self.tail:
                    if value != self.tail.value:
                        return False
                    else:
                        prev_node = current.prev
                        prev_node.nxt = None
                        self.tail.prev = None
                        self.tail = prev_node
                        self.count -= 1
                        return
                if current == self.head:
                    if value != self.head.value:
                        current = current.nxt
                    else:
                        nxt_node = current.nxt
                        nxt_node.prev = None
                        self.head.nxt = None
                        self.head = nxt_node
                        self.count-=1
                        return
                else:
                    if current.value != value:
                        current = current.nxt
                    else:
                        nxt_node = current.nxt
                        prev_node = current.prev
                        nxt_node.prev = prev_node
                        prev_node.nxt = nxt_node
                        current = Node()
                        return
    def display(self):
        '''Display the entire linked list'''
        current = self.head
        display_message=''
        if self.count == 0:
            display_message+="The doubly linked list is empty."
            return display_message
        if self.count ==1:
            display_message+="None <--- head (tail): %s ---> None" % current.value
            return display_message
        while current != None:
            if current == self.head:
                display_message+="<--- head: %s <--->" % current.value
            elif current == self.tail:
                display_message+=" tail: %s --->" % current.value
            else:
                display_message+=" node: %s <--->" % current.value
            current = current.nxt
        return display_message

def main():
    '''main funcs'''
    llst = DoubleLinkedList()
    llst.add_node_tail(1)
    llst.add_node_tail(2)
    llst.add_node_tail(3)
    llst.add_node_tail(4)
    print llst.display()

if __name__ == "__main__":
    main()

