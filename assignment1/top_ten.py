import json
import sys
import operator
def hw(tweet_file):
  tweetId=0
  htag_freq = {}
  for line in tweet_file:
    tweet = json.loads(line)
    #print 'TWEET# '+str(tweetId+1),
    if 'entities' in tweet and 'hashtags' in tweet['entities'] and len(tweet['entities']['hashtags'])>0:
      htags = tweet['entities']['hashtags'] 
      for htag in htags:
        tag=htag['text']
        #print tag,
        if tag not in htag_freq:
          htag_freq[tag]={'freq':0.0}
        htag_freq[tag]['freq']=htag_freq[tag]['freq']+1
    #print  
    tweetId=tweetId+1
  sortedHashTags = sorted(htag_freq.iteritems(),key=operator.itemgetter(1))
  size = len(sortedHashTags)
  for i in range (size-10,size,1):
    print sortedHashTags[i][0].encode('utf-8') + ' ' +str(sortedHashTags[i][1]['freq'])
    #print sortedHashTags[len(sortedHashTags)-1][0]
  #for htag in htag_freq:
    #freq=htag_freq[htag]['freq']
    #if freq>1:
      #print htag+' '+str(freq)
def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()  
