class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for v in self.tokens.values():
            if v > currentTime:
                count += 1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
obj = AuthenticationManager(5)
obj.renew("aaa", 1)
obj.generate("aaa", 2)
print(obj.countUnexpiredTokens(6))
obj.generate("bbb", 7)
obj.renew("aaa", 8)
obj.renew("bbb", 10)
print(obj.countUnexpiredTokens(15))
