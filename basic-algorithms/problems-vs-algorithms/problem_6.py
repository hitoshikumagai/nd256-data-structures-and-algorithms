"""
Problem 6: Unsorted Integer Array

In this problem, we will look for smallest and largest integer from a list of 
unsorted integers. The code should run in O(n) time. Do not use Python's 
inbuilt functions to find min and max.

You should implement the function body according to the get_min_max function 
signature. Use the test cases provided below to verify that your algorithm is 
correct. If necessary, add additional test cases to verify that your algorithm 
works correctly.
"""

from typing import Optional

def get_min_max(ints: list[int]) -> Optional[tuple[int, int]]:
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
    ints (list[int]): list of integers containing one or more integers

    Returns:
    Optional[tuple[int, int]]: A tuple containing the minimum and maximum 
    integer, or None if the list is empty
    """
    if not ints:
        return None
    
    # Helper function to recursively find the min and max
    def helper(ints: list[int], low: int, high: int) -> tuple[int, int]:
        # Base case: when the list has only one element
        if low == high:
            return ints[low], ints[low]
        
        # Divide the list into two halves
        mid = (low + high) // 2
        
        # Recursively find the min and max for both halves
        left_min, left_max = helper(ints, low, mid)
        right_min, right_max = helper(ints, mid + 1, high)
        
        # Manually compare and return the min and max
        min_val = left_min if left_min < right_min else right_min
        max_val = left_max if left_max > right_max else right_max
        
        return min_val, max_val
    
    return helper(ints, 0, len(ints) - 1)


if __name__ == '__main__':
    # Edge case: Empty input list
    print(get_min_max([]))
    # Expected output: None

    # Normal case: list with negative and positive numbers
    print(get_min_max([-10, 0, 10, -20, 20]))
    # Expected output: (-20, 20)

    # Normal case: list with large range of numbers
    print(get_min_max([1000, -1000, 500, -500, 0]))
    # Expected output: (-1000, 1000)

    # Normal case: list with already sorted numbers
    print(get_min_max([1, 2, 3, 4, 5]))
    # Expected output: (1, 5)
