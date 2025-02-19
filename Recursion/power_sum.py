def power_sum(array,power=1):
    #write code here
    total=0

    for i in array:
        if type(i)==list:
            total+=power_sum(i,power+1)
        else:
            total+=i
    return total ** (power)
        