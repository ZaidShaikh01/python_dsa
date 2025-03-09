def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []

        def helper(nums,i,subset):
                if i == len(nums):
                        output.append(subset.copy())
                        return
                helper(nums,i+1,subset)
                subset.append(nums[i])
                helper(nums,i+1,subset)
                subset.pop()
        helper(nums,0,[])
        return output


'''
This can work or you can also write this


res= []

def helper(nums,start,temp):
    res.append(temp.copy())

    for i in range(start,len(nums)):
        # Adding element
        temp.append(nums[i])
        # Backtracking to next element
        helper(nums,i+1,temp)
        # Removing the last element
        temp.pop()
helper(nums,0,[])
return res
'''