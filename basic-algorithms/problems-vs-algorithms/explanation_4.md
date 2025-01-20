<!--
Problem 4: Dutch National Flag Problem

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

# Dutch National Flag Problem - Algorithm Explanation

## Problem Analysis and Approach

The Dutch National Flag problem presents an interesting sorting challenge where we need to arrange elements (0s, 1s, and 2s) in a single traversal. The key insight is that we're not dealing with a general sorting problem, but rather a specialized partitioning problem with exactly three distinct values. This constraint allows us to develop a more efficient solution than traditional sorting algorithms.

## Algorithm Design Decisions

### Why Three-Way Partitioning?
1. The problem requires sorting in a single traversal
2. We have exactly three distinct values (0, 1, 2)
3. The final arrangement must maintain relative order (all 0s, followed by all 1s, followed by all 2s)

### Key Algorithmic Innovations

1. **Pointer-Based Approach**: Instead of counting elements (which would require multiple passes), we use three pointers:
   - low: marks the boundary of 0s
   - mid: current element being examined
   - high: marks the boundary of 2s

2. **In-Place Swapping**: The algorithm performs in-place swapping to achieve the desired ordering:
   - When we find a 0, swap it with the low pointer position
   - When we find a 2, swap it with the high pointer position
   - When we find a 1, just move to the next element

3. **Single-Pass Solution**: The algorithm maintains three invariants:
   - All elements before low are 0s
   - All elements between low and mid are 1s
   - All elements after high are 2s
   - Elements between mid and high are yet to be examined

## Why Not Alternative Approaches?

1. **Counting Sort**: While it would work in O(n), it requires two passes through the array
2. **Quick Sort**: Though efficient for general sorting, it's overkill and might require multiple passes
3. **Recursive Approach**: While cleaner to implement, it wouldn't satisfy the single-traversal requirement

## Complexity Analysis

### Time Complexity: O(n)
- Each element is examined exactly once
- Each swap operation takes O(1) time
- The mid pointer never needs to backtrack
- Total number of swaps is bounded by n

### Space Complexity: O(1)
- Only three pointers are used regardless of input size
- All operations are performed in-place
- No additional data structures are required
- No recursive call stack is needed
