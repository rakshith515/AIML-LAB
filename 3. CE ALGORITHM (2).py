import csv

with open("CandidateElimination.csv") as f:
    data = list(csv.reader(f))

    s = data[1][:-1]
    g = [['?' for i in range(len(s))] for j in range(len(s))]

    for i in data:
        if i[-1] == "Yes":
            for j in range(len(s)):
                if i[j]!=s[j]:
                    s[j] = '?'
                    g[j][j] = '?'
        
        elif i[-1] == "No":
            for j in range(len(s)):
                if i[j]!=s[j]:
                    g[j][j] = s[j]
                else:
                    g[j][j] = '?'

        print(f"iteration {data.index(i)+1} : \n")
        print(s)
        print(g)

    gh = []
    for i in g:
        for j in i:
            if j!='?':
                gh.append(i)
                break

    print("final Specific hypothesis : \n",s)
    print("final General Hypothesis : \n",gh)
