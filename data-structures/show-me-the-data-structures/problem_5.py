import hashlib
import datetime
from typing import Optional

class Block:
    """
    A class to represent a block in the blockchain using LinkedList structure.
    """
    def __init__(self, timestamp: datetime.datetime, data: str, previous_hash: str) -> None:
        self.timestamp: datetime.datetime = timestamp
        self.data: str = data
        self.previous_hash: str = previous_hash
        self.hash: str = self.calc_hash()
        self.next: Optional[Block] = None  # LinkedList next pointer

    def calc_hash(self) -> str:
        """Calculate the hash of the block using SHA-256."""
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self) -> str:
        """Return a string representation of the block."""
        return (f"Block(\n"
                f"  Timestamp: {self.timestamp},\n"
                f"  Data: {self.data},\n"
                f"  Previous Hash: {self.previous_hash},\n"
                f"  Hash: {self.hash}\n"
                f")\n")

class Blockchain:
    """
    A class to represent a blockchain using LinkedList structure.
    """
    def __init__(self) -> None:
        """Initialize an empty blockchain."""
        self.head: Optional[Block] = None
        self.tail: Optional[Block] = None
        self.length: int = 0
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """Create the genesis block (the first block in the blockchain)."""
        genesis_block = Block(
            timestamp=datetime.datetime.now(),
            data="Genesis Block",
            previous_hash="0"
        )
        self.head = genesis_block
        self.tail = genesis_block
        self.length = 1

    def add_block(self, data: str) -> None:
        """
        Add a new block to the blockchain.
        
        Parameters:
        -----------
        data : str
            The data to be stored in the new block.
        """
        if not self.tail:
            self.create_genesis_block()
            return

        new_block = Block(
            timestamp=datetime.datetime.now(),
            data=data,
            previous_hash=self.tail.hash
        )
        
        # Update LinkedList pointers
        self.tail.next = new_block
        self.tail = new_block
        self.length += 1

    def get_block_at_index(self, index: int) -> Optional[Block]:
        """
        Get block at specific index.
        
        Parameters:
        -----------
        index : int
            The index of the block to retrieve.
            
        Returns:
        --------
        Optional[Block]
            The block at the specified index or None if index is invalid.
        """
        if index < 0 or index >= self.length:
            return None

        current = self.head
        for _ in range(index):
            if current:
                current = current.next
        return current

    def __repr__(self) -> str:
        """Return a string representation of the blockchain."""
        chain_str = ""
        current = self.head
        while current:
            chain_str += str(current) + "\n"
            current = current.next
        return chain_str

    def validate_chain(self) -> tuple[bool, Optional[str]]:
        """
        Validate the integrity of the blockchain.
        
        Returns:
        --------
        Tuple[bool, Optional[str]]
            A tuple containing:
            - bool: True if the chain is valid, False otherwise
            - Optional[str]: Error message if validation fails, None if successful
        """
        if not self.head:
            return True, None

        current_block = self.head
        block_index = 0

        while current_block.next:
            # Validate current block's hash
            if current_block.hash != current_block.calc_hash():
                return False, f"Invalid hash in block {block_index}"

            # Validate link between current block and next block
            if current_block.hash != current_block.next.previous_hash:
                return False, f"Chain broken between blocks {block_index} and {block_index + 1}"

            current_block = current_block.next
            block_index += 1

        # Validate the last block's hash
        if current_block.hash != current_block.calc_hash():
            return False, f"Invalid hash in block {block_index}"

        return True, None

if __name__ == "__main__":
    # Test cases
    print("Test Case 1: Basic blockchain functionality")
    blockchain = Blockchain()
    blockchain.add_block("Block 1 Data")
    blockchain.add_block("Block 2 Data")
    blockchain.add_block("Block 3 Data")
    print(blockchain)

    print("\nTest Case 2: Multiple blockchain instances")
    blockchain1 = Blockchain()
    blockchain2 = Blockchain()
    
    blockchain1.add_block("Blockchain 1 - Transaction")
    blockchain2.add_block("Blockchain 2 - Payment")
    
    print("Blockchain 1:")
    print(blockchain1)
    print("Blockchain 2:")
    print(blockchain2)

    print("\nTest Case 3: Block retrieval by index")
    blockchain = Blockchain()
    blockchain.add_block("Block 1")
    blockchain.add_block("Block 2")
    blockchain.add_block("Block 3")
    
    # Test getting blocks at different indices
    print("Block at index 0:", blockchain.get_block_at_index(0))  # Should return genesis block
    print("Block at index 2:", blockchain.get_block_at_index(2))  # Should return Block 2
    print("Block at index 4:", blockchain.get_block_at_index(4))  # Should return None

    print("\nTest Case 4: Empty block creation")
    blockchain = Blockchain()
    # Try to add blocks with empty data
    blockchain.add_block("")
    blockchain.add_block(None)  # This should handle None gracefully
    print("Blockchain with empty blocks:")
    print(blockchain)
    
    print("\nTest Case 5: Blocks with same timestamp")
    blockchain = Blockchain()
    # Fix the timestamp for testing
    fixed_time = datetime.datetime.now()
    
    # Create multiple blocks with the same timestamp
    test_blocks = [
        Block(fixed_time, "Same Time Block 1", "0"),
        Block(fixed_time, "Same Time Block 2", "0"),
        Block(fixed_time, "Same Time Block 3", "0")
    ]
    
    # Verify that blocks with same timestamp have different hashes
    print("Hash comparison for blocks with same timestamp:")
    for i, block in enumerate(test_blocks):
        print(f"Block {i + 1} Hash: {block.hash}")
        
    # Verify hash uniqueness
    hashes = [block.hash for block in test_blocks]
    unique_hashes = set(hashes)
    print(f"\nNumber of unique hashes: {len(unique_hashes)}")
    print(f"Number of blocks: {len(test_blocks)}")
    print(f"All hashes are unique: {len(unique_hashes) == len(test_blocks)}")
