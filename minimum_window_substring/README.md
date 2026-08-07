# Minimum Window Substring

## Problem
Find the smallest substring of `s` containing all characters of `t`.

## Approach
- Store character frequencies of `t`.
- Expand the window until all required characters are included.
- Shrink the window while it remains valid.
- Track the minimum window.

## Time Complexity
O(m + n)

## Space Complexity
O(k)

## Concepts Used
- Sliding Window
- HashMap
- Two Pointers