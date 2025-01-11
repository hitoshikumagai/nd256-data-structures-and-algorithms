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

    # Test Case 2: Test capacity of 1
    print("\nTest Case 2: Testing cache with capacity 1")
    tiny_cache = LRU_Cache(1)
    tiny_cache.set(1, "one")
    assert tiny_cache.get(1) == "one"  # Returns "one"
    tiny_cache.set(2, "two")  # This should evict key 1
    assert tiny_cache.get(1) == -1     # Returns -1, 1 was evicted
    assert tiny_cache.get(2) == "two"  # Returns "two"

    # Test Case 3: Test updating existing keys and order
    print("\nTest Case 3: Testing update of existing keys and access order")
    update_cache = LRU_Cache(3)
    update_cache.set(1, "one")
    update_cache.set(2, "two")
    update_cache.set(3, "three")
    
    # Update existing key
    update_cache.set(2, "two-updated")
    assert update_cache.get(2) == "two-updated"  # Returns "two-updated"
    
    # Access key 1, making it most recently used
    update_cache.get(1)
    
    # Add new key, should evict key 3 (least recently used)
    update_cache.set(4, "four")
    assert update_cache.get(3) == -1          # Returns -1, 3 was evicted
    assert update_cache.get(1) == "one"       # Returns "one"
    assert update_cache.get(2) == "two-updated"  # Returns "two-updated"
    assert update_cache.get(4) == "four"      # Returns "four"
