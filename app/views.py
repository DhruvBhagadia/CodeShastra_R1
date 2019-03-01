from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import re
import json
import random
import os


def index(request):


    return render(request, 'index.html', {})


def linechart(request):

    return render(request, 'linechart.html', {})


def chart(request):
	data = [
				["China", 1882, "#7474F0"],
				["Japan", -33.923036, "#C5C5FD"],
				["Germany", -34.028249, "#952FFE"],
				["UK", -33.80010128657071, "#7474F0"]
			]
	context = {"data": data}
	return render(request, 'linechart.html', context)


def trying(request):
	return render(request, 'trying.html', {})


def render_sports_page(request):
	return render(request, 'sports.html', {})


def render_politics_page(request):

    return render(request, 'politics.html', {})


def render_gen_politics_page(request):
    return render(request, 'gen-politics.html', {})


def render_gen_sports_page(request):
    return render(request, 'gen-sports.html', {})


def context_qa(request):
    
    return render(request, "context_qa.html")
