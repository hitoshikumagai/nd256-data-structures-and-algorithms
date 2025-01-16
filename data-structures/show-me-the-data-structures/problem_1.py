from collections import OrderedDict
from typing import Any, Optional

class LRU_Cache:
    """
    A class to represent a Least Recently Used (LRU) cache.

    Attributes:
    -----------
    capacity : int
        The maximum number of items the cache can hold.
    cache : OrderedDict[int, Any]
        The ordered dictionary to store cache items.
    """

    def __init__(self, capacity: int) -> None:
        """
        Constructs all the necessary attributes for the LRU_Cache object.

        Parameters:
        -----------
        capacity : int
            The maximum number of items the cache can hold.
        """
        if not isinstance(capacity, int):
            raise ValueError("Capacity must be an integer")
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> Optional[Any]:
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.

        Parameters:
        -----------
        key : int
            The key to be accessed in the cache.

        Returns:
        --------
        Optional[Any]
            The value associated with the key if it exists, otherwise -1.
        """
        if key in self.cache:
            # Move the accessed item to the end to mark it as recently used
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def set(self, key: int, value: Any) -> None:
        """
        Set or insert the value if the key is not already present. When the cache reaches 
        its capacity, it should invalidate the least recently used item before inserting 
        a new item.

        Parameters:
        -----------
        key : int
            The key to be inserted or updated in the cache.
        value : Any
            The value to be associated with the key.
        """
        if key in self.cache:
            # Remove the old value for the key
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Pop the least recently used item (first item in OrderedDict)
            self.cache.popitem(last=False)

        # Insert the new key-value pair
        self.cache[key] = value

if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    assert our_cache.get(1) == 1   # Returns 1
    assert our_cache.get(2) == 2   # Returns 2
    assert our_cache.get(9) == -1  # Returns -1 because 9 is not in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)  # This should evict key 3
    assert our_cache.get(3) == -1  # Returns -1, 3 was evicted

    # Test Case 2: Invalid capacity inputs
    print("\n2. Testing invalid capacity inputs:")
    invalid_capacities = [0, -5, 3.5, None, "5"]
    for cap in invalid_capacities:
        try:
            invalid_cache = LRU_Cache(cap)
            print(f"Should have raised ValueError for capacity {cap}")
            assert False
        except ValueError as e:
            if isinstance(cap, (int, float)) and cap <= 0:
                assert str(e) == "Capacity must be a positive integer"
            elif not isinstance(cap, int):
                assert str(e) == "Capacity must be an integer"
            print(f"✓ Correctly handled invalid capacity: {cap}")
    # Test Case 2: Repeated access to same value
    print("\n2. Testing repeated access to same value:")
    repeat_cache = LRU_Cache(2)
    repeat_cache.set(1, "test")
    for _ in range(5):  # Access same value multiple times
        assert repeat_cache.get(1) == "test"
    print("✓ Successfully handled repeated access")

    # Test Case 3: Very large capacity
    print("\n3. Testing large capacity:")
    large_cap = 1000000
    large_cache = LRU_Cache(large_cap)
    for i in range(100):  # Test with a smaller subset
        large_cache.set(i, f"value_{i}")
    assert large_cache.get(50) == "value_50"
    print("✓ Successfully handled large capacity")
