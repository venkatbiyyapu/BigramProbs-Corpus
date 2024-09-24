import sys
import pandas as pd
from collections import Counter

def getProbability(sentence_list,df_probs):
    probability=1
    prob_set=list(zip(sentence_list,sentence_list[1:]))
    for i in prob_set:
        df= df_probs.loc[~df_probs.index.duplicated(),~df_probs.columns.duplicated()].copy()
        probability*=df.loc[i[0],i[1]]
    return probability
# pd.set_option('display.max_columns', None)
with open('corpus.txt') as f:
    l=f.read()
x=[]
list_corpus=l.split()
count_=0
for i in l.split("\n"):
    i="<s> "+i+" </s>"
    words_list=i.split()
    count_+=1
    x.extend(list(zip(words_list,words_list[1:])))
set_corpus=set(list_corpus)
word_count_dict={i : list_corpus.count(i) for i in set_corpus}
vocab_len=len(set_corpus)
corpus_dict= Counter(x)
word_count_dict['<s>']=count_
word_count_dict['</s>']=count_


with open('test.txt') as f:
    sentence_list=f.readlines()
option=int(sys.argv[-1])
sys.stdout = open("output_{}.txt".format(option), "w")
for sentence in sentence_list:
    bg_=[]
    sentence_=sentence.split()
    sentence_.insert(0,"<s>")
    sentence_.insert(len(sentence_),"</s>")
    df_counts=pd.DataFrame(columns=sentence_,index=sentence_)
    df_probs=pd.DataFrame(columns=sentence_,index=sentence_)
    for i in sentence_:
        for j in sentence_:
            bg_.append((i,j))
    
    if option==0:
        for bigram in bg_:
            counts_= corpus_dict[bigram]
            df_counts.loc[bigram[0],bigram[1]]=counts_
            prob=corpus_dict[bigram]/word_count_dict[bigram[0]]
            df_probs.loc[bigram[0],bigram[1]]=prob
        print(sentence+"\n")
        print("Bigram Counts : \n")
        print(df_counts,"\n")
        print("Bigram Probabilities : \n")
        print(df_probs,"\n")
        print("Probablity of the Sentence : ",getProbability(sentence_,df_probs))
        print("########################################################################################################################################################################################################\n")
        
    
    if option==1:
        for bigram in bg_:
            counts_= corpus_dict[bigram]
            df_counts.loc[bigram[0],bigram[1]]=counts_
            prob=(corpus_dict[bigram]+1) /(word_count_dict[bigram[0]]+vocab_len)
            df_probs.loc[bigram[0],bigram[1]]=prob

        print(sentence+"\n")
        print("Bigram Counts : \n")
        print(df_counts,"\n")
        print("Bigram Probabilities : \n")
        print(df_probs,"\n")
        print("Probablity of the Sentence : ",getProbability(sentence_,df_probs))
        print("########################################################################################################################################################################################################\n")



sys.stdout.close()









