f = open ('tweets.txt','r')         #open file in reading mode
output = open ('median.txt','w')    #open output file for feature 2
from array import array             #array used

i = 1                               #line number 
x = array('i')
z = []                              #median output, initially empty list

for line in f:
    #count the number of words in each tweet
    words = line.split()
    unique_words = 0
    counts = dict()
    for word in words:
        counts[word] = counts.get(word,0) + 1
    #get the length of the words and sort them in alphabetical order
    x.append(len(counts))
    y = sorted(x)
    #calculate the median
    #line by line
    if i % 2 == 0:
        #get the middle two elements if word count is even
        #and then multiply by 0.5 to get median
        temp1 = y[(i/2)-1]
        temp2 = y[i/2]
        median = (temp1 + temp2)*0.5
        z.append(median)
        output.write(str(median)+'\n')
    else:
        #get the middle element as median since word count is odd
        temp3 = y[((i+1)/2)-1]
        z.append(temp3)
        output.write(str(temp3)+'\n')
    i = i + 1        

f.close()                           #close the input file to free up resources
output.close()                      #close the output file to free up resources
