"""
Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Step 1: Use defaultdict(list) to automatically create an empty list for new keys
        # Why defaultdict?
        # With a normal dict(), if we do res[key].append(s) and key doesn't exist yet,
        # we would get KeyError: we need to manually check and initialize res[key] = []
        # defaultdict(list) does this automatically: when a new key is accessed,
        # it creates res[new_key] = [] by default
        res = defaultdict(list)
        
        # Step 2: For each string in the input list
        for s in strs:
            # Create a unique key by sorting the characters
            # All anagrams will produce the same sorted key
            key = ''.join(sorted(s))
            
            # Append the original string to the list for this key
            # If key is new, defaultdict automatically creates an empty list first
            res[key].append(s)
        
        # Step 3: Return all the grouped anagrams
        return list(res.values())