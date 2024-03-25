from django.shortcuts import render

def classmates(request):
    return render(request,'classes/classmates.html')

def classroom(request):
    return render(request,'classes/classroom.html')

def create_class(request):
    return render(request,'classes/create_class.html')

def join_class(request):
    return render(request,'classes/join_class.html')

def assignments(request):
    return render(request,'classes/assignments.html')

