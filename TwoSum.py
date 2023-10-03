from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #assign the size of "nums" to "n"
        n = len(nums)

        #For loop to go through the indices of n 
        for i in range(n):                                                                      #O(n)
            #Second for loop to assign the index of i + 1
            for j in range(i + 1, n):                                                           #O(n)
                #check if (nums at index i) + (nums at index j) gives the value of the target
                if(nums[i] + nums[j] == target):
                    #If the condition is true then print the indices i and j
                    return[i, j]
        return[]
    #O(n^2)
    #Runtime: 2462ms Memory: 17 MB, it consumes less memory but is slower  
    
    
    
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Empty dictionary to store the values ​​of the nums list that have already been seen
        #along with the index
        seen = {}

        #For loop to get the values ​​and indices through the enumerate
        for i, num in enumerate(nums):                                                         #O(n)
            #condition to know if there is a number in "nums" that adds to the num
            #results in the value expected by the target
            if target - num in seen:
                #returns the index of the two numbers
                return ([seen[target - num], i])
            #Checks that the value of the num is not in the list so that the number is not repeated
            elif num not in seen:
                seen[num] = i
                
    #O(n)
    #Runtime: 57 ms Memory: 17.7 MB, that is, it consumes more memory but is faster than the first solution.