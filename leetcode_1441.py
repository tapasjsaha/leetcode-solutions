# Build an Array With Stack Operations
class Solution:
    def buildArray(self, target, n):
        res = []
        i = 1
        while i <= target[-1] and i <= n:
            if i in target:
                res.append("Push")
            else:
                res.append("Push")
                res.append("Pop")
            i += 1
        return res


s = Solution()
print(s.buildArray(target=[1, 3], n=3))
print(s.buildArray(target=[1, 2, 3], n=3))
print(s.buildArray(target=[1, 2], n=4))
print(s.buildArray(target=[2, 3, 4], n=4))
#print(s.buildArray(target=[], n=4))
