<!--
Problem 7: Request Routing in a Web Server with a Trie

Provide an explanation for your answer, clearly organizing your thoughts into 
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->
# Request Routing in a Web Server with a Trie - Algorithm Explanation

## Problem Analysis and Approach

The key insight for solving this problem efficiently lies in recognizing that URL paths have a hierarchical structure that naturally maps to a tree-like data structure. For example, in a path like "/home/about/team", we have:
- Root level: "/"
- First level: "home"
- Second level: "about" 
- Third level: "team"

This hierarchical organization makes a trie (prefix tree) an ideal choice for storing and retrieving routes, as it allows us to:
1. Share common prefixes between different routes
2. Perform efficient prefix-based lookups
3. Handle variable-length paths naturally

## Algorithm Design Decisions

### Why Use a Trie?
1. Natural representation of hierarchical path structure
2. Efficient prefix matching capabilities
3. Space-efficient storage of routes with common prefixes
4. Fast lookup times regardless of total number of routes

### Key Algorithmic Innovations

1. **Path Normalization**: The router handles various edge cases in URLs:
   - Removing trailing slashes to treat "/about/" and "/about" as identical
   - Handling empty paths and root path "/" specially
   - Splitting paths into segments while preserving their order

2. **Three-Layer Architecture**: The solution uses a clean separation of concerns:
   - RouteTrieNode: Basic node structure for storing path segments
   - RouteTrie: Core trie operations and path traversal
   - Router: High-level interface with path normalization and handler management

3. **Handler Management**: The design includes three types of handlers:
   - Root handler: For the "/" path
   - Not found handler: For undefined routes
   - Route-specific handlers: For defined paths

## Complexity Analysis

### Time Complexity
1. **Insertion (add_handler)**: O(L)
   - L is the length of the path (number of segments)
   - Each segment requires one node creation/traversal
   - Path splitting and normalization are O(L)

2. **Lookup**: O(L)
   - Worst case requires traversing all segments of the path
   - Path normalization is linear in path length
   - No backtracking required during lookup

### Space Complexity
1. **Storage**: O(N * L)
   - N is the number of routes
   - L is the average path length
   - Common prefixes reduce actual space usage
   - Each node stores a handler and children dictionary

2. **Runtime**: O(1)
   - Lookup operations use constant extra space
   - No recursion in the final implementation
   - Path splitting creates temporary arrays of size L
