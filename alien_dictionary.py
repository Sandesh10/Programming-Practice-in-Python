def alien_dictionary(words):
    if not words:
        return ""
    if len(words)==1:
        return ",".join([w for w in set(words[0])])
    
    adj_dict = build_graph(words)
    visit_dict = dict([(k,0) for k in adj_dict.keys()])
    res = []
    valid= True
    
    for c in adj_dict.keys():
        topo_sort(c,visit_dict, adj_dict, res)
    print(res)
        
def topo_sort(c,visit_dict, adj_dict,res):
    if not visit_dict[c]:
        visit_dict[c]=1
        for adj_c in adj_dict[c].keys():
            if visit_dict[adj_c]==1:
                return
            if not visit_dict[adj_c]:
                topo_sort(adj_c,visit_dict,adj_dict,res)
        visit_dict[c] = 2
        res.append(c)
    
def build_graph(words):
    graph_dict = {}
    
    def add_node(c):
        if graph_dict.get(c,None)== None:
            graph_dict[c]={}
    
    def add_link(src,des):
        graph_dict[src][des]= None
    
    for i in range(len(words)-1):
#         print(i, end="")
        w1= words[i]
        w2= words[i+1]
        start2 =0
        
        for j in range(min(len(w1), len(w2))):
            if w1[j]==w2[j]:
                add_node(w1[j])
            else:
                add_node(w1[j])
                add_node(w2[j])
                add_link(w2[j],w1[j])
                start2 = j+1
                break
#             print(graph_dict)    
        for j in range(start2, len(w1)):
            add_node(w1[j])
        for j in range(start2, len(w2)):
            add_node(w2[j])
#         print("-->",graph_dict)    
    return graph_dict
                
alien_dictionary([
  "wrt",
  "wsf",
  "er",
  "ett",
  "rftt"])
