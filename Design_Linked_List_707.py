
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList3:
    """ Linked List, with entinel node（dummy head), recommended: https://leetcode-cn.com/problems/design-linked-list/solution/she-ji-lian-biao-by-leetcode/ """

    def __init__(self):
        self.dummy_head = Node()
        self.count = 0

    def get_node(self, index: int) -> int:
        # print(index, self.count)
        if 0 <= index < self.count:
            steps = index + 1
            node = self.dummy_head
            while steps:
                node = node.next
                steps -= 1
            return node
        elif index == -1:
            return self.dummy_head
        return None

    def get(self, index: int) -> int:
        # print(index, self.count)
        node = get_node(index)
        if not node:
            return -1
        return node.val

    def get1(self, index: int) -> int:
        # print(index, self.count)
        if 0 <= index < self.count:
            steps = index + 1
            node = self.dummy_head
            while steps:
                node = node.next
                steps -= 1
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.count, val)

    def addAtIndex(self, index: int, val: int) -> None:
        pre = self.get_node(index - 1)
        if not pre:
            return
        nxt = pre.next
        pre.next = Node(val, nxt)
        self.count += 1

    def addAtIndex1(self, index: int, val: int) -> None:
        if 0 <= index <= self.count:
            steps = index
            pre = self.dummy_head
            # print(index, node.val, pre.val)
            while steps:
                pre = pre.next
                steps -= 1
            nxt = pre.next
            pre.next = Node(val, nxt)
            self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        pre = self.get_node(index - 1)
        if not pre or not pre.next:
            return
        pre.next = pre.next.next
        self.count -= 1

    def deleteAtIndex1(self, index: int) -> None:
        if 0 <= index <= self.count - 1:
            steps = index
            pre = self.dummy_head
            while steps:
                pre = pre.next
                steps -= 1
            pre.next = pre.next.next
            self.count -=1


class Node(object):
    """ Learn https://leetcode-cn.com/leetbook/read/linked-list """
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):
    """ Learn https://leetcode-cn.com/leetbook/read/linked-list
    https://leetcode-cn.com/leetbook/read/linked-list/jy291/
    无哨兵sentinel node（dummy head），不推荐
    """
    def __init__(self, head=None):
        """
        Initialize your data structure here.
        """
        self.head = head


    def get_node(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        pointer = 0
        curr_node = self.head
        while pointer < index:
            if curr_node is not None:
                curr_node = curr_node.next
            else:
                return None
            pointer += 1
        return curr_node


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr_node = self.get_node(index)
        if curr_node is None:
            return -1
        return curr_node.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.curr_head = self.head
        self.head = Node(val, self.curr_head)


    def traverse(self):
        curr_node = self.head
        if curr_node is None:
            return None
        while curr_node.next is not None:
            curr_node = curr_node.next
        return curr_node


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr_tail = self.traverse()
        if curr_tail is None:
            self.head = Node(val)
        else:
            curr_tail.next = Node(val)



    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
        if index < 0:
            return
        prev = self.get_node(index - 1)
        nxt = prev.next
        prev.next = Node(val, nxt)


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
            return
        if index < 0:
            return
        prev = self.get_node(index - 1)
        to_del = prev.next
        if to_del is None:
            return
        nxt = to_del.next
        if nxt is None:
            prev.next = None
            return
        prev.next = nxt


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class MyLinkedList2:
    """ 双链表： https://leetcode-cn.com/leetbook/read/linked-list/fabl3/

    without creating tail and size; a slower solution
    无哨兵sentinel node（dummy head），不推荐
    """

    def __init__(self, head=None):
        """
        Initialize your data structure here.
        """
        self.head = head

    def get_node(self, index: int) -> ListNode:
        pointer = self.head
        i = 0
        while i < index:
            pointer = pointer.next
            i += 1
        return pointer

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.get_node(index)
        if node is None:
            return -1
        else:
            return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = ListNode(val)
        new_head.next = self.head
        if self.head is None:
            self.head = new_head
            return
        self.head.prev = new_head
        self.head = new_head


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        pointer = self.head
        new_tail = ListNode(val)
        if pointer is None:
            self.head = new_tail
            return
        while pointer.next is not None:
            pointer = pointer.next

        pointer.next = new_tail
        new_tail.prev = pointer


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
        prev_node = self.get_node(index - 1)
        if prev_node is None:
            return
        curr_node = prev_node.next
        if curr_node is None:
            self.addAtTail(val)
            return
        node = ListNode(val)
        prev_node.next = node
        node.prev = prev_node
        node.next = curr_node
        curr_node.prev = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            nxt = self.head.next
            self.head.next = None
            self.head = nxt
        prev_node = self.get_node(index - 1)
        if prev_node is None:
            return
        curr_node = prev_node.next
        if curr_node is None:
            return
        next_node = curr_node.next
        prev_node.next = next_node
        if next_node is not None:
            next_node.prev = prev_node


class MyLinkedList:
    """ 双链表：我自己的解
    efficient solution
    """

    def __init__(self, head=ListNode(None), tail=ListNode(None)):
        """
        Initialize your data structure here.
        """
        self.size = 0
        # sentinel nodes as pseudo-head and pseudo-tail
        self.head = head
        self.tail = tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_node(self, index: int) -> ListNode:
        if -1 <= index <= self.size // 2:    
            pointer = self.head
            i = 0
            while i < index + 1:
                pointer = pointer.next
                i += 1
            return pointer
        elif index <= self.size:
            pointer = self.tail
            i = self.size
            while i > index:
                pointer = pointer.prev
                i -= 1
            return pointer
        return None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.get_node(index)
        if node is None or node is self.head or node is self.tail:
            return -1
        else:
            return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        prev_node = self.get_node(index - 1)
        if not prev_node or prev_node is self.tail:
            return
        curr_node = prev_node.next
        node = ListNode(val)
        prev_node.next = node
        node.prev = prev_node
        node.next = curr_node
        curr_node.prev = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr_node = self.get_node(index)
        if curr_node is None or curr_node is self.head or curr_node is self.tail:
            return
        prev_node = curr_node.prev
        next_node = curr_node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1



class MyLinkedList3:
    """ 双链表： https://leetcode.cn/problems/design-linked-list/solution/she-ji-lian-biao-by-leetcode-solution-abix/
    efficient solution

    如果你需要经常添加或删除结点，链表可能是一个不错的选择。

    如果你需要经常按索引访问元素，数组可能是比链表更好的选择。
    """

    def __init__(self, head=ListNode(None), tail=ListNode(None)):
        """
        Initialize your data structure here.
        """
        self.size = 0
        # sentinel nodes as pseudo-head and pseudo-tail
        self.head = head
        self.tail = tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_node(self, index: int) -> ListNode:
        if index <= self.size // 2:    
            pointer = self.head.next
            i = 0
            while i < index:
                pointer = pointer.next
                i += 1
            return pointer
        elif index < self.size:
            pointer = self.tail.prev
            i = self.size - 1
            while i > index:
                pointer = pointer.prev
                i -= 1
            return pointer
        return None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.get_node(index)
        if node is None:
            return -1
        else:
            return node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = ListNode(val)
        nxt = self.head.next
        self.head.next = new_head
        new_head.next = nxt
        new_head.prev = self.head
        nxt.prev = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_tail = ListNode(val)
        prev = self.tail.prev
        self.tail.prev = new_tail
        new_tail.next = self.tail
        prev.next = new_tail
        new_tail.prev = prev
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            prev_node = self.get_node(index - 1)
            curr_node = prev_node.next
            node = ListNode(val)
            prev_node.next = node
            node.prev = prev_node
            node.next = curr_node
            curr_node.prev = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr_node = self.get_node(index)
        if curr_node is None:
            return
        prev_node = curr_node.prev
        next_node = curr_node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
