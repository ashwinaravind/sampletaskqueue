import webapp2
from google.appengine.api import users
# [START import_ndb]
from google.appengine.ext import db
# [END import_ndb]

# [START greeting]
class Greeting(db.Model):
    """Models an individual Guestbook entry."""
    content = db.StringProperty(multiline=True)
# [END greeting]




class MainPage(webapp2.RequestHandler):

	
    def get(self):
    	self.response.headers['Content-Type'] = 'text/plain'
    	self.response.write("test")
    	self.greeting = Greeting(content='tyrtty')
    	self.greeting.put()
    	#self.redirect('/')

    
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


def main():
    run_wsgi_app(application)
 
if __name__ == "__main__":
    main() 
