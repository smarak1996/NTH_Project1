from django.shortcuts import render
from .models import StudentData


def student_view(request):
    if request.method == 'POST':
        StudentData(

            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            mobile = request.POST['mobile'],
            gender = request.POST['gender']

        ).save()
        return render(request, 'main_page.html')

    student = StudentData.objects.all()
    return render(request, 'main_page.html', {'student':student})
