class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        # Here will be a helper funcion
        def helper(res,temp,start,candidates,target,sum):
            # Base conditons
            if sum > target:
                return
            if sum == target and res.__contains__(temp) == False :
                res.append(temp[:])
            for i in range(start,len(candidates)):
                # adding the value in temp list
                sum+=candidates[i]
                # adding in tempList
                temp.append(candidates[i])
                
                # calling the backtrack funtion
                helper(res,temp,i+1,candidates,target,sum)

                # Reverting the values
                sum-=candidates[i]
                temp.pop()

        # Here is helper funcion call
        helper(res,[],0,candidates,target,0)
        # Returning the res
        return res