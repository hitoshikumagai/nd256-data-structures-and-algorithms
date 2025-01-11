"""
Problem 1: Square Root of an Integer

In this problem, you need to find the square root of a given integer without using 
any Python libraries. You should return the floor value of the square root.

Below is a function signature that serves as a starting point for your implementation. 
Your task is to complete the body of the function. Additionally, some test cases are 
provided to help you verify the correctness of your implementation. If necessary, add 
test cases to verify that your algorithm is working properly.

The expected time complexity is O(log(n)).
"""

def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
    number(int): Number to find the floored square root

    Returns:
    int: Floored square root
    """

    if number < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    
    if number == 0 or number == 1:
        return number

    # Binary search initialization
    start, end = 0, number
    result = 0

    for _ in range(number + 1):  # Simulates the iterative process
        mid = (start + end) // 2
        
        # Check if mid is the square root
        if mid * mid == number:
            return mid
        
        # If mid squared is less than the number, discard the left half
        if mid * mid < number:
            start = mid + 1
            result = mid  # Store the floor of the square root
        else:
            end = mid - 1  # Discard the right half
        
        # Break the loop when start surpasses end
        if start > end:
            break

    return result

if __name__ == "__main__":
    # Test cases
    print("Pass" if 3 == sqrt(9) else "Fail")   # Expected Output: Pass
    print("Pass" if 0 == sqrt(0) else "Fail")   # Expected Output: Pass
    print("Pass" if 4 == sqrt(16) else "Fail")  # Expected Output: Pass
    print("Pass" if 1 == sqrt(1) else "Fail")   # Expected Output: Pass
    print("Pass" if 5 == sqrt(27) else "Fail")  # Expected Output: Pass
