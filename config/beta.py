################################################
####                                        ####
####! InstaPy by Borderless Cosmos Limited !####
####                                        ####
################################################

# This template will watch stories

from instapy import InstaPy
from instapy import smart_run

# Connection creation 
session = InstaPy(headless_browser=True, 
                  bypass_security_challenge_using='email')

with smart_run(session):

    session.watch_followers_stories_of_users(['cedricannicette'], amount=10, randomize=False)