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
    if len(heights) <= h:
        heights.append(root.data)
    else:
        heights[h] += root.data
    sum_each_level(root.left, h + 1, heights)
    sum_each_level(root.right, h + 1, heights)
    
def maxLevelSum(root):
    heights = []
    sum_each_level(root, 0, heights)
    return max(heights)
