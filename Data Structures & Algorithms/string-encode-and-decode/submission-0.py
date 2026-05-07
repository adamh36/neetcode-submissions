class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s  # add length + # + word to result
        
        return result 

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0  # tracks current position in string
    
        while i < len(s):  # keep going until we process the whole string
            j = i  # j starts at same position as i
        
            while s[j] != '#':  # move j forward until we hit the delimiter
                j += 1
        
            length = int(s[i:j])  # everything between i and j is the length number
            word = s[j+1: j+1+length]  # skip the # and read exactly length characters
            result.append(word)  # add the decoded word to our list
            i = j + 1 + length  # move i past the # and the word, ready for next
    
        return result  # return all decoded words
