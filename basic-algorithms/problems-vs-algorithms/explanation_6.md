<!--
Problem 6: Unsorted Integer Array

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->
# Finding Minimum and Maximum in Unsorted Array - Algorithm Explanation

## Problem Analysis and Approach

The challenge of finding both the minimum and maximum values in an unsorted array presents an interesting optimization opportunity. While a naive approach might traverse the array twice (once for min, once for max), we can achieve better efficiency by leveraging the following insights:

1. Every comparison between two elements can give us information about both the minimum and maximum
2. The problem can be broken down into smaller subproblems that maintain the same structure
3. We can use divide-and-conquer to process multiple elements in parallel conceptually

## Algorithm Design Decisions

### Why Divide-and-Conquer?
1. Reduces the total number of comparisons needed compared to linear scanning
2. Naturally handles the requirement of not using Python's built-in min/max functions
3. Makes the code more maintainable and easier to reason about
4. Provides opportunities for parallel processing in real-world scenarios

### Key Algorithmic Innovations

1. **Recursive Subdivision**: The array is continuously divided into halves until reaching single elements
   - Base case: Single element is both min and max of its subarray
   - Each recursive call handles a distinct portion of the array
   - Results are combined using simple comparison operations

2. **Efficient Comparison Strategy**: When combining results from subarrays:
   - Only two comparisons needed per merge operation (one for min, one for max)
   - No element is compared more than log n times
   - Avoids redundant comparisons by reusing information

3. **Null Safety**: The algorithm handles edge cases gracefully:
   - Empty arrays return None
   - Single-element arrays return the element as both min and max
   - No special handling needed for negative numbers or zero

## Complexity Analysis

### Time Complexity: O(n)
- The recurrence relation is T(n) = 2T(n/2) + 2
- At each level of recursion:
  * Number of subproblems: 2^k (where k is the level)
  * Size of each subproblem: n/2^k
  * Work per subproblem: O(1) (just 2 comparisons)
- Total comparisons ≈ 3n/2 - 2
- This resolves to linear time O(n)

### Space Complexity: O(log n)
- Recursive call stack depth is logarithmic in input size
- Each recursive call uses constant extra space
- No additional data structures are needed
- Could be optimized to O(1) with an iterative implementation
