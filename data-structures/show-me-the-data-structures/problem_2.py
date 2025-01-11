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
            None: Results are accumulated in the outer scope's matching_files list.
        """
        if os.path.isdir(current_path):
            try:
                for item in os.listdir(current_path):
                    recursive_search(os.path.join(current_path, item))
            except PermissionError:
                pass
        elif os.path.isfile(current_path) and current_path.endswith(suffix):
            matching_files.append(current_path)

    recursive_search(path)
    return matching_files


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir")
    print(result)
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

    # Test Case 2: Finding header files (.h)
    print("\nTest Case 2: Finding header files")
    result = find_files(".h", "./testdir")
    print(result)
    # Expected output: ['./testdir/subdir1/a.h', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h']

    # Test Case 3: Finding non-existent file type
    print("\nTest Case 3: Finding non-existent file type")
    result = find_files(".py", "./testdir")
    print(result)
    # Expected output: []
