import twitter
import json
import sys
import re
import os

try:
    with open(os.path.join(os.getcwd(),"Interview-2/keys.json"), "r") as keys:
        creds = json.load(keys)
except:
    print('please ensure a proper provision of your API credentials keys.json')
    sys.exit(0)

# Auth the API
api = twitter.Api(consumer_key=creds['consumer_key'],
                  consumer_secret=creds['consumer_secret'],
                  access_token_key=creds['access_token_key'],
                  access_token_secret=creds['access_token_secret'])


# Get raw inputs from your
keyword = str(input('Please provide a hashag keyword to search for:\n'))

keyword = keyword.strip('#')

# fetch the results containing the #hastag
tweet_results = api.GetStreamSample(stall_warnings=True)

print(len(list(tweet_results)[:5]))

# filter results containing the #hastag
search_tag = re.compile(r'#{}'.format(keyword),re.I|re.M)
filtered_results = list(filter(list(tweet_results), lambda x: search_tag.search(x['text'])))

# loop through the filtered results and print data

if not len(filtered_results):
    print('No tweet found in this hashtag')
else:
    for twt_objects in filtered_results:
        print("Returning tweets:\n")
        print(twt_objects['created_at'])
        print(twt_objects['text'])
