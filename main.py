import heapq
from collections import namedtuple

# Define the Node class for the Huffman Tree
class Node(namedtuple("Node", ["freq", "char", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

# Build the Huffman Tree
def build_huffman_tree(probabilities):
    # Create a heap of initial nodes
    heap = [Node(prob, char, None, None) for char, prob in probabilities.items()]
    heapq.heapify(heap)
    
    # Combine nodes to form the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)  # Remove the smallest node
        right = heapq.heappop(heap)  # Remove the second smallest node
        
        # Merge two nodes into a parent node
        merged = Node(left.freq + right.freq, None, left, right)
        heapq.heappush(heap, merged)  # Add the merged node back to the heap

    return heap[0]  # The root of the tree

# Generate Huffman codes from the tree
def generate_huffman_codes(node, prefix="", huffman_code={}):
    if node is None:
        return

    # If it's a leaf node, store the code
    if node.char is not None:
        huffman_code[node.char] = prefix
    else:
        # Traverse left and right subtrees
        generate_huffman_codes(node.left, prefix + "0", huffman_code)
        generate_huffman_codes(node.right, prefix + "1", huffman_code)

    return huffman_code

# Main function to generate Huffman codes
def huffman_coding(source, probabilities):
    # Check if probabilities match the source
    if len(source) != len(probabilities):
        raise ValueError("The source and probabilities must have the same length.")

    # Create a dictionary of character-probability pairs
    prob_dict = {source[i]: probabilities[i] for i in range(len(source))}

    # Build the Huffman Tree
    root = build_huffman_tree(prob_dict)

    # Generate Huffman codes
    huffman_code = generate_huffman_codes(root)

    return huffman_code

# Example usage
if __name__ == "__main__":
    # Source and their probabilities
    source = ['a', 'b', 'c', 'd', 'e']
    probabilities = [1/3,1/5, 1/5, 2/15,2/15]

    # Generate Huffman codes
    huffman_code = huffman_coding(source, probabilities)

    # Display the results
    print("Character Probabilities and Huffman Codes:")
    for char in source:
        print(f"Character: {char}, Probability: {probabilities[source.index(char)]}, Code: {huffman_code[char]}")
