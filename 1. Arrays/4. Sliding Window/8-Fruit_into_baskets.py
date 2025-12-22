"""
Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 
Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2]. 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
"""
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Find the maximum number of fruits you can collect.
        You have two baskets, each can hold only one type of fruit.
        Return the length of the longest subarray with at most 2 distinct fruit types.
        """
        n = len(fruits)
        
        # Step 1: Initialize sliding window variables
        l = 0                    # Left pointer of the current window
        res = -1                 # Maximum length of valid subarray found
        freq = {}                # Frequency map: tracks count of each fruit type in current window
        
        # Step 2: Expand the window using right pointer
        for r in range(n):
            # Add current fruit to the window
            freq[fruits[r]] = freq.get(fruits[r], 0) + 1
            
            # Step 3: Shrink window from left if more than 2 distinct fruit types
            while len(freq) > 2:
                # Remove the leftmost fruit from the window
                freq[fruits[l]] -= 1
                
                # If count reaches 0, remove the fruit type from the map
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                
                # Move left pointer right
                l += 1
            
            # Step 4: Update maximum length
            # Current window [l, r] has at most 2 distinct fruit types
            res = max(res, r - l + 1)
        
        # Step 5: Return the longest valid subarray length
        return res