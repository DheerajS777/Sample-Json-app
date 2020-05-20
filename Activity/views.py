from django.shortcuts import render
from django.http import JsonResponse
import os
import json
import mysql.connector
# Create your views here.
def activity_data(request):
	#print("Begin Activity View")
	fileDir = os.path.dirname(os.path.realpath('__file__'))#Project Directory
	print(fileDir)
    
	with open(os.path.join(fileDir,"Test JSON.json"),mode="r") as f:#Opening the JSON file
		s=json.load(f)
		print(s)
	print(type(s))
	d=[]
	try:
		#Establishing the connection to the Database
		connection=mysql.connector.connect(host="localhost",database="UserData",user="root",password="root")
		print("Connected to Activity_Database")
		cursor=connection.cursor()
		for i in s["members"]:
			id_no=i["id"]
			city=i["tz"]
			st_shift1=i["activity_periods"][0]["start_time"]
			st_shift2=i["activity_periods"][1]["start_time"]
			st_shift3=i["activity_periods"][2]["start_time"]
			cursor.execute("""insert into Activity_activity_data(Member_id,Location,StartTime_Shift1,StartTime_Shift2,StartTime_Shift3) values('%s','%s','%s','%s','%s')""" %(id_no,city,st_shift1,st_shift2,st_shift3))
			connection.commit()#Save the database
			d.append([{"id_no":id_no,"Country/City":city,"Shift 1 time":st_shift1,"Shift 2 time":st_shift2,"Shift 3 time":st_shift3}])
	except Exception as e:
		print(e)
	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()#Disconnect the database
	print(d)

	return JsonResponse({"ActivityPeriod_JSON":d})






# Create your views here.
