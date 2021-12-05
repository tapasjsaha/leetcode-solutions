# Word Break
# Trying BFS
class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        queue = [0]
        visited = set()
        while queue:
            # print(queue)
            start = queue.pop(0)
            if start in visited:
                pass
            else:
                visited.add(start)
                for i in range(start, len(s) + 1, 1):
                    # print(s[start:i])
                    if s[start:i] in wordDict:
                        if i == len(s):
                            return True
                        else:
                            queue.append(i)
        return False


s = Solution()
print(s.wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(s.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(s.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
print(s.wordBreak(s="a", wordDict=["a", "code"]))
print(s.wordBreak(
    s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    wordDict=["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
