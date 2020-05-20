from django.shortcuts import render
import os
import json
# Create your views here.
def index(request):
	fileDir = os.path.dirname(os.path.realpath('__file__'))#Project Directory Path
	print(fileDir)
    
	with open(os.path.join(fileDir,"Test JSON.json"),mode="r") as f:#opening JSON file
		s=json.load(f)
		print(s)
	print(type(s))#Type of s
	

	return render(request,"index/index.html",context=s)


