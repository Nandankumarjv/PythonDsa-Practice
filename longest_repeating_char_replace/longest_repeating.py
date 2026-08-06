from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        count=defaultdict(int)
        max_frequency=0
        max_length=0
        for r in range(len(s)):
            count[s[r]]+=1
            max_frequency=max(max_frequency,count[s[r]])
            while (r-l+1-max_frequency)>k:
                count[s[l]]-=1
                l+=1
            max_length=max(max_length,r-l+1)
        return max_length