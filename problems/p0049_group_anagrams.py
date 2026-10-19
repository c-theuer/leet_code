"""
49. Group Anagrams  (Medium)
https://leetcode.com/problems/group-anagrams/

Group the strings in strs that are anagrams of each other. The groups, and the
strings within each group, may be returned in any order.
Constraints: 1 <= strs.length <= 10^4, 0 <= strs[i].length <= 100,
strs[i] is lowercase English letters
"""

import pytest

from lc import *  # noqa: F401,F403


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict = {}

        for s in strs:
            key = tuple(sorted(s))
            if key not in dict:
                dict[key] = []
            dict[key].append(s)
        return list(dict.values())


def normalize(groups: list[list[str]]) -> list[list[str]]:
    # Any order is accepted, so compare with groups and their contents sorted.
    return sorted(sorted(g) for g in groups)


N = 10**4
LONG = "abcdefghijklmnopqrstuvwxy" * 4  # 100 chars

CASES = [
    # LeetCode examples
    (
        (["eat", "tea", "tan", "ate", "nat", "bat"],),
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    (([""],), [[""]]),
    ((["a"],), [["a"]]),
    # edge cases
    ((["", ""],), [["", ""]]),
    ((["", "a"],), [[""], ["a"]]),
    ((["ab", "ab"],), [["ab", "ab"]]),  # duplicates stay in the same group
    ((["aab", "abb", "bab", "aba"],), [["aab", "aba"], ["abb", "bab"]]),
    ((["abc", "def", "ghi"],), [["abc"], ["def"], ["ghi"]]),
    ((["ab", "abc", "ba"],), [["ab", "ba"], ["abc"]]),  # length matters
    # max length
    (([""] * N,), [[""] * N]),
    (
        (["abc", "bca", "cab", "xyz", "zyx"] * (N // 5),),
        [["abc", "bca", "cab"] * (N // 5), ["xyz", "zyx"] * (N // 5)],
    ),
    (([LONG, LONG[::-1]] * (N // 2),), [[LONG, LONG[::-1]] * (N // 2)]),
]


@pytest.mark.parametrize("args, expected", CASES)
def test_solution(args, expected):
    got = Solution().groupAnagrams(list(args[0]))
    assert normalize(got) == normalize(expected)


if __name__ == "__main__":
    for args, expected in CASES:
        got = Solution().groupAnagrams(list(args[0]))
        shown = args if len(args[0]) <= 10 else f"(<{len(args[0])} strings>,)"
        print(
            "PASS" if normalize(got) == normalize(expected) else "FAIL",
            shown,
            "->",
            got if len(args[0]) <= 10 else f"<{len(got)} groups>",
            "| expected",
            expected if len(args[0]) <= 10 else f"<{len(expected)} groups>",
        )
