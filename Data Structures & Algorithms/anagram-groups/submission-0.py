class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)   # maps character counts -> list of anagrams

        for s in strs:
            count = [0] * 26      # creates 26 zeros for a-z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())   # convert values into a list