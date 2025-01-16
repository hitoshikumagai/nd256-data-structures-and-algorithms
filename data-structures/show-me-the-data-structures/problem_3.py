import heapq
from collections import defaultdict
from typing import Optional

# Huffman Tree Node
class HuffmanNode:
    """
    A class to represent a node in the Huffman Tree.

    Attributes:
    -----------
    char : Optional[str]
        The character stored in the node.
    freq : int
        The frequency of the character.
    left : Optional[HuffmanNode]
        The left child node.
    right : Optional[HuffmanNode]
        The right child node.
    """

    def __init__(self, char: Optional[str], freq: int) -> None:
        """
        Constructs all the necessary attributes for the HuffmanNode object.

        Parameters:
        -----------
        char : Optional[str]
            The character stored in the node.
        freq : int
            The frequency of the character.
        """
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than comparison operator for HuffmanNode.

        Parameters:
        -----------
        other : HuffmanNode
            The other HuffmanNode to compare with.

        Returns:
        --------
        bool
            True if the frequency of this node is less than the other node, False otherwise.
        """
        return self.freq < other.freq

def calculate_frequencies(data: str) -> dict[str, int]:
    """
    Calculate the frequency of each character in the given data.

    Parameters:
    -----------
    data : str
        The input string for which frequencies are calculated.

    Returns:
    --------
    Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.
    """
    frequency = defaultdict(int)

    for char in data:
        frequency[char] += 1
    
    return dict(frequency)

def build_huffman_tree(frequency: dict[str, int]) -> HuffmanNode:
    """
    Build the Huffman Tree based on the character frequencies.

    Parameters:
    -----------
    frequency : Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    Returns:
    --------
    HuffmanNode
        The root node of the constructed Huffman Tree.
    """
    if not frequency:
        return None
    
    # Special case: single character
    if len(frequency) == 1:
        char = next(iter(frequency))
        root = HuffmanNode(char, frequency[char])
        return root

    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0] if priority_queue else None

def generate_huffman_codes_iterative(root: Optional[HuffmanNode]) -> dict[str, str]:
    """
    Generate Huffman codes for each character using an iterative approach.
    
    Parameters:
    -----------
    root : Optional[HuffmanNode]
        The root of the Huffman Tree.
    
    Returns:
    --------
    Dict[str, str]
        A dictionary containing characters and their Huffman codes.
    """
    if not root:
        return {}

    # Special case: root is a leaf node (single character case)
    if root.char is not None:
        return {root.char: "0"}

    huffman_codes = {}
    stack = [(root, "")]
    
    while stack:
        node, code = stack.pop()
        
        # If leaf node, store the code
        if node.char is not None:
            huffman_codes[node.char] = code
        
        # Add child nodes to stack
        if node.right:
            stack.append((node.right, code + "1"))
        if node.left:
            stack.append((node.left, code + "0"))
            
    return huffman_codes

def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    """
    Encode the given data using Huffman coding.

    Parameters:
    -----------
    data : str
        The input string to be encoded.

    Returns:
    --------
    Tuple[str, Optional[HuffmanNode]]
        A tuple containing the encoded string and the root of the Huffman Tree.
    """
    if not data:
        return "", None

    frequency = calculate_frequencies(data)
    root = build_huffman_tree(frequency)
    huffman_codes = {}
    huffman_codes = generate_huffman_codes_iterative(root)

    encoded_data = "".join(huffman_codes[char] for char in data)
    return encoded_data, root

def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    """
    Decode the given encoded data using the Huffman Tree.

    Parameters:
    -----------
    encoded_data : str
        The encoded string to be decoded.
    tree : Optional[HuffmanNode]
        The root of the Huffman Tree used for decoding.

    Returns:
    --------
    str
        The decoded string.
    """
    if not tree or not encoded_data:
        return ""

    # Special case: tree is a leaf node (single character case)
    if tree.char is not None:
        return tree.char * len(encoded_data)

    decoded_data = []
    current_node = tree

    for bit in encoded_data:
        current_node = current_node.left if bit == "0" else current_node.right
        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = tree

    return "".join(decoded_data)


# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fun!"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data
    
    # Test Case 2: Empty string
    # Tests edge case of empty input
    # Verifies proper handling of null/empty inputs
    print("\nTest Case 2: Empty string")
    test_str2 = ""
    encoded_data2, tree2 = huffman_encoding(test_str2)
    print("Original:", test_str2)
    print("Encoded:", encoded_data2)
    decoded_data2 = huffman_decoding(encoded_data2, tree2)
    print("Decoded:", decoded_data2)
    assert test_str2 == decoded_data2

    # Test Case 3: String with special characters
    # Tests encoding/decoding with a mix of regular and special characters
    # Verifies handling of extended ASCII and special symbols
    print("\nTest Case 3: String with special characters")
    test_str3 = "Hello, World!@#$%^&*()"
    encoded_data3, tree3 = huffman_encoding(test_str3)
    print("Original:", test_str3)
    print("Encoded:", encoded_data3)
    decoded_data3 = huffman_decoding(encoded_data3, tree3)
    print("Decoded:", decoded_data3)
    assert test_str3 == decoded_data3

    # Test Case 4: String with repeated characters
    # Tests encoding/decoding of a string with single repeated character
    # Verifies optimal encoding length (should be 1 bit per character)
    # and correct tree structure (single branch with one leaf)
    print("\nTest Case 4: Repeated characters")
    test_str4 = "AAAAAAA"
    encoded_data4, tree4 = huffman_encoding(test_str4)
    print("Original:", test_str4)
    print("Encoded:", encoded_data4)
    decoded_data4 = huffman_decoding(encoded_data4, tree4)
    print("Decoded:", decoded_data4)
    assert test_str4 == decoded_data4
    print("Length of encoded data:", len(encoded_data4))
    print("Expected optimal length:", len(test_str4))  # Since all characters are same, each should be encoded as single bit
