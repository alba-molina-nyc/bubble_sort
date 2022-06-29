# Bubble Sort

comparing an item in a list with the item to the right

1. start at index 0
2. compare item at index 0 with item at index 1

i.e.)

List = [7,4,1,2,3]
index0 = 7
index1 = 4

compare then if index0 > than index1 swap index0 with index1
List = [4,7,1,2,3]

index1 = 7
index2 = 1
move to index1 and index2
compare if index1 > index2 swap index1 with index2

List = [4,1,7,2,3]

move to index3 and index4
index2 = 7
index3 = 2
compare if index2 > index3 if it is then swap index3 with index4

List = [4,1,2,7,3]

move to index4 and index5
index4 = 7
index5 = 3
compare if index4 > than index 5 swap

List = [4,1,2,3,7]

## Go back to the beginning of the list and do it again

compare index0 with index1
index0 = 4
index1 = 1

if index 0 > index 1 swap

List = [1, 4, 2, 3, 7]

move to index1 and index2
if index1 > index2, swap

List = [1,2,4,3,7]

move to index2 and index3
if index2 > index3, swap

List = [1,2,3,4,7]

## things to keep in mind:

1. always start at index 0
2. then that index + 1
   - because you will be comparing index0 with index1
3. you keep comparing until you sort the largest number out
4. once you send the largest number to the end, you come back to the beginning and repeat that process again
