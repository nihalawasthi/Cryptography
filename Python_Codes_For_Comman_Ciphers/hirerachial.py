#35
import hashlib

class TreeNode:
    def _init_(self, data, children=None):
        self.data = data
        self.children = children or []

def hierarchical_hash(node):
    if not node.children:
        return hashlib.sha256(node.data.encode()).hexdigest()
    
    child_hashes = [hierarchical_hash(child) for child in node.children]
    combined_data = node.data + ''.join(child_hashes)
    return hashlib.sha256(combined_data.encode()).hexdigest()

# Create a simple hierarchical structure
root_node = TreeNode("Root Node")
child_node1 = TreeNode("Child Node 1")
child_node2 = TreeNode("Child Node 2")
root_node.children = [child_node1, child_node2]

# Calculate the hierarchical hash for the root node
root_hash = hierarchical_hash(root_node)
print("Hierarchical Hash:", root_hash)