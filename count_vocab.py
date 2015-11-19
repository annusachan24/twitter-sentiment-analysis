import twitter
import nltk
from pymongo import MongoClient
import pprint
import csv
import re
import removing_redundant_letters
import emoticon_analyze
#Stems the words in a given list using poeters algorithm and removes all nouns and proper nouns
#normalize words like 'city...' , 'ball.' , 'premiere?!', '@iamlilnicki'  , 'too!!!!','(gmt+1)' i.e strip all non alphabets
#remove urls , datetimes , integers


        
    


def get_db(db_name):
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db



   
    

    
    



def test():
    db=get_db('sentiments1')
    cur1=db.positive1.find()
    cur2=db.negative1.find()
    intersection=0
    positive_vocab=121824
    negative_vocab=111857
    for i in cur1[0].keys():
        if i in cur2[0].keys():
            intersection+=1
            print i
    print intersection
    print
        
test()        
        
         
            
            
          
    
