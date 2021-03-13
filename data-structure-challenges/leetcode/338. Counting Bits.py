"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
    calculate the number of 1's in their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]

Follow up:
    - It is very easy to come up with a solution with run time O(n*sizeof(integer)).
        But can you do it in linear time O(n) /possibly in a single pass?
    - Space complexity should be O(n).
    - Can you do it like a boss? Do it without using any builtin function like
        __builtin_popcount in c++ or in any other language.

Learnings:
- My solution works but it is slow, I think it's because complexity is around O(n^2)
- Could be done way faster. Another proposed solution is 
- Counting ones could be done using (i & (i - 1)), which is actually
    Brian Kernighan’s Algorithm, so always keep it handy for counting ones
- Another interesting solution is while len(res) <= num: res += [i + 1 for i in res],
    which is not intuitive at all IMO
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        print(f"num: {num}")
        sol = [0]
        if num == 0:
            return sol
        for n in range(1, num + 1):
            num_ones = 0
            while n > 0:
                num_ones += n & 1
                n = n >> 1
            sol.append(num_ones)
        print(f"sol: {sol}")
        return sol


sol = Solution().countBits(num=20)
print(sol == [0, 1, 1])


sol = Solution().countBits(num=5)
print(sol == [0, 1, 1, 2, 1, 2])
