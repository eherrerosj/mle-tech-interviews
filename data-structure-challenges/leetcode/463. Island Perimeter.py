"""
In an alien language, surprisingly they also use english lowercase letters,
but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in this alien language.


Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 20
    order.length == 26
    All characters in words[i] and order are English lowercase letters.

Learnings:
- Overcomplicated myself: loop every row and column starting from both sides (2x nested for loops). Used
    a XOR operation between current cell and next cell. Problem would be for 1 dim grids
- Better solution: look through every cell (O(m*n) time complexity). If current cell is land: check its
    4 surroundings: +1 if there's land on each, 0 otherwise; then add to the result (4 - (top-left-bottom-right))
"""

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r == 0:
                        up = 0
                    else:
                        up = grid[r - 1][c]
                    if c == 0:
                        left = 0
                    else:
                        left = grid[r][c - 1]
                    if r == rows - 1:
                        down = 0
                    else:
                        down = grid[r + 1][c]
                    if c == cols - 1:
                        right = 0
                    else:
                        right = grid[r][c + 1]

                    result += 4 - (up + left + right + down)

        return result


sol = Solution().islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])
print(sol == 16)

sol = Solution().islandPerimeter(grid=[[0, 1]])
print(sol == 4)

sol = Solution().islandPerimeter(grid=[[1, 1, 1]])
print(sol == 8)
