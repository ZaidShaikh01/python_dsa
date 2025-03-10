def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []

        # Sorting the arrray as it is required

        nums.sort()

        def helper(temp,start,nums):
                # Base condition
                if output.__contains__(temp) == False:
                        output.append(temp.copy())

                # Iterating through choices
                for i in range(start,len(nums)):
                        # Validating the choice
                        temp.append(nums[i])
                        # backtracking 
                        helper(temp,i+1,nums)
                        # reverting to the original condition
                        temp.pop()
        helper([],0,nums)
        return output

'''

One more method to do the same without contains method

def subsetsWithDup(nums):

res = []
def helper(i,curr):
    if i == len(nums):
        res.append(curr[:])
        return
    
    #include
    curr.append(nums[i])
    helper(i+1,curr)
    curr.pop()

    #excluding part
    while i<len(nums)-1 and nums[i]==nums[i+1]:
        i++
    helper(i+1)
helper(0,[])
return res
'''