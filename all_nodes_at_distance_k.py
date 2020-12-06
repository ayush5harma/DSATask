# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distanceK(root, target, K):
    ans = []

    # Return distance from node to target if exists, else -1
    # Vertex distance: the # of vertices on the path from node to target
    def dfs(node):
        if not node:
            return -1
        elif node is target:
            subtree_add(node, 0)
            return 1
        else:
            L, R = dfs(node.left), dfs(node.right)
            if L != -1:
                if L == K: ans.append(node.val)
                subtree_add(node.right, L + 1)
                return L + 1
            elif R != -1:
                if R == K: ans.append(node.val)
                subtree_add(node.left, R + 1)
                return R + 1
            else:
                return -1

    # Add all nodes 'K - dist' from the node to answer.
    def subtree_add(node, dist):
        if not node:
            return
        elif dist == K:
            ans.append(node.val)
        else:
            subtree_add(node.left, dist + 1)
            subtree_add(node.right, dist + 1)

    dfs(root)
    return ans
        
root = TreeNode(20) 
root.left = TreeNode(8) 
root.right = TreeNode(22) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(12) 
root.left.right.left = TreeNode(10) 
root.left.right.right = TreeNode(14) 
target = root.left.right 
distanceK(root, target, 2)
