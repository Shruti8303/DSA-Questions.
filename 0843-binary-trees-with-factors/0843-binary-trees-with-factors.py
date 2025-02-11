

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        arr.sort()  
        arr_set = set(arr)
        dp = {} 

        def dfs(num):
            if num in dp:
                return dp[num]
            
            count = 1  
            for j in arr:
                if j >= num:
                    break  
                if num % j == 0:
                    b = num // j
                    if b in arr_set:
                        count += dfs(j) * dfs(b)
                        count %= mod
            
            dp[num] = count
            return count

        return sum(dfs(num) for num in arr) % mod
