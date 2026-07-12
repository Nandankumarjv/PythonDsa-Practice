# Linear Search

## 📌 Problem Statement 1

Given a list of integers and a target value (`query`), find the index of the target element.

If the target element is not present in the list, return **-1**.

---

## Example

### Input

```python
cards = [10, 9, 8, 7, 6, 5, 4]
query = 7
```

### Output

```python
3
```

---

## Approach

1. Start from the first element of the list.
2. Compare each element with the target value.
3. If a match is found, return its index.
4. If the entire list is traversed without finding the target, return **-1**.

---

## Algorithm

```
For each element in the array:
    If element == query:
        Return its index

Return -1
```

---

## Time Complexity

**O(n)**

In the worst case, every element is checked once.

---

## Space Complexity

**O(1)**

No extra memory is used.

---

## Python Implementation

`linear_search.py`

#-----------------------------------------------

## 📌 Problem Statement 2

Given a sorted array that has been rotated an unknown number of times, determine the number of rotations.

The number of rotations is equal to the index of the smallest element in the array.

If the array is not rotated, return **0**.

---

## Example 1

### Input

```python
nums = [4, 5, 6, 1, 2, 3]
```

### Output

```python
3
```

### Explanation

The smallest element is **1**, which is located at index **3**. Therefore, the array has been rotated **3** times.

---

## Example 2

### Input

```python
nums = [1, 2, 3, 4, 5]
```

### Output

```python
0
```

### Explanation

The array is already sorted and has not been rotated.

---

## Approach

1. Traverse the array from left to right.
2. Compare each element with its previous element.
3. If the current element is smaller than the previous element, return its index.
4. If no such element exists, the array is not rotated, so return **0**.

---

## Algorithm

```
Initialize position = 0

While position is less than the length of the array:

    If position > 0 and current element < previous element:
        Return position

    Move to the next position

Return 0
```

---

## Time Complexity

**O(n)**

The algorithm scans the array once in the worst case.

---

## Space Complexity

**O(1)**

No additional memory is used.

---

## Test Cases Covered

- Rotated array
- Non-rotated array
- Empty array
- Single-element array
- Rotation by one position
- Small arrays
- Multiple rotation scenarios

---

## Python Implementation

`rotation_count.py`

-------------------------------

## 📌 Problem Statement 3

# Sorted User Database System

A lightweight, in-memory user database simulation implemented in Python. This project demonstrates core Object-Oriented Programming (OOP) concepts, data validation techniques, and custom string representations (`__repr__` and `__str__`). 

Instead of relying on complex third-party databases, this system maintains a collection of user profiles dynamically stored in **perfect alphabetical order** within a contiguous memory block.

---

## 🚀 Features

* **Auto-Sorting Insertion:** Automatically discovers the exact chronological/alphabetical index placement for new users upon insertion.
* **Linear Lookup Tracking:** Traverses memory arrays to safely locate structural data instances.
* **Safe Profile Updates:** Validates the presence of an identity footprint inside memory arrays before modifying personal account information to prevent software instability.
* **Polished Representation Overloads:** Leverages Python dunder magic methods (`__repr__`, `__str__`) to emit readable, syntax-accurate console representations during data debugging sequences.

---

## 🛠️ Performance Analysis

The underlying data layout is a linear sequence (**Python List**), not a tree structure (like a Binary Search Tree).

### 1. How Insertion Sorting Works
When executing `.insert()`, a tracking index steps forward, testing alphabetical inequality loops (`>`) character-by-character based on standard ASCII value strings:



* **Scenario:** If the database contains `["alice", "bob", "cherry"]` and you add `"abhay"`, the system determines that `"alice"` comes *after* `"abhay"` alphabetically (`"alice" > "abhay"` is `True`).
* **Result:** The system breaks out of its evaluation loop at index `0`, injects `"abhay"` right at the front, and cleanly slides the rest of the records forward.

### 2. Time Complexity Matrix

| Operation | Current List Implementation | Binary Search Tree (BST) Alternative |
| :--- | :--- | :--- |
| **Insert** | **$O(n)$** (Requires moving elements in memory) | **$O(\log n)$** (Fast pointer manipulation) |
| **Find** | **$O(n)$** (Linear scanning step-by-step) | **$O(\log n)$** (Halves the search space every step) |
| **Update** | **$O(n)$** (Limited by linear lookup metrics) | **$O(\log n)$** (Logarithmic traversal speeds) |

---

## 💻 Code Architecture

The solution uses two distinct structural components:

1. **`User` Class:** A clean metadata layout storing properties like `name`, `username`, and `email`. It overloads representation boundaries to mask dirty default memory pointers (like `<__main__.User object at...>`) with clean syntax formatting.
2. **`UserDatabase` Class:** An independent management workspace supervising internal storage lists via specific data manipulation pipelines.

---

## 📖 Verification Script & Console Log Output

The script contains a simulation initializing 5 target user files, verifying lookup consistency, modifying profile settings, and verifying changes safely:

### Expected Terminal Printout Trace

Executing this file locally displays the following output history in your console terminal:

```text
# Log 1: Array Content via print(db.list())
[User(username='abhay', name='Abhay', email='a@gmail.com'), User(username='alice', name='Alice', email='aice@gmail.com'), User(username='bob', name='Bob', email='bob@gmail.co.'), User(username='che', name='Chi', email='che@mail.com'), User(username='cherry', name='Cherry', email='c@gmail.com')]

# Log 2: User Lookup via print(db.find('abhay'))
User(username='abhay', name='Abhay', email='a@gmail.com')

# Log 3: Updated Instance Verification Post-Update Execution
User(username='abhay', name='Abhayyy', email='abhayy@gmail.com')