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

    session.set_do_story(enabled = True, percentage = 70, simulate = False)
    session.story_by_tags(['entreprise', 'entreprendre', 'startup', 'business',
    'entrepreneurs', 'success', 'leadership', 'marketing', 'infopreneurs', 'company',
    'entrepreneurship', 'money', 'motivation', 'work', 'instaentrepreneur', 'instastartup',
    'instabusiness', 'instaentrepreneurs', 'instasuccess', 'instaleadership', 'instamarketing',
    'instacompany', 'instasmallbiz', 'FEMTREPRENEUR', 'ENTREPRENEUSE', 'ENTREPRENEURE',
    'FEMMEENTREPRENEURE', 'ENTREPRENDREAUFEMININ', 'WontStop', 'QLRR', 'Immobilier', 'Mindset',
    'Freedom', 'BusinessOwner', 'OnlineBusiness', 'Coaching', 'Ambition', 'ThinkBig', 'Quitterlaratrace',
    'Businessman', 'BeYourOwnBoss', 'SmallBusiness', 'Mentor', 'InternetBusiness', 'digitalnomade',
    'createurfrancais', 'bourse', 'immo', 'appartement', 'immeuble'])