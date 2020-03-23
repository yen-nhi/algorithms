'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

def isBST(node):
    max_val = float("inf")
    min_val = float("-inf")
    return check_BST(node, max_val, min_val)


def check_BST(node, max_val, min_val):
    if node is None:
        return True
    if node.data >= max_val or node.data <= min_val:
        return False
    return check_BST(node.left, node.data, min_val) and check_BST(node.right, max_val, node.data)
