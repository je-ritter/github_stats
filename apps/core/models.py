from django.db import models
from apps.accounts.models import User

class DashboardPanel(models.Model):
	github_username = models.CharField(max_length=127)
	repo_name = models.CharField(max_length=127)
	
	panel_type = models.CharField(max_length=127, choices=[
		("piechart", "Pie-chart of languages used"),
		("barchart", "Bar-chart of languages used"),
	])
	
	def get_api_and_render_chart(self):
		response = requests.get("https://api.github.com/users/je-ritter/repos") # etc...
		repo_list = response.json()
		# TODO: make aspects of the chart (such as Pie vs Bar, styling, etc)
		# customizable based on the data in the panel model
		chart = pygal.Pie()
		# ...snip... (for loops etc building the Pygal chart here)
		# TODO: Check the otherpygal Chart for info...
		for repo_dict in repo_list:	
			value = repo_dict["size"]
			label = repo_dict["name"]
			chart.add(label, value)
			chart.render('chart.svg')
		print ("Is the chart working?")
		rendered = chart.render()
		return rendered
	
	# TODOL more fields might go here...
	# (Consider adding other customiable aspects, including style or theme,
	# different chart options, text descriptions)
