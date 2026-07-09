# Binary Search (Descending Sorted Array)

## 📌 Problem Statement 1

Given a list of integers sorted in **descending order** and a target value (`query`), find the index of the target using **Binary Search**.

If duplicate values are present, return the **first occurrence** of the target.

If the target is not present, return **-1**.

---

## Example

### Input

```python
cards = [10, 9, 8, 8, 7, 6, 5]
query = 8
```

### Output

```python
2
```

---

## Approach

1. Initialize two pointers:
   - `low`
   - `high`
2. Find the middle index.
3. Compare the middle element with the target.
4. If the target is found:
   - Check whether it is the first occurrence.
   - If yes, return the index.
   - Otherwise continue searching on the left side.
5. If the middle element is smaller than the target, search the left half.
6. Otherwise search the right half.
7. Continue until the target is found or the search space becomes empty.

---

## Algorithm

```
Set low = 0
Set high = length - 1

While low <= high:
    Find middle index

    If middle element equals query:
        Check whether it is the first occurrence
        If yes:
            Return middle index
        Else:
            Continue searching left

    Else if middle element < query:
        Search left half

    Else:
        Search right half

Return -1
```

---

## Time Complexity

**O(log n)**

The search space is reduced by half in every iteration.

---

## Space Complexity

**O(1)**

No additional memory is required.

---

## Python Implementation

`BinarySearch.py`