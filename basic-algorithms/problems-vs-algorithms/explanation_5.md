<!--
Problem 5: Autocomplete with Tries

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

# Autocomplete with Tries - Algorithm Explanation

## Problem Analysis and Approach

The autocomplete feature requires efficient prefix-based string searching, making a Trie (prefix tree) the ideal data structure. The key aspects that make Tries particularly suitable for this problem are:
- Each node represents a character in a sequence
- Common prefixes share the same path from the root
- Words are stored as paths from root to leaf
- Each node can mark whether it represents the end of a complete word

For example, storing ["fun", "function", "factory"] creates a tree where:
- The 'f' node has two children ('u', 'a')
- The path f->u->n represents "fun"
- The path f->u->n->c->t->i->o->n represents "function"
- The path f->a->c->t->o->r->y represents "factory"

## Algorithm Design Decisions

### Why Use a Trie?
1. Efficient prefix matching: O(m) where m is prefix length
2. Space-efficient for words sharing common prefixes
3. Natural support for autocomplete functionality
4. Faster than alternative approaches like binary search on sorted arrays O(log n) or hash tables

### Key Design Components

1. **TrieNode Structure**:
   - Dictionary for children (character → node mapping)
   - Boolean flag for word completion
   - Dictionary chosen over array for O(1) child access

2. **Insertion Method**:
   - Iterative approach for adding characters
   - Creates new nodes only when necessary
   - Marks word completion at final node

3. **Suffix Collection**:
   - Recursive depth-first search
   - Builds suffixes incrementally
   - Returns only complete words
   - Uses string concatenation for path tracking
   
## Complexity Analysis

### Time Complexity
1. **Insertion**: O(m) where m is word length
   - Each character requires constant-time operations
   - Dictionary lookups are O(1)

2. **Finding Prefix**: O(p) where p is prefix length
   - Similar to insertion, traverses one node per character
   - Early termination if prefix not found

3. **Collecting Suffixes**: O(n) where n is number of nodes in subtree
   - Must visit all nodes below prefix
   - String concatenation at each node is O(1) amortized
   - Total complexity depends on number of possible completions

### Space Complexity
1. **Trie Structure**: O(ALPHABET_SIZE * N) where N is total characters
   - Each node stores ALPHABET_SIZE potential children
   - Actual space often less due to prefix sharing
   - Worst case when no words share prefixes

2. **Suffix Collection**: O(m * k) where
   - m is max word length
   - k is number of completions
   - Space needed to store all possible suffix strings
