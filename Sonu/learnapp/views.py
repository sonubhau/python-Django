from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Wellcome to Learn App")
@csrf_exempt
def student(request):
    if request.method == "GET":
        result =[]
        # To get all the Object from database (Student Table)
        student_Table = Student.objects.all() #python orm module (Object Relationshiop module)
        for st in student_Table: #get Each object From student table
            data = {      # store inside dict
                "Name" : st.Name,
                "Last_Name" : st.Last_Name,
                "Roll_Number" : st.Roll_Number
            }
            result.append(data) #appent that dict inside list
        return HttpResponse(json.dumps(result)) # convert that list in to json format and send as a responce
    if request.method == "POST":
        # Assume that data comming from post method
        body_unicode = request.body.decode('utf-8') # body always comes in encoded format 
        # so we need to decode that body 
        data = json.loads(body_unicode) # load that (body) data in json format
        # now extract the the column name from that data like dictinary by key name
        Name = data['Name']
        Last_Name = data['Last_Name']
        Roll_Number = data['Roll_Number']
        # create a instance/object of class/table and assign that data as thair respected columns
        student = Student(Name = Name,Last_Name = Last_Name,Roll_Number = Roll_Number)
        student.save() #save the data in database
        # send the http responce back
        return HttpResponse("Student Added Successfuly In Database....!!!!!!")
    if request.method == "DELETE":
        body_unicode = request.body.decode('utf-8') # decode that data 
        data = json.loads(body_unicode) # load that data in json format
        name = data['name']
        student = Student.objects.filter(Name = name).delete()
        return HttpResponse("Student Deleted Successfuly From Database....!!!!!!")