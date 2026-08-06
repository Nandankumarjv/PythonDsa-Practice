# Longest Substring Without Repeating Characters

## Problem
Find the length of the longest substring without repeating characters.

## Approach
- Maintain a sliding window.
- Store the last index of each character.
- Move the left pointer whenever a duplicate is found.

## Time Complexity
O(n)

## Space Complexity
O(min(n, charset))

## Concepts Used
- Sliding Window
- HashMap
- Two Pointers