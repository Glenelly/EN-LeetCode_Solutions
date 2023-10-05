from typing import List

class Solution1:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        #Constraints
        if n <= 1 or n <= 500:
            n = n
        
        for i in nums:
            if i > 1000:
                break
            else:
                nums = nums
                
        #Solution
        
        #Creating an empty array that will store the value of the result
        emptyArray = []

        #for loop to loop the number that is stored in variable n
        for i in range(n):
            #Saving the values ​​of nums in position i
            emptyArray.append(nums[i])
            #Saving the values ​​of nums in position i + n
            emptyArray.append(nums[i + n])

        return emptyArray
    
    #Runtime: 56 ms Memory: 16.4 MB This solution is faster and takes up more memory

class Solution2:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        #Creating an empty array that will store the value of the result
        emptyArray = []

       #for loop to loop the number that is stored in variable n
        for i in range(n):
            #Saving the values ​​of nums in position i
            emptyArray.append(nums[i])
            #Saving the values ​​of nums in position i + n
            emptyArray.append(nums[i + n])

        return emptyArray
    
     #Runtime: 59 ms Memory: 16.3 MB This solution is slower and takes up less memory  