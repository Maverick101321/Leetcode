class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        left, result, count = 0, 0, 0

        for right in range(len(s)):
            if s[right] in vowel:
                count += 1
            if right - left >= k:
                if s[left] in vowel:
                    count -= 1
                left += 1
            result = max(result, count)
        return result