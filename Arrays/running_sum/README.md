# 1480. Running Sum of 1d Array

## Problem
Given an integer array `nums`, return the running sum of the array.

## Approach
Traverse the array from left to right. Add the previous running sum to the current element and update it in place.

## Algorithm
1. Start from index 1.
2. Add the previous element to the current element.
3. Continue until the end.
4. Return the modified array.

## Time Complexity
O(n)

## Space Complexity
O(1)

## Concepts
- Arrays
- Prefix Sum