
## Union Function

### Reasoning Behind Decisions:

### Time Efficiency:
Time complexity is O(n + m) where n and m are the lengths of the input lists:
* Traversing first list: O(n)
* Traversing second list: O(m)
* Adding to set operations: O(1) on average
* Creating new list with elements: O(n + m)

### Space Efficiency:
Space complexity is O(n + m):
 * Storage for unique elements in set: O(n + m)
 * New linked list creation: O(n + m)
 * Temporary variables: O(1)

## Intersection Function

### Reasoning Behind Decisions:
Chosen to create two sets and use the intersection() method:

* Python's set.intersection() is highly optimized
* Code is readable with clear intentions
* Handles edge cases (like empty lists) naturally
* Makes the implementation straightforward

### Time Efficiency:
Time complexity is O(n + m):

* Creating set from first list: O(n)
* Creating set from second list: O(m)
* set.intersection() operation: O(min(n,m))
* Creating result list: O(min(n,m))

### Space Efficiency:
Space complexity is O(n + m):
* Two set structures: O(n) + O(m)
* Resulting linked list: O(min(n,m))
* Temporary variables: O(1)
