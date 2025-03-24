# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ''' res = []
        queue = deque([root])

        while queue:
            sum1 = 0
            count = len(queue)

            for _ in range(count): 
                node = queue.popleft()
                sum1 += node.val 
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(sum1 / count)  

        return res'''
        sum1=[]
        count=[]
        def dfs(root,depth):
            if not root:
                return
            if depth<len(sum1):
                sum1[depth]+=root.val
                count[depth]+=1
            else:
                sum1.append(root.val)
                count.append(1)
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        dfs(root,0)
        res=[]
        for i in range(len(sum1)):
            avg=sum1[i]/count[i]
            res.append(avg)
        return res



        