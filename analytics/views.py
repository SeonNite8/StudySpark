import os
from django.shortcuts import render
import matplotlib.pyplot as plt
from analytics.models import TestScore

def save_bar_chart(request):
    # Your existing code to generate the bar chart
    data = TestScore.objects.all()
    students = [score.student.name for score in data]
    marks = [score.test1 + score.test2 + score.test3 + score.test4 + score.test5 for score in data]
    
    plt.figure(figsize=(10, 5))
    plt.bar(students, marks, color='skyblue')
    plt.xlabel('Students')
    plt.ylabel('Total Marks')
    plt.title('Total Marks of Students in All Tests')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Define the path to save the image file within the "analytics" app's static folder
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(BASE_DIR, 'analytics', 'static', 'analytics')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    
    # Save the bar chart image to the static folder
    filename = 'average_marks.png'
    image_path = os.path.join(static_dir, filename)
    plt.savefig(image_path)

    return render(request, 'analytics/analytics.html')
