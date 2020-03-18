'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def constructTree(pre, preLN, n):
    '''
    Param: pre:  list of Preorder traversal of tree
    param:  preln: list indicating leaf or node
    param: n: no of nodes
    '''
    root = Node(pre[0])
    stack = [root]
    for i in range(1, n):
        node = Node(pre[i])
        if stack:
            if stack[-1].left == None:
                stack[-1].left = node
            elif stack[-1].right == None:
                stack[-1].right = node
            if stack[-1].left != None and stack[-1].right != None:
                stack.pop()
        if preLN[i] == 'N':
            stack.append(node)
    return root