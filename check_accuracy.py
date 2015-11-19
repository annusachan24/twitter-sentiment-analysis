import sentiment_analysis_final1
import twitter
import nltk
from pymongo import MongoClient
import pprint
import csv
import re
import removing_redundant_letters
import emoticon_analyze




def check_accuracy():
    correct=0
    wrong=0
    times=0
    with open('trainingProcessed.csv','r') as f:
        for line in f:
              if times>1000:
                  break;
              
              line=line.strip('\n')
              print line
              part=csv.reader(line)
              j=0
              for key in part:
                  #print key
                  if j==0:
                      value=key
                  j+=1
              print value[0]
              print key
              key[0]=key[0].strip(']').strip('[').strip('\'').strip(' ')
              print key[0]
              result=sentiment_analysis_final1.test(key[0])
              print result
              if result==int(value[0]):
                  correct+=1
              else:
                  wrong+=1
              times+=1
        print correct
        print wrong

        print correct*1.0/(correct+wrong)
check_accuracy()
            
    
