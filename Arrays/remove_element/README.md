# 27. Remove Element

## Problem
Remove all occurrences of a given value in-place and return the number of remaining elements.

## Approach
Use two pointers. One pointer scans the array while the other stores the next valid position.

## Algorithm
1. Traverse the array.
2. If the current element is not equal to `val`, copy it to the write pointer.
3. Increment the write pointer.
4. Return the number of valid elements.

## Time Complexity
O(n)

## Space Complexity
O(1)

## Concepts
- Arrays
- Two Pointers