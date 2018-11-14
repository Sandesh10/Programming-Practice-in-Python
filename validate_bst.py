'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.


'''
    
def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root==None:
        return True
    l = helper(root.left,float('-inf'),root.val)
    r = helper(root.right,root.val,float('inf'))
    return (l and r)


def helper(node,minval,maxval):
    if node==None:
        return True
    if node.val> minval and node.val <maxval:
        return helper(node.left,minval,node.val) and helper(node.right,node.val, maxval)
    else:
        return False


    
