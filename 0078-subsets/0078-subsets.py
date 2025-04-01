class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def recu(start,path):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                print(path)
                recu(i+1,path)
                path.pop()

        recu(0,[])
        return res
        