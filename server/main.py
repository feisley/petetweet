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
    'petetweet.status': api.status,
    'petetweet.post': api.post,
}

def main():
    application_paths = [('/', MainPage),
        ('/api', WebAppGateway(services))]
    application = webapp.WSGIApplication(application_paths, debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main() 