class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_count=0
        for i in range(k):
            if s[i].lower() in 'aeiou':
                vowel_count+=1
        max_count=vowel_count
        for j in range(k,len(s)):
            if s[j].lower() in 'aeiou':
                vowel_count+=1
            if s[j-k].lower() in 'aeiou':
                vowel_count-=1
            max_count=max(max_count,vowel_count)
        return max_count