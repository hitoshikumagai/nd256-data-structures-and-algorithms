
## Reasoning Behind Decisions:
* Data Structure Choices
 * HuffmanNode class implementation: Creates a binary tree structure that holds character and frequency information with references to left and right child nodes
 * Use of defaultdict: Efficient choice for character frequency counting as it automatically handles default values (0) for non-existent keys
 * heapq adoption: Used for priority queue implementation, enabling efficient access to nodes with minimum frequency

* Algorithm Design
 * Separation of encoding into two phases (frequency calculation → tree construction): Enhances code maintainability and reusability
 * Recursive approach: Uses recursion for Huffman tree traversal and code generation, keeping implementation clean
 * Type hints utilization: Improves code readability and maintainability through Python type annotations
## Time Efficiency:
Encoding Process O(n log n)
* Frequency calculation: O(n) - Single pass through input string
* Huffman tree construction: O(k log k) - where k is number of unique characters
 * log k operations for each heapq operation
 * Requires k-1 merge operations
* Code generation: O(k) - Visit each node once
* String encoding: O(n) - Convert each character to its code

Decoding Process O(n)
* Single tree traversal for each bit in encoded data
* Number of bits is proportional to original string length

## Space Efficiency:
Memory Usage for Data Structures
* Huffman tree: O(k) - where k is number of unique characters

Each node stores character, frequency, and two pointers
* Frequency table: O(k)
* Huffman code dictionary: O(k)

Temporary Memory Usage
* Priority queue: O(k) - Stores up to k nodes for unique characters
* String buffers during encode/decode: O(n)