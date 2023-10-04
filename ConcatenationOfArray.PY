from typing import List

class Solution1:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
    
class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        #assigns the size of the nums array
        n = len(nums)
        #creates an empty array
        ans = []

        #for loop to go through the size of the nums array
        for i in range(n):
            #Assigns the values ​​from the nums array to the ans array
            ans.append(nums[i])
            #Join the values ​​of the two arrays
            concatenation = nums + ans 
            
        return(concatenation)
