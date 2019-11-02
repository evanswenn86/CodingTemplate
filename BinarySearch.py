def binSearch(self,nums, target):
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if nums[mid] > target:
            end = mid
        else:
            start = mid

    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    else:
        return -1


# 找旋转数组最小值
def findMin(self, A):
    # write your code here
    start, end = 0, len(A) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if A[mid] < A[end]:
            end = mid
        else:
            start = mid

    if A[start] < A[end]:
        return A[start]
    return A[end]

# 二叉树迭代器
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        dummy = TreeNode(0)
        dummy.right = root
        self.stack = [dummy]
        self.next()

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return bool(self.stack)

    """
    @return: return next node
    """
    def next(self):
        node = self.stack.pop()
        next_node = node
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return next_node
