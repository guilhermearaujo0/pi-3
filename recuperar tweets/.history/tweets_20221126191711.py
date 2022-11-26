import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "#AFazenda14"
tweets = []
limit = 6336


for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.id, "2022-10-14 18:16:12", tweet.username, tweet.content,
                      tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount])

df = pd.DataFrame(tweets, columns=[
                  'ID', 'Date', 'User', 'Tweet', 'ReplyCount', 'RTCount', 'LikeCount', 'QuoteCount'])
print(df)
df['ID'] = df['ID'].astype(str)
# df['Date'] = df['Date'].astype(str).str[:-6]  // tweet.date
# to save to csv
df.to_excel('tweets14-10.xlsx')
# to save to csv
