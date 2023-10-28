import datetime
import pandas as pd
import tweepy as tw


def main():
    consumer_key = 'zMhqRupnzViKtKTKW7hY0DY4R'
    consumer_secret = 'OWVHDn8NitkGms81s0UsP30hHidGnT6mCVvWjTId831YWO83r0'
    access_token = '1458945878866202624-8utD3dWYPUSiU7yAmPRWJheWNxFMW4'
    access_token_secret = 'jPhf9M890DEz7W5bt24AgyCxWJfbE1F29tX9yQBVnfKfK'
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, timeout=3000)
    #places = api.search_geo(query="Canada", granularity="country")
    #place_id = places[0].id
    keywords = "COVID OR vaccination OR Pfizer OR Moderna OR vaccine" \
               " AND since:2021-11-23 AND until:2021-11-26" + " -filter:retweets -filter:links"
               #"AND place:" + place_id
    start_date = datetime.datetime(2021, 11, 26, 23, 00, 00)
    end_date = datetime.datetime(2021, 11, 26, 23, 00, 00)
    cursor = tw.Cursor(api.search_tweets, q=keywords, lang="en", tweet_mode="extended", result_type='mixed', count=25).items(1000)

    topic = []
    text = []
    sentiment = []
    time = []
    for i in cursor:
        t = i.full_text
        text.append(t)
        if t.find("vaccine") + t.find("vaccination") + t.find("pfizer") + t.find("moderna") != -4:
            topic.append("v")
        else:
            topic.append("c")
        sentiment.append("n")
        time.append(i.created_at)

    df = pd.DataFrame({"topic": topic, "sentiment": sentiment, "time": time, "text": text})
    df.to_csv("C:\\Users\\admin\Python\COMP598\FinalProject\data3.tsv", sep="\t")


if __name__ == '__main__':
    main()