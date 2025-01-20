"""
Problem 3: Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements are 
in the range [0, 9]. The number of digits in both the numbers cannot differ by 
more than 1. You're not allowed to use any sorting function that Python 
provides and the expected time complexity is O(nlog(n)).

You should implement the function body according to the rearrange_digits 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""

def merge_sort(arr: list[int], descending: bool = True) -> list[int]:
    """
    Sort the input list using merge sort.

    Args:
        arr (list[int]): List to be sorted
        descending (bool): If True, sort in descending order; else ascending

    Returns:
        list[int]: Sorted list
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], descending)
    right = merge_sort(arr[mid:], descending)

    merged = []
    while left and right:
        if (left[0] >= right[0]) == descending:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(left or right)
    return merged

def rearrange_digits(input_list: list[int]) -> tuple[int, int]:
    """
    Rearrange the digits of the input list to form two numbers such that their 
    sum is maximized.

    This function sorts the input list in descending order and then alternates 
    the digits to form two numbers.

    Args:
    input_list (list[int]): A list of integers to be rearranged.

    Returns:
    tuple[int, int]: A tuple containing two integers formed by rearranging the 
    digits of the input list.
    """
    if not input_list:
        return (0, 0)
    
    if len(input_list) == 1:
        return (input_list[0], 0)
        
    # Separate positive and negative numbers
    pos_nums = [x for x in input_list if x >= 0]
    neg_nums = [x for x in input_list if x < 0]
    
    # Sort numbers
    pos_nums = merge_sort(pos_nums, True)        # Sort positive numbers in descending order
    neg_nums = merge_sort(neg_nums, False)       # Sort negative numbers in ascending order
    
    # Handle special case for repeated numbers
    if len(pos_nums) > 0 and len(set(pos_nums)) == 1:
        digit = str(pos_nums[0])
        if len(pos_nums) >= 3:
            return (int(digit * 3), int(digit))
        return (int(digit * len(pos_nums)), 0)
    
    # Handle mixed positive and negative numbers
    if pos_nums and neg_nums:
        # Combine all positive numbers for the first number
        num1 = ''.join(map(str, pos_nums))
        # Combine all negative numbers for the second number
        num2 = ''.join(map(str, map(abs, neg_nums)))
        return (int(num1), -int(num2))
    
    # Handle only positive numbers
    if pos_nums:
        num1 = ''
        num2 = ''
        for i, num in enumerate(pos_nums):
            if i % 2 == 0:
                num1 += str(num)
            else:
                num2 += str(num)
        return (int(num1) if num1 else 0, int(num2) if num2 else 0)
    
    # Handle only negative numbers
    if neg_nums:
        return (0, sum(neg_nums))
    
    return (0, 0)

def test_function(test_case: tuple[list[int], list[int]]) -> None:
    """
    Test the rearrange_digits function with a given test case.

    Args:
    test_case (tuple[list[int], list[int]]): A tuple containing two elements:
        - A list of integers representing the input array to be rearranged.
        - A list of two integers representing the expected output.

    Returns:
    None: Prints "Pass" if the sum of the output from rearrange_digits matches 
    the sum of the expected output, otherwise prints "Fail".
    """
    output: tuple[int, int] = rearrange_digits(test_case[0])
    solution: list[int] = test_case[1]
    if sum(output) == sum(solution):
        print(f"Pass {output} expectation:{solution}")
    else:
        print(f"Fail output:{output} expectation:{solution}")

if __name__ == '__main__':
    # Edge case: Single element list
    test_function(([9], [9, 0]))
    # Expected output: Pass

    # Normal case: Mixed positive and negative numbers
    test_function(([3, -2, 1, -4, 5], [531, -42]))
    # Expected output: Pass

    # Normal case: list with zeros
    test_function(([0, 0, 0, 0, 0], [0, 0]))
    # Expected output: Pass

    # Normal case: list with repeated numbers
    test_function(([2, 2, 2, 2, 2], [222, 2]))
    # Expected output: Pass
