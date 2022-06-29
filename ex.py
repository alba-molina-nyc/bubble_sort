def bubble_sort(L):
    # for loop - range is the len of list -1, start at 0, increment by -1
    for i in range(len(L) -1 , 0, -1):
        # for loop that is going to move us forward through the list
        for j in range(i):
            # if j(index 0) > j+1(index1)
            if L[j] > L[j+1]:
                # temp holds L[j]
                temp = L[j]
                # L[j] moved over one
                L[j] = L[j+1]
                # now that it is moved we hold L[j+1] with temp
                L[j+1] = temp
    return L



bubble_sort(L=[4,2,6,5,1,3])

