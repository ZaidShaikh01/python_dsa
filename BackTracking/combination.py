def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(temp,start,n,k):
                
                # base condition
                if len(temp) == k:
                        res.append(temp[:])
                        return
                # Iteration on choices

                for i in range(start,n+1):
                        # adding the element 
                        temp.append(i)

                        # Calling backtracking
                        backtrack(temp,i+1,n,k)

                        # Removing the element

                        temp.pop()
                        
        
        backtrack([],1,n,k)
        return res