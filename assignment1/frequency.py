import sys
import json

def hw(tweet_file):
    totalTag='total'
    tweet_lines = []
    tweetId=0
    globalWordCount = 0
    wordDict = {}
    for line in tweet_file:
      tweet = json.loads(line) 
      #print 'TWEET# '+str(tweetId+1)
      #print tweet['text']
      text = tweet['text'].replace('\n','')
      words = text.split(" ")
      wordId=0
      for word in words:
        if word.strip()=='' or word.strip()=='I\'ll':
          continue
        #print 'WORD# ' + str(wordId+1)
        if word not in wordDict:
            wordDict[word]={totalTag:0}
        wordDict[word][totalTag] = wordDict[word][totalTag]+1 
        globalWordCount = globalWordCount + 1
        wordId= wordId+1
      tweetId = tweetId+1 
      #print float(tweetScore)
    #del wordDict['I''ll']
    for key in wordDict:
      totalCount=wordDict[key][totalTag]
      wordFreq = float(totalCount) / globalWordCount
      print key.encode('utf-8') +'  '.encode('utf-8')+ '{0:.3f}'.format(wordFreq).encode('utf-8')
      #print 'cosa 0.0004'
     
def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
