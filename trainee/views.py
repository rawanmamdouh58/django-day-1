from django.shortcuts import render ,redirect

# Create your views here.


def traineeList(request):
    trainees=[{"id":1,"name":"Ahmed"},{"id":2,"name":"Ayat"},{"id":3,"name":"Ali"}]
    return render(request,'listtrainee.html',{"trainees":trainees})


def addTrainee(requset):
    return render(requset,'addTrainee.html')

def updateTrainee(requset,id):
    print(id)
    return redirect('traineeList')

def deleteTrainee(requset,id):
    print(id)    
    return redirect('traineeList')