
## Reasoning Behind Decisions:
The implementation utilizes OrderedDict to realize the LRU cache functionality. This choice was made based on several key considerations:

### Data Structure Selection
The choice of OrderedDict perfectly aligns with the LRU cache requirements as it maintains insertion order. This enables efficient identification and removal of the least recently used items.

### Cache Operation Design

* The get method updates items to "most recently used" status by re*inserting them after access
* The set method clearly separates capacity management and update operations, properly handling both existing key updates and new key insertions

## Time Efficiency:
The time complexity for key operations are as follows:
* get operation: O(1)
* set operation: O(1)

Space Efficiency:
## Space Efficiency:
The space efficiency has the following characteristics:
Base storage: O(n)
* Stores up to n key/value pairs using OrderedDict
* n is the cache capacity
* Each entry holds a key/value pair, so
