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

    # Test Case 4: Repeated identical data
    print("\nTest Case 4: Repeated identical data")
    blockchain = Blockchain()
    repeated_data = "AAAAAAA"  # Test with repeated characters
    
    # Add multiple blocks with the same data
    for _ in range(3):
        blockchain.add_block(repeated_data)
    
    print("Blockchain with repeated data:")
    print(blockchain)
    
    # Verify that each block has a unique hash despite identical data
    block0 = blockchain.get_block_at_index(0)  # Genesis block
    block1 = blockchain.get_block_at_index(1)  # First repeated data block
    block2 = blockchain.get_block_at_index(2)  # Second repeated data block
    block3 = blockchain.get_block_at_index(3)  # Third repeated data block
    
    print("\nVerifying unique hashes for blocks with identical data:")
    if block1 and block2 and block3:  # Check if blocks exist
        print(f"Block 1 hash: {block1.hash}")
        print(f"Block 2 hash: {block2.hash}")
        print(f"Block 3 hash: {block3.hash}")
        
        # Assert that all hashes are different
        assert block1.hash != block2.hash != block3.hash, "Blocks with same data should have different hashes"
        print("✓ All blocks have unique hashes")
        
        # Verify that previous_hash links are correct
        assert block1.previous_hash == block0.hash, "Block 1 previous_hash should match Genesis block hash"
        assert block2.previous_hash == block1.hash, "Block 2 previous_hash should match Block 1 hash"
        assert block3.previous_hash == block2.hash, "Block 3 previous_hash should match Block 2 hash"
        print("✓ All previous_hash links are correct")
