'''
#MAANG Question

Write a program to find all pairs of integer array whoose sum is equal to a given numbers.

Eg: [2,6,3,9,11] --> [6,3]

#Questions based on the problem above:
* Does array contain only +ve or -ve numbers ?
* What if the same pair repeats twice, should we print it every time ?
* If the reverse of the pair is acceptable. 
    Eg: Can we print both (4,1) and (1,4) if the given numbers sum is 5. 
* Do we need to print only distinct pairs ?
* Does (3,3) is a valid pair for a given sum of 6 ?
* How big is the array ?

#The pairs have to be distinct. Therefore (2,2) or (3,3) is NOT a valid pair.

'''

 

def findPairs (nums, target):
    for i in range(len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i,j)

mylist = [1,2,3,2,3,4,5,6]
findPairs(mylist, 6)
