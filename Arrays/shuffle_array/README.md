# 1470. Shuffle the Array

## Problem
Rearrange the array into the pattern:
[x1,y1,x2,y2,...]

## Approach
Create a new array and alternately place elements from the first and second halves.

## Algorithm
1. Traverse from 0 to n-1.
2. Append nums[i].
3. Append nums[i+n].
4. Return the new array.

## Time Complexity
O(n)

## Space Complexity
O(n)

## Concepts
- Arrays