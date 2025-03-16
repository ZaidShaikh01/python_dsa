class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        arr=[1,2,3,4,5,6,7,8,9]
        res = []
        def helper(start,tempList,sum,arr):
            # base condtion
            if sum > n:
                return
            if len(tempList) == k and sum == n:
                res.append(tempList[:])
            
            # Iteration through choices
            for i in range(start,len(arr)):
                # adding in sum
                sum+=arr[i]
                # adding in templist
                tempList.append(arr[i])
                # calling the recursion
                helper(i+1,tempList,sum,arr)
                # backtracking the changes
                sum-=arr[i]
                tempList.pop()
        helper(0,[],0,arr)
        return res
            
