class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        l = len(arr)
        cnt = 0
        for i in range(0, l - 2, 1):
            for j in range(i + 1, l - 1, 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, l, 1):
                        if (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                            cnt += 1
        return cnt


s1 = Solution()
print(s1.countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3))
print(s1.countGoodTriplets(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1))
