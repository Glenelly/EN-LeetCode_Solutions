from typing import List

class Solution1:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        #Constraints
        
        n = len(candies)
                
        if(n <= 2 and n <=100):
            n = n
                    
        for i in candies:
            if i > 100:
                return(i)
                break
        
        if extraCandies > 50:
            return(extraCandies)
            
        #solution
        
        #creating an empty array to store the result
        result = []
        #variable to store the maximum value of the candy array
        maxValue = max(candies)

        #for loop to go through the indices in the size of the candy array
        for i in range(n):
            #checking whether the value stored in the candies array at position i plus the value of extraCandies
            #is greater than the largest value stored in the candy array
            if candies[i] + extraCandies >= maxValue:
                result.append(True)
            else: 
                result.append(False)
                
        return result
    
    #Runtime: 49 ms Memory: 16.1 MB This solution is faster and takes up less memory 

        
class Solution2:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        n = len(candies)

         #creating an empty array to store the result
        result = []
        #variable to store the maximum value of the candy array
        maxValue = max(candies)

        #for loop to go through the indices in the size of the candy array
        for i in range(n):
            #checking whether the value stored in the candies array at position i plus the value of extraCandies
            #is greater than the largest value stored in the candy array
            if candies[i] + extraCandies >= maxValue:
                result.append(True)
            else: 
                result.append(False)
                
        return result
    
    #Runtime: 56 ms Memory: 16.2 MB This solution is slower and takes up more memory  
        