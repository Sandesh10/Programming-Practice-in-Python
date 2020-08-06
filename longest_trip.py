"""
  Longest Trip
"""

def graph():
    g ={}
    
    def add_edge(node):
        n = node.split(":")
        if g.get(n[0])==None:
            g[n[0]]={}
        if g.get(n[1])==None:
            g[n[1]]={}    
        g[n[0]][n[1]] = n[2]
        g[n[1]][n[0]] = n[2]
        
    add_edge("CHI:NYC:719")
    add_edge("NYC:LA:2414")
    add_edge("NYC:SEATTLE:2448")
    add_edge("NYC:HAWAII:4924")
    add_edge("HAWAII:KTM:9024")
    
    longest = 0
    res = ""
    for key1,val1 in g.items():
        for key2,val2 in g.get(key1).items():
            if g.get(key2) is not None:
                for key3,val3 in g.get(key2).items():
                    if key1!=key2 and key1!=key3 and key2!=key3:
                        if longest < (int(val2)+int(val3)):
                            longest = int(val2)+int(val3)
                            res = (key1,key2,key3)
    temp = sorted(res)
    res = str(longest)+":"
    res+=":".join(temp)
    return "None" if res=='' else res                 
graph()
