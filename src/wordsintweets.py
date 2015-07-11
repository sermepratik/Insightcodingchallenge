handle = open ('tweets.txt','r')    #open file in reading mode
op=open('wordsop.txt','w')          #open output file for feature 1
text = handle.read()                #read the contents
words_total = text.split()          #split the lines
counts_total = dict()               #initialize dictionary

for word in words_total:
    counts_total[word] = counts_total.get(word,0) + 1
    #get count of all the words
for w in sorted(counts_total, key=counts_total.get(0), reverse=False):
    #sort in alphabetical order
    op.writelines(w+'\t'+'\t'+'\t'+'\t'+'\t'+str(counts_total[w])+'\n')
    #write to output file

handle.close()                      #close the input file to free up resources
op.close()                          #close the output file to free up resources
