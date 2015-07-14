"""
Created on Tue Jul 14 00:40:18 2015

@author: Pratik
This code will count words in txt file 
"""
wordcount = {}    
colwidth = 0
with open("tweets.txt","r") as fileinput:
    for word in fileinput.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] = wordcount[word] + 1
        colwidth = max(len(word),colwidth)
            
with open("newoutputspyder.txt","w") as fileoutput:
        for word in sorted(wordcount):
            print>>fileoutput, "".join(word.ljust(colwidth)),"\t\t",wordcount[word]
            
