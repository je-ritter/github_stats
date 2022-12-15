import hashlib

from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User class which extends built-in User. Presently, just adds a "bio"
# and a gravatar method. Feel free to add your own new fields here!

class User(AbstractUser):

    bio = models.TextField()

    def gravatar(self, size=None):
        GRAVATAR_URL = 'https://gravatar.com/avatar/%s?d=identicon%s'
        email = str(self.email).strip().lower()
        digest = hashlib.md5(email.encode('utf-8')).hexdigest()

        if size:
            size_str = '&s=%i' % size
        else:
            size_str = ''

        return GRAVATAR_URL % (digest, size_str)
        
class DashboardPanel(models.Model):
	github_username = models.CharField(max_length=127)
	repo_name = models.CharField(max_length=127)
	
	creator = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
	)
	
	panel_type = models.CharField(max_length=127, choices=[
		("piechart", "Pie-chart of languages used"),
		("barchart", "Bar-chart of languages used"),
	])
	
	def get_api_and_render_chart(self):
		response = requests.get("https://api.github.com/users/") # etc...
		repo_list = response.json()
		# TODO: make aspects of the chart (such as Pie vs Bar, styling, etc)
		# customizable based on the data in the panel model
		chart = pygal.Pie()
		# ...snip... (for loops etc building the Pygal chart here)
		# TODO: Check the otherpygal Chart for info...
		rendered = chart.render()
		return rendered
        


# TODO: More fields might got here...
# (Consider adding other customizable aspects, including style or theme,
# different chart options, text descriptions.)

 	
