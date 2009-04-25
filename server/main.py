import time

import wsgiref.handlers
from google.appengine.ext import webapp

from pyamf.remoting.gateway.google import WebAppGateway

from petetweet import api


class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, Welcom to PeteTweet!')

# Return the API version
def version():
    return "PeteTweet API 1.0.0"

# Define the API services for PyAMF
services = {
    'api.version': version,
    'petetweet.register': api.register,
    'petetweet.login': api.login,
    'petetweet.logout': api.logout,
    'petetweet.status': api.status,
    
    'petetweet.post': api.post,
    
    'petetweet.gettweets': api.gettweets,
    'petetweet.getusertweets': api.getusertweets,
    'petetweet.getalltweets': api.getalltweets,
    'petetweet.getfollowedtweets': api.getfollowedtweets,
    
    'petetweet.search': api.search,
    'petetweet.profile': api.getMyProfile,
    'petetweet.updateprofile': api.updateMyProfile,
    'petetweet.getprofile': api.getProfile,
    
    'petetweet.follow': api.follow,
    'petetweet.unfollow': api.unfollow,
    'petetweet.checkfollower': api.checkFollower,
    'petetweet.checkfollowing': api.checkFollowing,
    'petetweet.followers': api.followers,
    'petetweet.following': api.following,
}

def main():
    application_paths = [('/', MainPage),
        ('/api', WebAppGateway(services))]
    application = webapp.WSGIApplication(application_paths, debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main() 