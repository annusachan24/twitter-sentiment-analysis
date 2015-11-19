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

def is_nonword(word):
    if word.startswith('@'):
        return 1
    if word.startswith('http'):
        return 1
    if re.search(r'[0-9]{2,4}',word): #qwerty {2,4} why? its enough :D
        return 1
    
def standardize_stem(word_list):
    from nltk import stem
    word_list=[''.join(c for c in word if c.isalpha()) for word in word_list if not is_nonword(word)]
    word_list = nltk.pos_tag(word_list)
    #pprint.pprint( word_list)
    word_list=[word for (word,tag) in word_list if tag not in['NN','CD','MD','IN','DT','CC','PRP']]# DT for determiner and CC for conjunctions.
    snowball = stem.snowball.EnglishStemmer()
    #word_list=[snowball.stem(word) for word in word_list] when used result=[u'the', u'was', u'awesom', ''] when not used ['the', 'was', 'awesome', '']
    #pprint.pprint( word_list)
    i=0
    for word in word_list:
        word_list[i]=removing_redundant_letters.extra_occ(word)
        i+=1
    #print word_list
    return word_list    
        
    

#Reads the csv training data , produces list of tokenized tweets words and its emotion
def read_csv_tweets(filename):
    op_list=[]
    pos_docs=0
    neg_docs=0
    i=0
    with open(filename,'r') as f:
      for line in f:
            if i>1600000:
                break
            if i>1500000:
                line=line.strip('\n')
                part=csv.reader(line)
                j=0
                for key in part:
                      #print key
                    if j==0:
                        value=key
                    j+=1
              
                #print key
                key[0]=key[0].strip(']').strip('[').strip('\'').strip(' ')
                #print key[0]      
                #part=[p.strip("\"").strip("\"") for p in line.strip("\n").split(",")] #qwerty remove ' and tc of abbr^n
                #print part[5]
                w_list=[ele.lower() for ele in key[0].strip("\"").split() if len(ele)>=2]# ntng indise split fn means split on the basis of space
              
                #print w_list
                w_list=standardize_stem(w_list)
                if value[0]=='0':
                    op_list.append(('negative1',w_list))
                    neg_docs+=1
                else:
                    op_list.append(('positive1',w_list))
                    pos_docs+=1
            
            i+=1
                #print i
    print "no of positive documents"
    print pos_docs
    print "no of negative documents"
    print neg_docs
    return op_list

def get_db(db_name):
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db


# inserted in a collection , postivie or negative in format {word1:count1 , word2:count2.....}    
def insert_db(db_name,coll_name,word):
  try:
    coll=db_name[coll_name]
    if coll.count() == 0:
        dict_e={}
        coll.insert(dict_e)
        

    coll.update(  { },
                  {"$inc":{word:1}
                   }                  
                  )
    print "Success!inserted {0} into {1}".format(word,coll_name)
    return 0
  except :
    print "Oops!could not inserted {0} into {1}".format(word,coll_name)
    return 1
   
    

    
    
def train():
    list_0=read_csv_tweets('trainingProcessed.csv')
    #pprint.pprint(list_0)
    db=get_db('sentiments1')
    fail_count=0
    for (emotion,w_list) in list_0:
        for word in w_list:
            fail_count+=insert_db(db,emotion,word)
             
    print "failed to insert {0} words".format(fail_count)

#train() 

def addab():
    pos_abv=['AAMOF','AFAIK','ASAP','BBL','BRB','CUL8R','CYA','EZ','REHI','ROFL','ROTF','ROTFL','SOL','TY','YW','HAND','HHOK','HTH','IMO','JK','LMFAO','LTNS','NTK','L8R']
    neg_abv=['PITA','PSTFU','RUOK','WEG','WTF','H8','IDGI','L8R','NTK','ONNA','IDC','IDN']
    db=get_db('sentiments1')
    for word in pos_abv:
        ans=insert_db(db,'positive1',word)
        #print ans
    for word in neg_abv:
        ans1=insert_db(db,'negative1',word)
        #print ans1

#addab()


def test(string):
    
    #print "INPUT"
    #t=input()
    #while t>0:
    #string=raw_input()
    w_list=nltk.word_tokenize(string)
    #print w_list
    w_list=standardize_stem(w_list)
    #print w_list
    emoticon=emoticon_analyze.analyze_emoticon(w_list)
    #print emoticon        #'string' is the input tweet
    
    if abs(emoticon[0]-emoticon[1])!=0:
        if emoticon[0]>emoticon[1]:
            #print "the sentence is positive sensed"
            return 4
        else:
            #print "the sentence is negative sensed"
            return 0
                
    #print "going to analyse using db"
    if 1:
            
        db=get_db('sentiments1')
        cur1=db.positive1.find()
        cur2=db.negative1.find()


        """" pos_words=len(cur1[0])
        neg_words=len(cur2[0])
        print "the value of cur1 is as follows:"
        print cur1
        print "the value of cur2 is as follows:"
        print cur2
        print "*******************"
        print pos_words   #total no of distinct words i.e., vocabulary of positive collections
        print neg_words   #total no of distinct words i.e., vocabulary of negative collections
        print "************************"
        """
        vocabulary=187443
        #print vocabulary
        total_pos_words=4101280
        total_neg_words=4617389
        """ for i in cur1[0].keys():
              if i!="_id":
                total_pos_words+=cur1[0][i]
                print i
            for i in cur2[0].keys():
                if i!="_id":
                    total_neg_words+=cur2[0][i]
                    print i
            print "#####################"
            print total_pos_words
            print total_neg_words
            print "#########################"
            """    

            

            
        pos_prob=1.0
        neg_prob=1.0
        for word in w_list:
                count_pos=1
                count_neg=1
                if word in cur1[0].keys():
                    count_pos+=int(cur1[0][word])
                    #print "{} pos {}".format(word,cur1[0][word])
                prob_word_pos=float(count_pos)/float(total_pos_words+vocabulary)
                #print prob_word_pos
                pos_prob*=prob_word_pos
                if word in cur2[0].keys():
                    count_neg+=int(cur2[0][word])
                    #print "{} neg {}".format(word,cur2[0][word])
                prob_word_neg=float(count_neg)/float(total_neg_words+vocabulary)
                #print prob_word_neg
                neg_prob*=prob_word_neg
                   
        pos_prob=pos_prob*0.5
        neg_prob=neg_prob*0.5 
       
        if pos_prob>neg_prob:
            #print "the sentence is positive sensed"
            return 4
        elif pos_prob<neg_prob:
            #print "the sentence is negative sensed"
            return 0
        #else:
            #print "the sentence is neutral"
#test()        
        
         
            
            
          
    
