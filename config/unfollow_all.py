################################################
####                                        ####
####! InstaPy by Borderless Cosmos Limited !####
####                                        ####
################################################

# This template will unfollow everybody

from instapy import InstaPy
from instapy import smart_run

# Connection creation 
session = InstaPy(headless_browser=True, 
                  bypass_security_challenge_using='email')

with smart_run(session):

    # This command will unfollow everybody (7481 accounts) after following them 
    # for at least 48 hours and will sleep 1 hour every 10 unfollow.
    #! Insta Limit :
    #  Per hour : 20 unfollow / follow
    #  Per day : 200 unfollow / follow

    session.unfollow_users(amount=7481, allFollowing=True, style="RANDOM", unfollow_after=None, sleep_delay=600)