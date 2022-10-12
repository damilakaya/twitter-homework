from dataclasses import fields
from inspect import Attribute
import psycopg2
import json

#example data 
tweets = {
    "data": [
        {
            "author_id": "1460431590455414785",
            "created_at": "2022-10-12T03:51:16.000Z",
            "edit_history_tweet_ids": [
                "1580043398974562304"
            ],
            "id": "1580043398974562304",
            "text": "#ApplicationReceived\n#TwitterAPI\nI applied for being a #TwitterDev and my #ApplicationReceived! I hope I get approved. https://t.co/b1LsOs6KUE"
        },
        {
            "author_id": "1059961925948317702",
            "created_at": "2022-10-12T03:22:25.000Z",
            "edit_history_tweet_ids": [
                "1580036138106245120"
            ],
            "id": "1580036138106245120",
            "text": "RT @_kato_shinya: #twitter_api_v2 is ready to take things to the next level. This library can be even more amazing :)\n\n#Programming #Dart #\u2026"
        }
    ],
    "meta": {
        "newest_id": "1580043398974562304",
        "next_token": "b26v89c19zqg8o3fpzbnghhnda90fpk3ewclrfxhr24xp",
        "oldest_id": "1579415477969096704",
        "result_count": 10
    }
}

tweets_data = tweets["data"]
print(tweets_data)


try:
    connect = psycopg2.connect(
        database="content", user="postgres", password="12345", host="127.0.0.1", port = "5433"
    )

except:
    print("error")


def addTweetsIntoDB(tweets):
    fields = ['id', 'text', 'created_at', 'author_id']
    global connect
    cur = connect.cursor()


    for tweet in tweets:
        attributes = list(int(tweet["id"]), tweet["text"], tweet["created_at"], tweet["author_id"])
        insert_query = "INSERT INTO Tweet VALUES (%d, %s, %s, %s)"
        cur.execute(insert_query, tuple(attributes))
        connect.commit()

    
    cur.close()

   
    connect.close()

#main

addTweetsIntoDB(tweets)