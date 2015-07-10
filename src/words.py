handle = open ('tweets.txt','r') #handler
text = handle.read() #read the contents
words_total = text.split() #split the lines
counts_total = dict() #initialize dictionary 
for word in words_total:
    counts_total[word] = counts_total.get(word,0) + 1
for w in sorted(counts_total, key=counts_total.get(0), reverse=False):
  print w, counts_total[w]
print '\n'
handle.close()
