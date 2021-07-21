#Subdomain Visit Count
class Solution:
    def subdomainVisits(self, cpdomains):
        d = {}
        for cp in cpdomains:
            visit_cnt, visit_dom = cp.split()
            lst_dom = visit_dom.split('.')
            for i in range(len(lst_dom)):
                dom = '.'.join(lst_dom[i:])
                if dom in d:
                    d[dom] = d[dom] + int(visit_cnt)
                else:
                    d[dom] = int(visit_cnt)
        return [str(v)+' '+k for k, v in d.items()]

s = Solution()
print(s.subdomainVisits(["9001 discuss.leetcode.com"]))
print(s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))

# Slow
#    @staticmethod
#    def getsubdom(domain):
#        l = []
#        s = domain.split('.')
#        for i in range(len(s)):
#            l.append('.'.join(s[i:]))
#        return l
#
#    def subdomainVisits(self, cpdomains):
#        d = {}
#        for cp in cpdomains:
#            visit_cnt = cp.split()[0]
#            lst_dom = self.getsubdom(cp.split()[1])
#            for dom in lst_dom:
#                if dom in d:
#                    d[dom] = d[dom] + int(visit_cnt)
#                else:
#                    d[dom] = int(visit_cnt)
#        res = []
#        for k, v in d.items():
#            res.append(str(v)+' '+k)
#        return res

