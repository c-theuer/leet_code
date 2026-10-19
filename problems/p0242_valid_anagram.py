"""
242. Valid Anagram  (Easy)
https://leetcode.com/problems/valid-anagram/

Return true if t is an anagram of s (uses exactly the same letters, the same
number of times), and false otherwise.
Constraints: 1 <= s.length, t.length <= 5 * 10^4, s and t are lowercase English letters
Follow up: what if the inputs contain Unicode characters?
"""

from typing import Counter

import pytest

from lc import *  # noqa: F401,F403


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)


N = 5 * 10**4

CASES = [
    # LeetCode examples
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
    # edge cases
    (("a", "a"), True),
    (("a", "b"), False),
    (("a", "ab"), False),  # different lengths
    (("ab", "a"), False),
    (("aab", "abb"), False),  # same letters, different counts
    (("abc", "cba"), True),
    (("listen", "silent"), True),
    # max length
    (("a" * N, "a" * N), True),
    (("ab" * (N // 2), "ba" * (N // 2)), True),
    (("a" * (N - 1) + "b", "a" * N), False),
    (("abcdefghijklmnopqrstuvwxyz" * 1923, "zyxwvutsrqponmlkjihgfedcba" * 1923), True),
]


@pytest.mark.parametrize("args, expected", CASES)
def test_solution(args, expected):
    assert Solution().isAnagram(*args) == expected


if __name__ == "__main__":
    for args, expected in CASES:
        got = Solution().isAnagram(*args)
        shown = (
            args
            if max(map(len, args)) <= 20
            else tuple(f"<{len(a)} chars>" for a in args)
        )
        print(
            "PASS" if got == expected else "FAIL",
            shown,
            "->",
            got,
            "| expected",
            expected,
        )
