################################################
####                                        ####
####! InstaPy by Borderless Cosmos Limited !####
####                                        ####
################################################

# This template will unfollow all non-followers

from instapy import InstaPy
from instapy import smart_run

# Connection creation 
session = InstaPy(headless_browser=True, 
                  bypass_security_challenge_using='email')

with smart_run(session):

    # This command will unfollow all non-followers and will sleep 1 hour every 16 unfollow.
    #! Insta Limit :
    #  Per hour : 20 unfollow / follow
    #  Per day : 200 unfollow / follow

    session.unfollow_users(amount=16, nonFollowers=True, style="RANDOM", unfollow_after=None, sleep_delay=600)