"""
You are given an array of logs. Each log is a space-delimited string of words,
where the first word is the identifier.

There are two types of logs:
    Letter-logs: All words (except the identifier) consist of lowercase English letters.
    Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:
    The letter-logs come before all digit-logs.
    The letter-logs are sorted lexicographically by their contents.
    If their contents are the same, then sort them lexicographically by their identifiers.
    The digit-logs maintain their relative ordering.

Return the final order of the logs.

Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

Example 2:
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

Constraints:
    1 <= logs.length <= 100
    3 <= logs[i].length <= 100
    All the tokens of logs[i] are separated by a single space.
    logs[i] is guaranteed to have an identifier and at least one word after the identifier.

Learnings:
- sorted() accepts more than one element on the `key` parameter, through a tuple
- Real Facebook question. Solved it in 25'. Best solutions are similar to mine
- Better than 90% in speed. Can improve memory usage
"""

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        print(f"\nlogs: {logs}")

        letter_logs = []
        digit_logs = []

        for log in logs:
            if self.is_letter_log(log.split(" ", 1)[1]):
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        # sort letter logs (careful with identical content ones)
        letter_logs = sorted(
            letter_logs, key=lambda l: (l.split(" ", 1)[1], l.split(" ", 1)[0])
        )
        print(f"letter logs: {letter_logs}, letter digit_logs: {digit_logs}")
        print(f"sol: {letter_logs + digit_logs}")
        return letter_logs + digit_logs

    @staticmethod
    def is_letter_log(log: str) -> bool:
        return not all(c.isdigit() for c in log.split())


sol = Solution().reorderLogFiles(
    logs=[
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero",
    ]
)
print(
    sol
    == ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
)

sol = Solution().reorderLogFiles(
    logs=["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
)
print(sol == ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"])

sol = Solution().reorderLogFiles(
    logs=["a1 9 2 3 1", "g2 act car", "zo4 4 7", "ab1 off key dog", "g1 act car"]
)
print(sol == ["g1 act car", "g2 act car", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"])
