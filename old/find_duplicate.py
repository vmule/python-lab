list = [3,5,6,4,6,7,4,6,0,0,0,6,0,0]

# Remove duplicates
seen = set()
uniq = []
dups = []

for i in list:
    if i not in seen:
        seen.add(i)
        uniq.append(i)
    if list.count(i) > 1 and i not in dups:
        dups.append(i)

print(uniq)
print(dups)

adict = {}

for i in list:
    if i in adict:
        adict[i] += 1
    else:
        adict[i] = 1

dupes2 = []
for k,v in adict.items():
    if v > 1:
        dupes2.append(k)

print(adict)
print(dupes2)
