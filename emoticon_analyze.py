import re


#parse the tweet for emoticons and decide the positivity and negativity on a scale of 1-10 above 5 means positive with 10 being most strong positive
#below 5 means negative emotion with 1 being most negative
happy=r':-\)|:\)|:o\)|:]|:3|:c\)|:>|=]|8\)|=\)|:}|:\^\)|っ\)'
laugh=r':-D|:D|8-D|8D|x-D|xD|X-D|XD|=-D|=D|=-3|=3|B\^D'
veryhappy=r':-\)\)'
sad=r'>:\[|:-\(|:\(|:-c|:c|:-<|:っC|:<|:-\[|:\[|:\{'
winky=r';\('  #bit of sarcasam difficult to analyse
angry=r':-\|\||:@|>:\('
crying=r':\'-\(|:\'\('
tears_of_happiness=r':\'-\)|:\'\)'
horror=r'D:<|D:|D8|D;|D=|DX|v\.v|D-\':'
surprise=r'>:O|:-O|:O|:-o|:o|8-0|O_O|o-o|O_o|o_O|o_o|O-O'
kiss=r':\*|:\^\*|\(|\'}\{\'|\)'
wink=r';-\)|;\)|\*-\)|\*\)|;-]|;]|;D|;\^\)|:-,'
cheeky=r'>:P|:-P|:P|X-P|x-p|xp|XP|:-p|:p|=p|:-Þ|:Þ|:þ|:-þ|:-b|:b|d:'
skeptical=r'>:\\|>:/|:-/|:-\.|:/|:\\|=/|=\\|:L|=L|:S|>\.<' #doubtful
no_expression=r':\||:-\|'
embarrased=r':\$'
sealed_lips=r':-X|:X|:-#|:#'
angel=r'O:-\)|0:-3|0:3|0:-\)|0:\)|0;\^\)'     #angel,saint or innocent
evil=r'>:\)|>;\)|>:-\)'
devilish=r'}:-\)|}:\)|3:-\)|3:\)'
highfive=r'o/\\o|\^5|>_>\^|\^<_<'
bored=r'\|;-\)|\|-O'
speechless=r':-&|:&'
partied_all_night=r'#-\)'
drunk=r'%-\)|%\)'   #confused
being_sick=r':-###\.\.|:###\.\.'
dumb=r'<:-\|'
disapproval=r'ಠ_ಠ'
fishy=r'<\*\)\)\)-\{|><\(\(\(\*>|><>'   #doubt or suspicion
cheer=r'\\o/'
cheerleader=r'\*\\0/\*'
rose=r'@}-;-\'---|@>-->--'
heart=r'<3'
broken_heart=r'</3'





def analyze_emoticon(words):
    pos_score=0
    neg_score=0
    emotional_value=[]
    for tweet in words:
        if re.search(happy,tweet):
            pos_score+=8
        if re.search(laugh,tweet):
            pos_score+=9
        if re.search(veryhappy,tweet):
            pos_score+=9
        if re.search(sad,tweet):
            neg_score+=8
        if re.search(winky,tweet):    #sarcasm check its value
            pos_score+=2
            neg_score+=4
        if re.search(angry,tweet):
            neg_score+=7
        if re.search(crying,tweet):
            neg_score+=8
        if re.search(tears_of_happiness,tweet):
            pos_score+=8
        if re.search(horror,tweet):
            neg_score+=8
        if re.search(surprise,tweet):
            pos_score+=3
            neg_score+=2
        if re.search(kiss,tweet):
            pos_score+=7
        if re.search(wink,tweet):
            pos_score+=7
        if re.search(cheeky,tweet):
            pos_score+=7
        if re.search(skeptical,tweet):
            neg_score+=7
        if re.search(no_expression,tweet):
            pos_score+=1
            neg_score+=1
        if re.search(embarrased,tweet):
            neg_score+=5
        if re.search(sealed_lips,tweet):
            pos_score+=4
            neg_score+=3
        if re.search(angel,tweet):
            pos_score+=7
        if re.search(evil,tweet):
            neg_score+=7
        if re.search(devilish,tweet):
            neg_score+=7
        if re.search(highfive,tweet):
            pos_score+=7
        if re.search(bored,tweet):
            neg_score+=6
        if re.search(speechless,tweet):
            pos_score+=4
            neg_score+=2
        if re.search(partied_all_night,tweet):
            pos_score+=5
        if re.search(drunk,tweet):
            neg_score+=4
            pos_score+=3
        if re.search(being_sick,tweet):
            neg_score+=7
        if re.search(dumb,tweet):
            neg_score+=2
        if re.search(disapproval,tweet):
            neg_score+=5
        if re.search(fishy,tweet):
            neg_score+=4
        if re.search(cheer,tweet):
            pos_score+=7
        if re.search(cheerleader,tweet):
            pos_score+=7
        if re.search(rose,tweet):
            pos_score+=8
        if re.search(heart,tweet):
            pos_score+=8
        if re.search(broken_heart,tweet):                           #check its value
            neg_score+=6

    pos_score=pos_score*100000
    neg_score=neg_score*100000
    
    emotional_value.append(pos_score)
    emotional_value.append(neg_score)

    return emotional_value

    
        

