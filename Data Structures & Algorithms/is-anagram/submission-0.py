class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # brute force
        # string_s = []
        # string_t = []
        # for ch in s:
        #     string_s.append(ch)
        # for ch in t:
        #     string_t.append(ch)
        # if sorted(string_s) == sorted(string_t):
        #     return True
        # return False

        for ch in s:
            if s.count(ch) != t.count(ch):
                return False
        return True
        
