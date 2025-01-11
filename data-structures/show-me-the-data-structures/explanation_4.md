
## Reasoning Behind Decisions:
The Group class uses a tree-like structure where each group can contain both users and subgroups, enabling flexible hierarchical organization. This design choice allows for natural representation of organizational structures, file systems, or any nested grouping system.
The is_user_in_group function employs an iterative depth-first search (DFS) using a stack rather than recursion. This decision provides several advantages:

* Stack-based iteration prevents potential stack overflow issues that could occur with deep recursive calls, especially in large group hierarchies.
* The implementation maintains better control over the search process and memory usage compared to recursion.
* The iterative approach makes the code more maintainable and easier to debug since the state of the search is explicitly visible in the stack.
## Time Efficiency:
* Worst-case time complexity: O(V + E)where V is the total number of groups and E is the total number of parent-child relationships between groups
* For each group, checking user membership is O(n) where n is the number of users in that group
## Space Efficiency:
The space complexity can be broken down into two parts:<br>

Group Class Storage:<br>
* Each Group instance stores:
 * name: O(1) - Single string reference
 * groups: O(n) where n is number of direct subgroups
 * users: O(m) where m is number of direct users
* Total space per group: O(1 + n + m)

* is_user_in_group() Function:
 * Stack space: O(V) where V is the total number of groups
 * No additional data structures are needed beyond the stack
 * The stack size is bounded by the maximum number of groups in the hierarchy

