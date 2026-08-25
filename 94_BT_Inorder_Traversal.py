'''
Q. Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''
# Ans :

def inorderTraversal(root):
    result = []

    def inorder(key):
        if key:
            inorder(key.left)
            result.append(key.val)
            inorder(key.right)

    inorder(root)
    return result

