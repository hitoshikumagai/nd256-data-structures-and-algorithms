
## Reasoning Behind Decisions:
The implementation demonstrates several key design decisions that enhance its robustness and usability:

* Use of Closure Pattern: The code employs a nested helper function recursive_search within the main find_files function. This design choice provides clean encapsulation of the recursive logic while maintaining access to the shared matching_files list through closure. This prevents the need to pass and return the list through each recursive call.
* Error Handling: The implementation includes two important error handling mechanisms:
Initial path validation using os.path.exists(path) to handle non-existent directories gracefully try-except block for handling PermissionError when accessing directories, allowing the search to continue even if some directories are inaccessible
## Time Efficiency:
The time complexity analysis reveals O(n) performance where n is the total number of files and directories in the tree:
when searching for ".c" files, four files (file2.c, file3.c, file5.c, file6.c) are found, but the algorithm needs to visit all 11 nodes to find them. This is why the overall time complexity is O(n).

## Space Efficiency:
The space complexity can be analyzed across several dimensions:

* Primary Storage:The matching_files list grows linearly with the number of matching files found, resulting in O(m) space where m is the number of matching files