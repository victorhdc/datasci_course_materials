import sys
import json

def hw(sent_file,tweet_file):
    positiveTag='pos'
    negativeTag='neg'
    totalTag='total'
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    newScores={}
    tweet_lines = []
    tweetId=0 
    for line in tweet_file:
      negTweet=False
      posTweet=False
      #tweet_lines.append(json.loads(line))
      tweet = json.loads(line)
      ##unicode_text = tweet['text']
      ##encoded_text = unicode_text.encode('utf-8') 
      text=tweet['text']
      tweetScore=0
      #print 'TWEET# '+str(tweetId+1)
      #print tweet['text']
      words = text.split(" ")
      wordId=0
      for word in words:
        #print 'WORD# ' + str(wordId+1)
        wordId = wordId+1
        if word in scores:
          wordScore = scores.get(word)
          negTweet = wordScore <0
          posTweet = wordScore >0
        else:
          wordScore= 0
          if word not in newScores:
            newScores[word]={positiveTag:0,negativeTag:0,totalTag:0}
          newScores[word][positiveTag] = newScores[word][positiveTag] + int(posTweet)
          newScores[word][negativeTag] = newScores[word][negativeTag] + int(negTweet)
          newScores[word][totalTag] = newScores[word][totalTag]+1 
        tweetScore = tweetScore + wordScore
        #print word+'score: '+str(wordScore)
      tweetId = tweetId+1 
      #print float(tweetScore)
    #print newScores
    for key in newScores:
      posCount=newScores[key][positiveTag]
      negCount=newScores[key][negativeTag]
      totalCount=newScores[key][totalTag]
      negRatio=float(negCount)/totalCount
      posRatio=float(posCount)/totalCount
      #-5 for 100% apperance in neg posts to +5 for 100% appearance on pos posts
      negValue=negRatio * -5
      posValue=posRatio * 5
      derivedScore= negValue+posValue
      #if (posCount>1 or negCount>1 ):
      #  print key+' pos: '+str(posCount)+' neg: '+str(negCount) +' total: '+str(totalCount)+' score:'+str(derivedScore)
      print key.encode('utf-8') +' '.encode('utf-8')+ '{0:.3f}'.format(derivedScore).encode('utf-8')
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
