from django.shortcuts import render
from django.http import JsonResponse
import json
import os
import mysql.connector
from random import randint
# Create your views here.
def user_data(request):
	#print("begin")
	fileDir = os.path.dirname(os.path.realpath('__file__'))#Project Directory Path
	print(fileDir)
    
	with open(os.path.join(fileDir,"Test JSON.json"),mode="r") as f:#Opening  JSON file
		s=json.load(f)
		print(s)
	#print("Done")
	#print(type(s))
	l=[]
	

	try:
		#Establishing connection with the 'UserData' database"
		connection=mysql.connector.connect(host="localhost",database="UserData",user="root",password="root")
		print("Connected to Database")
		cursor=connection.cursor()#Connecting the database
		for i in s["members"]:
			full_name=i["real_name"]
			location=i["tz"]
			no_workdaysPerWeek=randint(1,7)#random integer generation.
			#Execute the insert query
			cursor.execute("""insert into User_usermodel(Full_Name,Location,No_of_WorkDaysPerWeek) values('%s','%s','%s')""" %(full_name,location,no_workdaysPerWeek))
			connection.commit()#save database
			l.append([{"name":full_name,"location":location,"DaysPerWeek":no_workdaysPerWeek}])
	except Exception as e:#raises exception if connection of the database failed
		print(e)
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()#disconnect the database
	print(l)

	#user_json=[{"name":full_name,"location":location,"DaysPerWeek":no_workdaysPerWeek}]
	

	return JsonResponse({"User_JSON":l})#return the modified json


