class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagram_map = defaultdict(list)
        
        for w in strs: 
            key = "".join(sorted(w))
            anagram_map[key].append(w)
        return list(anagram_map.values())
