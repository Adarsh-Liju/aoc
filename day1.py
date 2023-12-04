# Part 1
with open('day1.txt','r') as fp:
    fc=fp.readlines()
res = []
for i in fc:
    res.append(''.join(filter(str.isdigit, i)))
i=0
for i in range(len(res)):
    if len(res[i]) != 2:
        res[i] = res[i][0] + res[i][-1]
    res[i]=int(res[i])
print(sum(res))

# Part 2
