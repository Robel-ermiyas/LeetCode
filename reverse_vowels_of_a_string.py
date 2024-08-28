# The time and space complexity are O(n), where n is the length of the string.
class Solution:
    def reverseVowels(self, s: str) -> str:
        sl = list(s) 
        vowels = "aeiouAEIOU" 
        # two pointers technique
        i = 0  #left
        n = len(sl) 
        j = n-1 #right
        while i < j:
            if sl[i] not in vowels:
                i+=1
            elif sl[j] not in vowels:
                j-=1
            else:
                sl[i], sl[j] = sl[j], sl[i]
                i+=1
                j-=1
        return ''.join(sl)
