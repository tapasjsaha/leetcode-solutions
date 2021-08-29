# Unique Email Addresses
class Solution:
    def numUniqueEmails(self, emails: [str]) -> int:
        res = []
        for email in emails:
            localName, domainName = email.split('@')
            localName = localName.split('+')[0]
            localName = localName.replace(".", "")
            email = localName + '@' + domainName
            res.append(email)
        return len(set(res))


s = Solution()
print(s.numUniqueEmails(
    emails=["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
print(s.numUniqueEmails(
    emails=["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
