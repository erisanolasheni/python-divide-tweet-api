import twitter
import json
import sys
import os

try:
    with open(os.path.join(os.getcwd(), "Interview-2/keys.json"), "r") as keys:
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
keyword = '#'+keyword

print(keyword)

# fetch the results containing the #hastag
tweet_results = api.GetStreamSample()

# loop through the filtered results and print data
for twt_objects in tweet_results:
    try:
        # filter results containing the #hastag
        if keyword in twt_objects['text']:
            print("Returning tweets:\n")
            print(twt_objects['created_at'])
            print(twt_objects['text'])
        else:
            print('...----Hashtag Not Found------....')
    except:
        pass
else:
    print('No tweet found!')
