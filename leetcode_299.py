# Bulls and Cows
class Solution:
    @staticmethod
    def getBullHint(s_arr, g_arr):
        bulls = 0
        for i in range(len(s_arr) - 1, -1, -1):
            if s_arr[i] == g_arr[i]:
                bulls += 1
                s_arr.pop(i)  # deleting from front will corrupt the index hence deleting from back
                g_arr.pop(i)
        return bulls, s_arr, g_arr

    @staticmethod
    def getCowHint(s_arr, g_arr):
        cows = 0
        for ch in s_arr:
            try:
                x = g_arr.index(ch)
                cows += 1
                g_arr.pop(x)
            except ValueError:
                continue
        return cows

    def getHint(self, secret, guess):
        s_arr = list(secret)
        g_arr = list(guess)
        bulls, s_arr, g_arr = self.getBullHint(s_arr, g_arr)
        cows = self.getCowHint(s_arr, g_arr)
        return str(bulls) + "A" + str(cows) + "B"


s = Solution()
print(s.getHint(secret="1807", guess="7810"))
print(s.getHint(secret="1123", guess="0111"))
print(s.getHint(secret="1", guess="0"))
print(s.getHint(secret="1", guess="1"))
