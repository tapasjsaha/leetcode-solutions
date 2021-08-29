# Defanging an IP Address
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


s = Solution()
print(s.defangIPaddr(address="1.1.1.1"))
print(s.defangIPaddr(address="255.100.50.0"))
