from typing import List

class Solution1:
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        #creating an empty array to store the result
        result = []

        #For loop to go through the nums array starting from position 0 and jumping from 2 to 2 numbers
        for i in range(0, len(nums), 2):
            #creating a variable freq to store the values ​​of nums in position i
            freq = nums[i]
            #creating a variable val to store the values ​​of nums in position i + 1
            val = nums[i + 1]
            #Creating variable to store the values ​​of the variable val within an array and multiplying by the frequency
            generetedList = [val] * freq 
            #putting the values ​​together
            result.extend(generetedList)

        return result
    #Runtime: 64 ms  Memory: 16.8 MB this solutions is faster and both has the same memory

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        #Constraints
        if len(nums) <= 2 and len(nums) <= 100:
            nums = nums
            
        if len(nums) % 2 == 0:
            rnums = nums
            
        for i in nums:
            if i > 100:
                nums = nums
                
        #Solution

        #creating an empty array to store the result
        result = []

        #For loop to go through the nums array starting from position 0 and jumping from 2 to 2 numbers
        for i in range(0, len(nums), 2):
            #creating a variable freq to store the values ​​of nums in position i
            freq = nums[i]
            #creating a variable val to store the values ​​of nums in position i + 1
            val = nums[i + 1]
            #Creating variable to store the values ​​of the variable val within an array and multiplying by the frequency
            generetedList = [val] * freq 
            #putting the values ​​together
            result.extend(generetedList)

    #Runtime: 67 ms  Memory: 16.8 MB this solutions is slower and both has the same memory 