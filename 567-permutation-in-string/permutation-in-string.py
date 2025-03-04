class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        from collections import Counter
        
        s1_count = Counter(s1)  # Frequency count of s1
        s2_count = Counter(s2[:len(s1)])  # First window
        
        if s1_count == s2_count:
            return True
        
        l = 0
        
        # Start sliding the window
        for r in range(len(s1), len(s2)):
            s2_count[s2[r]] += 1  # Add new character
            s2_count[s2[l]] -= 1  # Remove old character
            
            if s2_count[s2[l]] == 0:
                del s2_count[s2[l]]  # Clean zero counts
            
            l += 1
            
            if s1_count == s2_count:
                return True
        
        return False