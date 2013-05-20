import sys
import json

def hw(sent_file,tweet_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
      ##print scores.items() # Print every (term, score) pair in the dictionary
    
    
    tweet_lines = []
    tweetId=0 
    for line in tweet_file:
      #tweet_lines.append(json.loads(line))
      tweet = json.loads(line) 
      tweetScore=0
      #print 'TWEET# '+str(tweetId+1)
      #print tweet['text']
      words = tweet['text'].split(" ")
      wordId=0
      for word in words:
        #print 'WORD# ' + str(wordId+1)
        wordId = wordId+1
        wordScore = scores.get(word,0)
        tweetScore = tweetScore + wordScore
        #print word+'score: '+str(wordScore)
      tweetId = tweetId+1 
      print float(tweetScore)

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
