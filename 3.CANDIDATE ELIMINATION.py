def g_o(n):
    return ("?")*n
def s_o(n):
    return ("0")*n

def more_general(h1,h2):
    more_general_parts = []
    for x,y in zip(h1,h2):
        mg = x=="?" or (x!="0" and (x==y or y=="0"))
        more_general_parts.append(mg)

    return all(more_general_parts)
    
def fulfills(example,hypothesis):
    return more_general(hypothesis,example)

def min_generalization(h,x):
    h_new = list(h)
    for i in range(len(h)):
        if not fulfills(x[i:i+1],[h[i:i+1]]):
            h_new = "?" if h[i]!="0" else x[i]
        return tuple(h_new)

min_generalization(h=("0","0","sunny"),x=("rainy","windy","cloudy"))

def min_specializations(h,domains,x):
    results = []
    for i in range(len(h)):
        if h[i]=="?":
            for val in domains[i]:
                if x[i]!=val:
                    h_new = h[i]+(val,)+h[i+1:]
                    results.append(h_new)
        elif h[i]!="0":
            h_new = h[:i]+("0",)+h[i+1:]
            results.append(h_new)
    return results

min_specializations(h=("?","x"),domains=[["a","b","c"],["x","y"]],x=["b","x"])

import csv
with open('CandidateElimination.csv') as csvFile:
    examples = [tuple(line)[0:] for line in csv.reader(csvFile)]
examples = examples[1:]

def get_domains(examples):
    d = [set() for i in examples[0]]
    for x in examples:
        for i,xi in enumerate(x):
            d[i].add(xi)
        return [list(sorted(x)) for x in d]

get_domains(exapmles)

def generalize(x,G,s):
    s_prev = list(s)
    for S in s_prev:
        if S not in s:
            continue 
        if not fulfills(x,S):
            s.remove(S)
            splus = min_generalization(S,x)
            s.update([h for h in splus if any([more_general(g,h) for g in G])])
            s.difference_update([h for h in s if any([more_general(h,h1) for h1 in s if h!=h1])])
    return s

def specialize(x,G,s):
    G_prev = list(G)
    for g in G_prev:
        if g not in G:
            continue 
        if not fulfills(x,g):
            G.remove(S)
            Gminus = min_generalization(g,x)
            G.update([h for h in Gminus if any([more_general(h,s) for S in s])])
            G.difference_update([h for h in G if any([more_general(h,h1) for h1 in G if h!=h1])])
    return G
