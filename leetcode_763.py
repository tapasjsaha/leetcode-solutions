# Partition Labels
class Solution:
    def partitionLabels(self, s: str) -> [int]:
        res = []

        def partition(st):
            end = len(st) - 1
            start = s.index(st[end])
            while end > start > 0:
                i = s.index(st[end])
                if i < start:
                    start = i
                end -= 1
            res.append(st[start:])
            if start > 0:
                partition(st[:start])

        partition(s)
        res.reverse()
        return [len(r) for r in res]


s = Solution()
print(s.partitionLabels(s="ababcbacadefegdehijhklij"))
print(s.partitionLabels(s="eccbbbbdec"))
