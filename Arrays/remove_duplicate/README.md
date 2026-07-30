# 26. Remove Duplicates from Sorted Array

## Problem
Remove duplicates from a sorted array in-place and return the number of unique elements.

## Approach
Use two pointers. One pointer tracks the last unique element while the other scans the array.

## Algorithm
1. Keep the first element.
2. Compare the current element with the previous unique element.
3. If different, place it at the write pointer.
4. Return the count of unique elements.

## Time Complexity
O(n)

## Space Complexity
O(1)

## Concepts
- Arrays
- Two Pointers