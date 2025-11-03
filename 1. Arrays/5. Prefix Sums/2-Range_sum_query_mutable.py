"""
Range Sum Query - Mutable

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
"""
class NumArray(object):
    def __init__(self, nums):
        """
        Initialize the NumArray with range sum query + point update capability
        Using Fenwick Tree (Binary Indexed Tree) for O(log n) operations
        """
        # Step 1: Store length of input array
        self.n = len(nums)
        
        # Step 2: Initialize Fenwick Tree (BIT) with size n+1 (1-based indexing)
        # bit[i] stores partial sum of a range of elements
        self.bit = [0] * (self.n + 1)
        
        # Step 3: Keep original array for reference during updates
        # Needed to compute diff = new_val - old_val
        self.arr = nums[:]
        
        # Step 4: Build the Fenwick Tree by updating each element
        # We use 1-based indexing for BIT, so enumerate(nums, 1)
        for i, v in enumerate(nums, 1):  # i from 1 to n
            j = i
            # Update BIT: add value v at index i
            while j <= self.n:
                self.bit[j] += v           # Add v to responsible node
                j += j & -j                # Move to next responsible index
                # j & -j gives the least significant bit (LSB)
    
    def update(self, i, v):
        """
        Update element at index i to new value v
        Time: O(log n)
        """
        # Step 1: Compute difference between new and old value
        diff = v - self.arr[i]
        
        # Step 2: Update the original array
        self.arr[i] = v
        
        # Step 3: Update Fenwick Tree with the difference
        # Convert 0-based index to 1-based for BIT
        i += 1
        while i <= self.n:
            self.bit[i] += diff            # Add diff to all responsible ranges
            i += i & -i                    # Move to next node
    
    def sumRange(self, l, r):
        """
        Return sum of elements from index l to r (inclusive)
        Time: O(log n)
        """
        # Helper function: sum from index 0 to x (inclusive)
        def prefix_sum(x):
            total = 0
            # Convert to 1-based index
            x += 1
            while x > 0:
                total += self.bit[x]       # Add partial sum
                x -= x & -x                # Move to parent
            return total
        
        # Step 1: sum(l to r) = prefix_sum(r) - prefix_sum(l-1)
        return prefix_sum(r) - prefix_sum(l - 1) if l > 0 else prefix_sum(r)