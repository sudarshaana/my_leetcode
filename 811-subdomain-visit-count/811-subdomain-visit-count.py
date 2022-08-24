class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        dic = {}
        
        for d in cpdomains:
            
            visit, domain = d.split(" ")
            
            s_domain = domain.split(".")
            for i in range(len(s_domain)):
                dd = '.'.join(s_domain[i:])
                dic[dd] = dic.get(dd, 0) + int(visit)
                
        res = []
        for key, val in dic.items():
            res.append(f"{val} {key}")
            
        return res