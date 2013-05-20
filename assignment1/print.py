import urllib
import json

##set number of pages
maxPages = 1
startPage=1
currPage=1
while currPage <= maxPages:
  ##search an

  tweets = resp_obj['results']
  print resp_obj['results'][0].keys()
  numTweets= len(tweets)
  for currTweetId in range(0,2,1):
    ##extract text from json object
    unicode_text = tweets[currTweetId]['text']
    encoded_text = unicode_text.encode('utf-8')
    print 'TWEET #'+str(currTweetId)
    print encoded_text
  currPage= currPage+1
