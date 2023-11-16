from collections import Counter
import math
import pandas as pd

df = pd.read_csv("PlayTennis.csv")
print(len(df))
print(df)

def entropy(ls):
    counts = Counter(x for x in ls)
    total = len(ls)
    probs = (x/total for x in counts.values())
    E = sum(-p*math.log(p,2) for p in probs)
    return E


dfs = df.groupby('PlayTennis')
for k,v in dfs:
    print(v)


def inf_gain(data,a,target):
    df_split = df.groupby(a)
    n = len(data)
    df_agg = df_split.agg({target:[entropy,lambda x : len(x)/n]})[target]
    df_agg.columns = ['Entropy','Proportion']
    new_E = sum(df_agg['Entropy']*df_agg['Proportion'])
    old_E = entropy(df[target])
    return old_E-new_E

def id3(df,target,attr,def_class = None,def_attr = "S"):
    pn = Counter(x for x in df[target])
    print(f'\n **{pn}**')

    if len(pn)==1:
        return next(iter(pn))
    elif df.empty or (not attr):
        return def_class
    else:
        def_class = max(pn,key=pn.get)
        print(f'Default class {def_class}')
        gains = {}
        for a in attr:
            gains[a] = inf_gain(df,a,target)
            print(f"Inf gain on {a} : {gains[a]}")

        best = max(gains,key=gains.get)
        print(f"\nBest attribute is {best}")

        tree = {best : {}}
        attr.remove(best)

        for av,data in df.groupby(best):
            subtree = id3(data,target,attr,def_class,best)
            tree[best][av] = subtree
            print(f"best {best} {av}")
            print(tree)
    return tree

attr = list(df.columns)
attr.remove('PlayTennis')
print("Predicting Attribute : ",attr)
tree = id3(df,'PlayTennis',attr)


from pprint import pprint
print("Tree \n")
pprint(tree)
ba = next(iter(tree))
print("Best Attribute : ",ba)
print("Tree Keys : ",tree[ba].keys())
