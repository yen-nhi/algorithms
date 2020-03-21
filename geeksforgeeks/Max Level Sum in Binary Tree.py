# Your task is to complete this function
# function should return max sum level in the tree
'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''
def sum_each_level(root, h, heights):
    if root is None:
        return
    if heights[h] is None:
        heights[h] = root.data
    else:
        heights[h] += root.data
    sum_each_level(root.left, h + 1, heights)
    sum_each_level(root.right, h + 1, heights)

def find_max(heights):
    i = 0
    max_int = float("-inf")
    while heights[i] is not None:
        if heights[i] > max_int:
            max_int = heights[i]
        i += 1
    return max_int

def maxLevelSum(root):
    heights = [None] * 10000
    sum_each_level(root, 0, heights)
    return find_max(heights)
