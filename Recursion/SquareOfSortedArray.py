
def sorted_squared(array):
    '''

    Brute apparoch

    n=len(array)
    res=[0]*n
    for i in range(n):
        res[i]=array[i]**2
    res.sort()
    '''

    # optimal apparoch by using two pointers
    i=0
    j= len(array)-1
    new_arr =[0]*len(array)
    for k in reversed(range(len(array))):
        sq_i = array[i]**2
        sq_j=array[j]**2
        if sq_i >sq_j:
            new_arr[k]=sq_i
            i+=1
        else:
            new_arr[k]= sq_j
            j-=1
    return new_arr


arr=[-1,-2,-3,0,12,14,16]
arr=sorted_squared(arr)
print(arr)