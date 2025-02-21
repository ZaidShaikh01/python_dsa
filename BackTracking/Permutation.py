def permuteUnique(self, nums):
    res=[]

    def helper(i):
        #base condition 
        if i == len(nums)-1:
            res.append(nums[:])
            return
        # recursive case
        hash={}
        for j in range(i,len(nums)):
            if nums[j] not in hash:
                hash[nums[j]]=True
                nums[i],nums[j]=nums[j],nums[i]
                helper(i+1)
                nums[i],nums[j]=nums[j],nums[i]
    helper(0)
    return res
'''
        So, Na it's a back tracking problem pr yaha pe na jo hash map hai usko use kiya hai takii apan track kar sake j ki value ko ki kya vo repeate hori
        agar nahi hori to uskko apan if me jaake baki opertaion karne dere pr agar already exist karti hai to apan usko block me jane hi nai dere
        so, it's not working for that reason.

        That's it. ANd that's why hash map is used. It's storing key as int and boolean as values
'''