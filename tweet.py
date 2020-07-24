from win10toast import ToastNotifier
from helper import handler
import twitter
import time
import config
"""
You need to make config.py
ex) config.py
twitter_consumer_key = {$Your_twitter_Consumer_Keys}
twitter_consumer_secret = {$Your_twitter_Consumer_Secret}
twitter_access_token = {$Your_twitter_Access_token}
twitter_acess_secret = {$Your_twitter_Access_secret}
account = ["favorite_people_twiiter_id", "favorite_people_twiiter_id" ...]
"""

def tweet_noti(dt):
        twitter_api = twitter.Api(consumer_key=config.twitter_consumer_key,
                                consumer_secret=config.twitter_consumer_secret,
                                access_token_key=config.twitter_access_token,
                                access_token_secret=config.twitter_access_secret)
        temp_date = dt.get_alert_time()
        for account in config.account:
                statuses = twitter_api.GetUserTimeline(screen_name=account, count=1,
                        include_rts=True, exclude_replies=False)
                toaster = ToastNotifier()
                for status in statuses:
                        if(dt.get_alert_time() < dt.get_time(status.created_at)):
                                if(temp_date < dt.get_time(status.created_at)):
                                        temp_date = dt.get_time(status.created_at)
                                profile = status.user.profile_image_url
                                handler.get_profile(profile)
                                toaster.show_toast(status.user.name + "님이 트윗을 올렸습니다.", status.text,
                                         icon_path="profile.ico")
        dt.update_time(temp_date)