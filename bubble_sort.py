
"""
psuedo
step 1 take item at index 0 compare to item at index 1
if index 0 > index 1 --> swap items 
     0,1,2,3,4,5 (INDEX)
L = [4,2,6,5,1,3]
L = [2,4,6,5,1,3]

now compare item at index 1 (AKA the second item) to item at index 2 (AKA the third item)
     0,1,2,3,4,5 (INDEX)
L = [2,4,6,5,1,3]

if index 1 > index 2 --> swap 
if index 1 < index 2 --> leave it, move one position to the right (to be at index and compare item at index 2 with item at index 3)

and do the above RINSE AND REPEAT
"""
# L = [4,2,6,5,1,3]

def bubble_sort(L):
    for i in range(len(L) - 1, 0, -1):
        print(i)
        for j in range(i):
            print(j)
            if L[j] > L[j+1]:
                temp = L[j]  
                print(temp, 'temp')
                L[j] = L[j+1]
                L[j+1] = temp  
    return L

bubble_sort(L = [4,2,6,5,1,3])


"""
def bubble_sort(L):
    for i in range(len(L) - 1, 0, -1):
        for j in range(i):
            if L[j] > L[j+1]:
                temp = L[j]
                print(L)      
                L[j] = L[j+1]
                L[j+1] = temp  
    print(L)
    return L

bubble_sort(L = [4,2,6,5,1,3])
"""
