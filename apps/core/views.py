from django.shortcuts import render

import requests
import pygal

from pygal.style import DarkenStyle
from .models import DashboardPanel

# Two example views. Change or delete as necessary.
def home(request):

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)
    
def allrepos(request):
    response = requests.get('https://api.github.com/users/je-ritter/repos')
    repo_list = response.json()
    context = {
    	# TODO: Example and possibly change the code below. Why are they the same??
    	"github_repos": repo_list,
    	"name": repo_list,
    }
    print("yay - check out all the repos!")

    return render(request, 'pages/allrepos.html', context)
    
def visualrepos(request):
    response = requests.get('https://api.github.com/users/je-ritter/repos')
    repo_list = response.json()
    darken_style = DarkenStyle('#66f2f4')
    chart = pygal.Pie(inner_radius = .75, fill=True, interpolate='cubic', style=darken_style)
    
    for repo_dict in repo_list:	
        value = repo_dict["size"]
        label = repo_dict["name"]
        chart.add(label, value)
        chart.render_to_file('chart.svg')
			
    print ("Is the chart working?")
	
    chart_svg_as_datauri = chart.render_data_uri()
    context = {
        "rendered_chart_svg_as_datauri": chart_svg_as_datauri,
    }
    
    return render(request, 'pages/visualrepos.html', context)


def about(request):
    context = {
    }

    return render(request, 'pages/about.html', context)
    
def viewpanels(request):
	panels = DashboardPanel.objects.all()
	context = {
		"dboard_panels": panels,
	}
	return render(request, "pages/view_panels.html", context)
	
def panel_details(request, panel_id):
	panel = DashboardPanel.objects.get(id=panel_id)
	
	chart = pygal.Pie()
		# TODO: Make aspects of the chart (such as pie v bar, styling, etc)
		# custoomizable based on the data in the panel model
		
		# TODO: Get data from API, file, DB, or womehere else, possibly based on
		# the panel model
		
	for repo_dict in repo_list:
		value = 42 # TODO: Replace this...
		label = repo_dict["name"]
		chart.add(label,value)

		context = {
			"panel": panel,
			"rendered_chart_svg": chart.render(), # TODO: change this to the other 
			# format??
		}
		return render (request, "panel_details.html", context)
		
def view_user_dash(request, the_username):
	user_object = User.objects.filter(username=the_username)
	panels = DashboardPanel.objects.filter(user=user_object)
	context = {
		'panels': panels,
	}
	return render(request, "panel_details.html", context)

	

	
			
