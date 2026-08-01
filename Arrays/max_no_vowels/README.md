# 1456. Maximum Number of Vowels in a Substring of Given Length

## Problem
Find the maximum number of vowels present in any substring of length `k`.

## Approach
Use a fixed-size sliding window and maintain the count of vowels inside the current window.

## Algorithm
1. Count vowels in the first window.
2. Slide the window by removing the left character and adding the new right character.
3. Update the maximum vowel count.
4. Return the maximum count.

## Time Complexity
O(n)

## Space Complexity
O(1)

## Concepts
- Strings
- Sliding Window
- Hash Set