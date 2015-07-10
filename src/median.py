f = open ('tweets.txt','r')
from array import array
i = 1
x = array('i')
z = array('f')
for line in f:
    words = line.split()
    unique_words = 0
    counts = dict()
    for word in words:
        counts[word] = counts.get(word,0) + 1
    x.append(len(counts))
    y = sorted(x)
    if i % 2 == 0:
        temp1 = y[(i/2)-1]
        temp2 = y[i/2]
        median = (temp1 + temp2)*0.5
        z.append(median)
    else:
        temp3 = y[((i+1)/2)-1]
        z.append(temp3)
    i = i + 1        

print z
f.close()
