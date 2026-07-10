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


-------------------------------------


# Rotation Count in a Sorted Rotated Array (Binary Search)

## 📌 Problem Statement 2

Given a sorted array that has been rotated an unknown number of times, determine the number of rotations.

The number of rotations is equal to the index of the smallest element in the array.

Your task is to find the rotation count using **Binary Search**.

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

The smallest element is **1**, which is located at index **3**. Hence, the array has been rotated **3** times.

---

## Example 2

### Input

```python
nums = [1, 2, 3, 4, 5, 6]
```

### Output

```python
0
```

### Explanation

The array is already sorted, so it has not been rotated.

---

## Approach

Instead of scanning every element, use **Binary Search** to locate the smallest element.

1. Initialize two pointers:
   - `low = 0`
   - `high = len(nums) - 1`
2. Find the middle index.
3. If the middle element is smaller than its previous element, return its index.
4. If the middle element is greater than the last element, search the right half.
5. Otherwise, search the left half.
6. If no rotation point is found, return **0**.

---

## Algorithm

```
Set low = 0
Set high = length - 1

While low <= high:

    Find middle index

    If middle element is smaller than previous element:
        Return middle index

    Else if middle element is greater than last element:
        Search the right half

    Else:
        Search the left half

Return 0
```

---

## Time Complexity

**O(log n)**

Binary Search reduces the search space by half in each iteration.

---

## Space Complexity

**O(1)**

No additional memory is required.

---

## Test Cases Covered

- Rotated array
- Non-rotated array
- Empty array
- Single-element array
- Rotation by one position
- Multiple rotation scenarios

---

## Python Implementation

`rotation_count_binary_search.py`