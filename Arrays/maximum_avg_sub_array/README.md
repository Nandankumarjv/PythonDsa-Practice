# 643. Maximum Average Subarray I

## Problem
Find the maximum average value of any contiguous subarray of length `k`.

## Approach
Use a fixed-size sliding window to maintain the current window sum.

## Algorithm
1. Calculate the sum of the first window.
2. Slide the window by removing the left element and adding the new right element.
3. Keep track of the maximum window sum.
4. Return the maximum average.

## Time Complexity
O(n)

## Space Complexity
O(1)

## Concepts
- Arrays
- Sliding Window