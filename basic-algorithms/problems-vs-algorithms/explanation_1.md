<!--
Problem 1: Square Root of an Integer

Provide an explanation for your answer, clearly organizing your thoughts into concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a detailed description of the code. For instance, why did you choose a particular data structure? Additionally, discuss the efficiency of your solution in terms of time and space complexity. If necessary, you can support your explanation with code snippets or mathematical formulas. For guidance on how to write formulas in markdown, 
refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->


I chose to use a binary search approach to solve this problem because:

* Efficient Search: The problem boils down to finding the integer square root of a number, which can be done efficiently using a binary search. The idea is that by iteratively narrowing down the range of possible values, we can find the square root in logarithmic time, rather than checking every integer from 0 to number (which would be much slower).
* Division of the Problem: The binary search works by repeatedly dividing the search space in half, which is particularly useful for problems where the target value lies within a continuous range (like numbers in this case).

* Efficiency: Binary search reduces the problem space by half with each iteration, making it very efficient. This leads to a time complexity of O(log n), where n is the input number.
Simpler than brute-force: A brute-force approach that checks all numbers up to number would take O(n) time, which is much slower than the binary search approach.
* Time and Space Complexity
  * Time Complexity:
The time complexity is O(log n) because we repeatedly halve the search space. Each iteration reduces the search space by half, which is characteristic of binary search.
  * Space Complexity:
The space complexity is O(1) because we only use a constant amount of space, i.e., a few variables for storing start, end, mid, and result. The space does not grow with the size of the input.