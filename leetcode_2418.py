# Sort the People
class Solution:
    def sortPeople(self, names: [str], heights: [int]) -> [str]:
        x = list(zip(names, heights))
        x.sort(key=lambda a: a[1], reverse=True)
        names = [a[0] for a in x]
        return names


s = Solution()
print(s.sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))
print(s.sortPeople(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150]))
