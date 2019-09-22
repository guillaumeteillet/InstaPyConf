################################################
####                                        ####
####! InstaPy by Borderless Cosmos Limited !####
####                                        ####
################################################

# This template will watch stories

from instapy import InstaPy
from instapy import smart_run
import random

# Connection creation 
session = InstaPy(headless_browser=True, 
                  bypass_security_challenge_using='email')

with smart_run(session):

    UserList = [
        "cedricannicette", "entrepreneursfr", 'alexandre.lahouel', 'franckmaessmart',
        "antoinebm", "professor.enzo", "fouqueflorent", "deslivrespoursenrichirofficiel",
        "carrement_libre", "kimbennour", "kevin_marieqlrr", "jesuismonpatron.fr",
        "mickaelzonta", "xolali_zigah", "mason.mnd", "manuelravier", "sebastienascon",
        "alechy", "jean.laplace", "vincent.d.robert", "grosargentofficiel"
    ]
    User = random.choice(UserList)

    user_followers = session.grab_followers(username=User, amount=1000, live_match=False, store_locally=False)
    session.set_do_story(enabled=True,percentage=70, simulate=False)
    session.story_by_users(user_followers)