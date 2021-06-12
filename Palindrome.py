class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = ''.join(e.lower() for e in s if e.isalnum())
                    
        return all(s[i] == s[~i] for i in range(len(s)))
