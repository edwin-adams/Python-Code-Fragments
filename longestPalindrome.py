#A function that returns the longest palindromatic substring of a string of text.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        pLen = 0
        
        for i in range(len(s)):
            #odd palindromes
            leftPtr, rightPtr = i, i   #pointers to outer characters of i
            while leftPtr >= 0 and rightPtr < len(s) and s[leftPtr] == s[rightPtr]: # palindrome check 
                if(rightPtr - leftPtr + 1) > pLen:
                    palindrome = s[leftPtr : rightPtr + 1]
                    pLen = rightPtr - leftPtr + 1
                    
                leftPtr -=1
                rightPtr +=1
                
            #even palindromes 'abba'
            leftPtr, rightPtr = i, i+1
            while leftPtr >= 0 and rightPtr < len(s) and s[leftPtr] == s[rightPtr]:  #palindrome check
                if(rightPtr - leftPtr + 1) > pLen:
                    palindrome = s[leftPtr : rightPtr + 1]
                    pLen = rightPtr - leftPtr + 1
                
                leftPtr -=1
                rightPtr +=1
            
                
                
                
                
        return palindrome  
            
