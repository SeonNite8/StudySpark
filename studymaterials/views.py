from django.shortcuts import render
from .models import StudyMaterial

def study_materials(request):
    materials = StudyMaterial.objects.all()
    query = request.GET.get('q')
    subject_filter = request.GET.get('subject')
    
    if query:
        materials = materials.filter(title__icontains=query)
    
    if subject_filter:
        materials = materials.filter(subject=subject_filter)
    
    return render(request, 'study_materials.html', {'materials': materials, 'query': query})
