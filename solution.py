class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        NO_ROUTE = -1
        frs, tos = defaultdict(list), set() ## convert flights to dictionary/set form
        flights.sort(key=lambda x:x[2], reverse=True)
        for fr,to,price in flights:
            frs[fr].append([to, price])
            tos.add(to)
        if src not in frs or dst not in tos: return NO_ROUTE ## early exit
        
        cheapest, l = float('inf'), [[t,p,0] for t,p in frs[src]]
        while l: ## dfs
            to, price, stop = l.pop()
            if price>=cheapest: continue
            if to==dst: 
                cheapest = price
            elif stop<k and to in frs:
                for t,p in frs[to]:
                    if price+p<cheapest:
                        l += [[t, price+p, stop+1]]
        return cheapest if cheapest!=float('inf') else NO_ROUTE