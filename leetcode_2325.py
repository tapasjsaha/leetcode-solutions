# Decode the Message
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {' ': ' '}
        i, j = 0, 0
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        while i < len(key) and j <= 25:
            if key[i] not in d:
                d[key[i]] = alpha[j]
                j += 1
            i += 1

        res = ''
        for ch in message:
            res += d[ch]

        return res


s = Solution()
print(s.decodeMessage(key="eljuxhpwnyrdgtqkviszcfmabo", message="zwx hnfx lqantp mnoeius ycgk vcnjrdb"))
