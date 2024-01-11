import csv

with open('/content/CandidateElimination.csv') as f:

    data = list(csv.reader(f))

    s = data[1][:-1]
    g = [['?' for i in range(len(s))] for j in range(len(s))]
    for i in data:
        if i[-1] == "Yes":
            for j in range(len(s)):
                if i[j] != s[j]:
                    s[j] = '?'
                    g[j][j] = '?'

        elif i[-1] =='No':
            for j in range(len(s)):
                if i[j]!=s[j]:
                    g[j][j] = s[j]
                else:
                    g[j][j] = '?'
        print("\n steps of CE algorithm",data.index(i)+1)
        print(s)
        print(g)

    gh = []
    for i in g:
        for j in i:
            if j!='?':
                gh.append(i)
                break
    print("\n final specific hypothesis:\n",s)
    print("\n final general hypothesis:\n",gh)
