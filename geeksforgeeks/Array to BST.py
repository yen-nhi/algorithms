class Node():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def build_bst_tree(nodes, l, r):
    if l > r:
        return None
    mid = l + ((r-l) // 2)
    node = nodes[mid]
    node.left = build_bst_tree(nodes, l, mid - 1)
    node.right = build_bst_tree(nodes, mid + 1, r)
    return node

def preorder(root, array):
    if root is None:
        return
    array.append(root.data)
    preorder(root.left, array)
    preorder(root.right, array)

for t in range(int(input())):
    n = int(input())
    nodes = [Node(int(i)) for i in input().split()]
    root = build_bst_tree(nodes, 0, n-1)
    array = []
    preorder(root, array)
    print(*array)