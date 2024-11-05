from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = defaultdict(list)  # Dictionary to store grouped anagrams

        for word in strs:
            sorted_word = ''.join(sorted(word))  # Sort each word to get the key
            anagram_dict[sorted_word].append(word)  # Append word to the corresponding anagram group

        return list(anagram_dict.values())  # Return the grouped anagrams as a list