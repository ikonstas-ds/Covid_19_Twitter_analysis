import urllib.request
from bs4 import BeautifulSoup

def getTweetTextAndLocation(row):

    # print(row.tweet_id)
    # print(tweet_id)
    url = 'https://twitter.com/i/web/status/' + str(row.loc['tweet_id'])

    try:
        page = urllib.request.urlopen(url)
    except:
        return "", "", "", "", "0", "0", "0"

    soup = BeautifulSoup(page, 'html.parser')

    results = soup.find('div', class_='js-tweet-text-container')

    if results:
        tweet_text = results.text.strip()
        lang = results.find('p', class_='TweetTextSize TweetTextSize--jumbo js-tweet-text tweet-text')
        if lang:
            lang = lang.attrs.get('lang')
        else:
            lang = ""
    else:
        return "", "", "", "", "0", "0", "0"

    location = soup.find('div', class_='ProfileHeaderCard-location ')
    if location:
        location_text = location.text.strip()
        location_id = location.find('a')
        if location_id:
            location_id = location_id.attrs.get('data-place-id')
        else:
            location_id = ""
    else:
        location_text = ""
        location_id = ""

    reactions = soup.find('div', class_='ProfileTweet-actionCountList u-hiddenVisually')
    if reactions:
        replies = reactions.find('span', class_='ProfileTweet-action--reply u-hiddenVisually')
        replies_text = replies.text.strip().replace(',', '').split()[0]

        retweets = reactions.find('span', class_='ProfileTweet-action--retweet u-hiddenVisually')
        retweets_text = retweets.text.strip().replace(',', '').split()[0]

        likes = reactions.find('span', class_='ProfileTweet-action--favorite u-hiddenVisually')
        likes_text = likes.text.strip().replace(',', '').split()[0]
    else:
        replies_text, retweets_text, likes_text = "0", "0", "0"

    a = tweet_text, lang, location_id, location_text, replies_text, retweets_text, likes_text

    return a
