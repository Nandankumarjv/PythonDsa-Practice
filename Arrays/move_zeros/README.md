# 283. Move Zeroes

## Problem
Move all zeros to the end while maintaining the relative order of non-zero elements.

## Approach
Use two pointers to move all non-zero elements to the front, then fill the remaining positions with zeros.

## Algorithm
1. Traverse the array.
2. Copy non-zero values to the write pointer.
3. Fill remaining positions with zeros.
4. Return the modified array.

## Time Complexity
O(n)

## Space Complexity
O(1)

## Concepts
- Arrays
- Two Pointers