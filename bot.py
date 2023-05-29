import praw
import time

reddit = praw.Reddit(
    client_id="LZ_MGDYViwjw8YmW5mN0og",
    client_secret="5DvP2YYX3O50S5YiwyZKGfQ4V-at2A",
    user_agent="<console:south_asian_boy:1.0",
    username = 'southasian_bot_boy',
    password = "southasian_bot69",
)

subreddit = reddit.subreddit('2SouthAsian4you')

bot_comment = "this bot likes the word saar, thank you for using it"

for submission in subreddit.hot(limit=10):
    #print("*********************")
    #print(submission.title.encode("utf-8")) 

    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if "saar" in comment_lower: 
                print("----------------")
                print(comment.body.encode("utf-8"))
                comment.reply(bot_comment)
                time.sleep(600)
