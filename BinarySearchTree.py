'''
Created on Oct 9, 2015

@author: ljiang
'''
class Node(object):
    def __init__(self, data, level, left, right):
        self.left = left
        self.right = right
        self.data = data
        self.level = level

class BinarySearchTree(object):
    def __init__(self, root):
        self.root = root
    def create(self, data):
        if self.root == None:
            self.root = Node(data, 0, None, None)
        else:
            current = self.root
            while 1:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        left_level = current.level + 1
                        current.left = Node(data, left_level, None, None)
                        current = current.left
                        break
                elif data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        right_level = current.level + 1
                        current.right = Node(data, right_level, None, None)
                        break
                else:
                    break
    #Depth First Traversals: (a) Inorde (b) Preorde (c) Postorder
    def inorder_ascend(self, node, str_to_print = ''):
        if node:
            str_to_print = self.inorder_ascend(node.left, str_to_print) + ' '
            str_to_print += str(node.data) + ' '
            str_to_print = self.inorder_ascend(node.right, str_to_print) + ' '
        return str_to_print.strip()

    def inorder_descend(self, node, str_to_print = ''):
        if node:
            str_to_print = self.inorder_descend(node.right, str_to_print) + ' '
            str_to_print += str(node.data) + ' '
            str_to_print = self.inorder_descend(node.left, str_to_print) + ' '
        return str_to_print.strip()

    def preorder(self, node, str_to_print = ''):
        if node:
            str_to_print += str(node.data) + ' '
            str_to_print = self.preorder(node.left, str_to_print) + ' '
            str_to_print = self.preorder(node.right, str_to_print) + ' '
        return str_to_print.strip()

    def postorder(self, node, str_to_print = ''):
        if node:
            str_to_print = self.postorder(node.left, str_to_print) + ' '
            str_to_print = self.postorder(node.right, str_to_print) + ' '
            str_to_print += str(node.data) + ' '
        return str_to_print.strip()

    #Breadth First Traversals
    def bft(self):
        queue = [self.root]
        str_to_print = ''
        while len(queue) > 0:
            current_node = queue.pop(0)
            str_to_print += str(current_node.data) + ' '
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return str_to_print.rstrip()
                    