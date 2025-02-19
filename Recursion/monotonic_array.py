def monotonic_array(array):
    n=len(array)
    if n == 1 or n == 0:
        return True
    first=array[0]
    last=array[n-1]

    if first>last:
        # MD or not monotonic

        for k in range(n-1):
            if array[k] < array [k+1]:
                return False
    elif first == last:
        # M all values are equal
        for k in range(n-1):
            if array[k] != array[k+1]:
                return False
    else:
        # MI or not
        for k in range(n-1):
            if array[k] > array [k+1]:
                return False
    return True
