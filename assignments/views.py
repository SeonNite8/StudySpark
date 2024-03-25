from django.shortcuts import render
from django.http import HttpResponse
from .forms import AssignmentForm

def upload_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.student = request.user
            assignment.save()
            return HttpResponse('Assignment submitted successfully')
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = AssignmentForm()
    return render(request, 'assignments/upload_assignment.html', {'form': form})
