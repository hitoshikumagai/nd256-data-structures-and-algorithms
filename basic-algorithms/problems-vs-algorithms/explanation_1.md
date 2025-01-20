<!--
Problem 1: Square Root of an Integer

Provide an explanation for your answer, clearly organizing your thoughts into concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a detailed description of the code. For instance, why did you choose a particular data structure? Additionally, discuss the efficiency of your solution in terms of time and space complexity. If necessary, you can support your explanation with code snippets or mathematical formulas. For guidance on how to write formulas in markdown, 
refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

# Square Root of an Integer - Algorithm Explanation

## Problem Analysis and Approach

The core challenge in this problem is to efficiently compute the floor value of a square root without using built-in library functions. The key insight is recognizing that the square root of a number N must lie in the range [0, N], and this range has a monotonic property: for any number x in this range, x² increases monotonically. This property makes binary search an ideal choice for our solution.

## Algorithm Design Decisions

### Why Binary Search?
1. The monotonic nature of squares means we can efficiently narrow down the search space
2. The problem requires O(log n) time complexity, which binary search naturally provides
3. The continuous range of possible values maps perfectly to binary search's divide-and-conquer approach

### Key Algorithmic Innovations

1. **Range Initialization**: 
   - Start with the full possible range [0, N]
   - This ensures we don't miss any potential solutions
   - Handles all valid input cases, including edge cases like 0 and 1

2. **Search Space Management**:
   - At each step, we calculate mid = (start + end) // 2
   - Compare mid² with the target number
   - Keep track of the largest valid square root found so far
   - This handles both perfect squares and numbers that aren't perfect squares

3. **Floor Value Handling**:
   - When mid² < number, store mid as a potential result
   - This ensures we always have the floor value of the square root
   - Critical for non-perfect squares like √27 = 5.196... where we need to return 5

## Edge Cases and Error Handling

1. **Negative Numbers**:
   - Explicitly check and raise ValueError
   - Mathematical validity: square roots of negative numbers are not real numbers

2. **Special Cases**:
   - Handle 0 and 1 separately
   - These inputs would work in the main algorithm but can be returned immediately
   - Improves efficiency for common edge cases

## Complexity Analysis

### Time Complexity: O(log n)
- Each iteration reduces the search space by half
- The search space starts at size n
- Number of iterations needed to reduce n to 1: log₂(n)
- Each iteration performs constant time operations (multiplication and comparison)

### Space Complexity: O(1)
- Only uses a fixed number of variables (start, end, mid, result)
- Space usage doesn't grow with input size
- No recursive calls or additional data structures needed

## Practical Considerations

1. **Integer Overflow Prevention**:
   - Using (start + end) // 2 for midpoint calculation
   - Alternative: start + (end - start) // 2 could be used for very large numbers

2. **Iteration Control**:
   - Loop continues until start > end
   - Guarantees termination while ensuring all possible values are checked

3. **Result Accuracy**:
   - Always returns the floor value as required
   - Verified through test cases including perfect and non-perfect squares