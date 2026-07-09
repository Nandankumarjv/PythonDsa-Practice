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