class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_s = "".join(char.lower() for char in s if char.isalnum())

        reversed_cleaned = cleaned_s[::-1]

        if reversed_cleaned == cleaned_s:
            return True 
        else: 
            return False




 