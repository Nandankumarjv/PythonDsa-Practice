# Longest Repeating Character Replacement

## Problem
Find the length of the longest substring that can be made of the same character after replacing at most `k` characters.

## Approach
- Maintain character frequencies.
- Track the highest frequency character.
- If replacements exceed `k`, shrink the window.
- Keep updating the maximum window size.

## Time Complexity
O(n)

## Space Complexity
O(1)

## Concepts Used
- Sliding Window
- HashMap