class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Converting an int to a string 
        x_str = str(x)

        #reversing the string using the [::-1] slicing technique
        reverse = x_str[::-1]

        #Checking if the number stored in x is the same from right to left
        #and from left to right
        if(reverse == x_str):
            return("true")
        else:
            print("false")  