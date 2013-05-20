import sys
import json
import re

def hw(sent_file,tweet_file):
    pattern = re.compile(r'\w+,\s([A-Z]{2})')
    stateScores = {}
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
      ##print scores.items() # Print every (term, score) pair in the dictionary
    
    
    tweet_lines = []
    tweetId=0 
    for line in tweet_file:
      tweetScore=0
      tweet = json.loads(line) 
      if tweet.get('lang','NA')<>'en':
        continue
      t_loc = tweet['user']['location']
      t_place_desc='NA'
      if 'place' not in tweet or tweet['place'] is None:
        continue        
      t_place = tweet['place']
      if t_place['country_code']<>'US':
        continue 
      if 'full_name' not in t_place or t_place['full_name'] is None :
        continue  
      t_place_desc = t_place['full_name']
      match = pattern.match(t_place_desc)
      if not match:
        continue
      state = match.group(1)
      ##agregar estado al mapa
      words = tweet['text'].split(" ")
      for word in words:
        wordScore = scores.get(word,0)
        tweetScore = tweetScore + wordScore
      tweetId = tweetId+1 
      ##sumarle el score
      if state not in stateScores:
        stateScores[state]={score:0}
      if 'score' not in stateScores[state]:
        stateScores[state]['score']=0
      stateScores[state]['score']=stateScores[state]['score']+tweetScore
      #if tweetScore <> 0:
       #print 'TWEET# '+str(tweetId) + ' score: '+ str(tweetScore) + ' state: '+state
    if 'US' in stateScores: 
     del stateScores['US']
    #for st in stateScores:
      #if stateScores[st]['score'] <> 0:
        #print st +' '+ '{0:.3f}'.format(stateScores[st]['score'])
    lista = sorted(stateScores, key = lambda stateScores:stateScores[1] )
    if len(lista)>0:
      print lista[0]      
    else: 
      print 'XX'
def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
