<!--
Problem 2: Search in a Rotated Sorted Array

Provide an explanation for your answer, clearly organizing your thoughts into 
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

# Search in a Rotated Sorted Array - Algorithm Explanation

## Problem Analysis and Approach

The key insight for solving this problem efficiently lies in recognizing that despite the rotation, the array maintains partial sorting properties that we can leverage. After rotation, the array effectively consists of two sorted subarrays. For example, in [4,5,6,7,0,1,2], we have:
- Left subarray: [4,5,6,7] (sorted)
- Right subarray: [0,1,2] (sorted)
- Pivot point: Between 7 and 0

This structure allows us to adapt the binary search algorithm rather than resorting to a linear search. The challenge is determining which subarray contains our target number.

## Algorithm Design Decisions

### Why Binary Search?
1. The problem explicitly requires O(log n) runtime complexity
2. The partially sorted nature of the array enables us to make decisions about which half to search
3. Binary search is optimal for searching in sorted arrays, and we can modify it to handle the rotation

### Key Algorithmic Innovations

1. **Subarray Identification**: At each step, we can determine if the left or right half is sorted by comparing the leftmost element with the middle element
   - If left ≤ middle: Left half is sorted
   - Otherwise: Right half is sorted

2. **Search Space Reduction**: Once we know which half is sorted, we can determine if our target lies within that sorted range using simple comparisons:
   - For sorted left half: check if target ∈ [left, middle)
   - For sorted right half: check if target ∈ (middle, right]

3. **Recursive Approach**: The problem naturally lends itself to recursion because:
   - Each subproblem is a smaller instance of the same problem
   - The base cases are clearly defined (target found or invalid range)
   - The problem space is reduced by half in each recursive call

## Complexity Analysis

### Time Complexity: O(log n)
- The algorithm divides the search space in half at each step
- Each operation within the recursive call takes constant time O(1)
- The recurrence relation is T(n) = T(n/2) + O(1)
- This solves to O(log n) using the Master Theorem

### Space Complexity: O(log n)
- The recursion stack can go up to log n levels deep
- Each recursive call uses constant extra space
- If implemented iteratively, space complexity could be reduced to O(1)

