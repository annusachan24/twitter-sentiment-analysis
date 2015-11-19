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
    total_pos_words=0
    total_neg_words=0
    count1=0
    count2=0 #just to match the count in robomongo and here
    for i in cur1[0].keys():
        print i
        if i!="_id":
            total_pos_words+=cur1[0][i]
            count1+=1
    for j in cur2[0].keys():
        if j!="_id":
            
            total_neg_words+=cur2[0][j]
            count2+=1
    
    print "@@@@@@@"
    print count1
    print count2
    print "@@@@@@@"
    print total_pos_words
    print total_neg_words
        
test()        
        
