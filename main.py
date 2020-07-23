from helper import handler
import schedule
import tweet
import time
import data

dt = data.Data()
schedule.every(5).minutes.do(tweet.tweet_noti, dt)

while True:
    schedule.run_pending()
    time.sleep(1)