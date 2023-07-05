
from django.shortcuts import render, redirect
from .forms import CountryForm, StudentForm
from .models import Student,Country
from django.db.models import Count

def index(request):
    countries = Country.objects.all()
    students_by_country = []

    for country in countries:
        students = Student.objects.filter(country=country)
        students_by_country.append({
            'country': country,
            'total': students.count(),
            'students': students
        })
    # students = Student.objects.values('country').annotate(total=Count('country')).order_by('country')
    return render(request, 'index.html', {"students_by_country":students_by_country})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def add_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CountryForm()
    return render(request, 'add_country.html', {'form': form})