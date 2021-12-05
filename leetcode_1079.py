# Letter Tile Possibilities
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = []
        d = {}

        def backtrack(current, available, l):
            if len(current) == l:
                res.append(current[:])
            else:
                candidate_list = [key for (key, val) in available.items() if val > 0]
                for candidate in candidate_list:
                    available[candidate] -= 1
                    backtrack(current + [candidate], available, l)
                    available[candidate] += 1

        for n in tiles:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for i in range(1, len(tiles) + 1, 1):
            backtrack([], d, i)
        #print(res)
        return len(res)


s = Solution()
print(s.numTilePossibilities(tiles="AAB"))
print(s.numTilePossibilities(tiles="AAABBC"))
print(s.numTilePossibilities(tiles="V"))
