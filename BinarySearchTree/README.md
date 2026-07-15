# Functional Binary Search Tree (BST) Logic

A minimalist implementation of a Binary Search Tree (BST) data structure in Python using standalone recursive functions. This architecture isolates tree navigation logic from the structural `Node` memory containers.

---

## 📐 The Tree Structure

Given your specific sequence of insertions:
1. `root = Node(50)`
2. `insert(root, 49)`
3. `insert(root, 59)`
4. `insert(root, 69)`
5. `insert(root, 9)`
6. `insert(root, 19)`

The values arrange themselves into the following hierarchical tree shape based on the strict BST rule (*values smaller go left, values larger go right*):

```text
         50 (Root)
        /  \
      49    59
     /        \
    9          69
     \
      19


