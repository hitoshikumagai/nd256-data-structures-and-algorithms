<!--
Problem 3: Rearrange Array Digits

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->
# Rearrange Array Digits - Algorithm Explanation

## Problem Analysis and Approach

The core challenge in this problem is to construct two numbers from the given digits such that their sum is maximized while maintaining certain constraints:
- All array elements are in range [0, 9]
- The difference in number of digits between the two numbers cannot exceed 1
- Must achieve O(nlog(n)) time complexity without using Python's built-in sorting

The key insight is that to maximize the sum, we want to:
1. Place larger digits in more significant positions (leftmost)
2. Distribute digits alternately between the two numbers to keep their lengths similar
3. Handle special cases like negative numbers and repeated digits carefully

## Algorithm Design Decisions

### Why Merge Sort?
1. The problem requires O(nlog(n)) time complexity
2. We can't use Python's built-in sorting functions
3. Merge sort is stable and performs consistently across different input distributions
4. It adapts well to sorting in both ascending and descending orders

### Key Algorithmic Innovations

1. **Special Case Handling**: The solution innovates by considering several edge cases:
   - Single element arrays
   - Arrays with all repeated numbers
   - Mixed positive and negative numbers
   - Arrays containing only zeros

2. **Number Construction Strategy**: 
   - For normal cases: Alternate digits between numbers (e.g., [9,8,7,6] → 97 and 86)
   - For repeated numbers: Group more digits in the first number (e.g., [2,2,2,2,2] → 222 and 2)
   - For mixed signs: Combine positive numbers for first number, negative for second

3. **Flexible Sorting Direction**:
   - Positive numbers sorted in descending order to maximize leading digits
   - Negative numbers sorted in ascending order to minimize their absolute value

## Complexity Analysis

### Time Complexity: O(nlog(n))
- Merge sort dominates the time complexity
- The merge sort recurrence relation: T(n) = 2T(n/2) + O(n)
- All other operations (string joining, type conversion) are O(n)
- Overall complexity remains O(nlog(n)) as required

### Space Complexity: O(n)
- Merge sort requires O(n) auxiliary space for merging
- Additional O(n) space for storing separated positive/negative numbers
- String conversion and joining operations use O(n) space
- Overall space complexity is O(n)
