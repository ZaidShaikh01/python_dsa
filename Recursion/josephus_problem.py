
# Brute force apparoch way to delete 

def winner(n,k):
    arr=[i+1 for i in range(n)]
    def helper(arr,start_index):
        if len(arr)==1: return arr[0]
        # Recursive case
        index_to_remove = (start_index + k-1) % len(arr)
        del arr[index_to_remove]
        return helper(arr,index_to_remove)
    return helper(arr,0)


