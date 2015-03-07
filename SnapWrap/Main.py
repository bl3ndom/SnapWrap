from snapchat import Snapchat
import time
from requests.exceptions import HTTPError, ConnectionError
import logging

class SnapchatBot(Snapchat):
    
    def on_snap(self, sender, snap):
        self.post_story(snap)
        
    def on_friend_add(self, friend):
        self.add_friend(friend)

    def on_friend_delete(self, friend):
        self.delete_friend(friend)

logging.getLogger("requests").setLevel(logging.WARNING)

while True:
    try:
        bot = SnapchatBot(*["user", "pass"])
        bot.begin()
    except (HTTPError, ConnectionError) as e:
        time.sleep(180)
    
