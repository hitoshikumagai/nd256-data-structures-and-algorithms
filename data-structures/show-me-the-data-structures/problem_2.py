import os

def find_files(suffix: str, path: str) -> list[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    if not os.path.exists(path):
        return []

    matching_files = []

    def recursive_search(current_path):
        """
        Recursively search through directories to find files with the specified suffix.

        This helper function performs the actual recursive traversal of the directory
        tree, adding matching files to the outer scope's matching_files list. It handles
        both files and directories, skipping directories that cannot be accessed due
        to permissions.

        Args:
            current_path (str): The path to the current file or directory being processed.
                              This path is joined with the base path during recursion.

        Returns:
            matching_files (list): Results are accumulated in the outer scope's matching_files list.
        """
    # Input validation
    if suffix is None or not isinstance(suffix, str):
        raise TypeError("Suffix must be a string")
    if path is None or not isinstance(path, str):
        raise TypeError("Path must be a string")

    if not os.path.exists(path):
        return []

    matching_files = []
    
    # os.walk yields a 3-tuple: (dirpath, dirnames, filenames)
    for root, _, files in os.walk(path):
        try:
            # Add all files that end with the suffix in current directory
            matching_files.extend(
                os.path.join(root, file)
                for file in files
                if file.endswith(suffix)
            )
        except PermissionError:
            continue

    return matching_files


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir")
    print(result)
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

    # Test Case 2:Finding non-existent file type
    print("\nTest Case 2: Finding non-existent file type")
    result = find_files(".py", "./testdir")
    print(result)
    # Expected: []

    # Test Case 3:Edge case test cases
    print("\nTest Case 3: Invalid input path")
    result = find_files(".txt", "./nonexistent_directory")
    print(result)
    # Expected: []

    # Test Case 4: None as suffix
    print("\nTest Case 4: None as suffix")
    try:
        result = find_files(None, "./testdir")
        print(result)
    except TypeError:
        print("Handled None suffix correctly")
    # Expected: TypeError or empty list
