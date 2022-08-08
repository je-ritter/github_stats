from django.shortcuts import render

import requests
import pygal

from pygal.style import DarkenStyle

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
    



	
			
