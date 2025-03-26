from django.shortcuts import render,redirect
from.models import user_entry_details,problem_selection

def login(request):
    if request.method == 'POST':
        name=request.POST['name']
        department=request.POST['department']
        college_name=request.POST['college_name']
        year=request.POST['year']
        team_name=request.POST['team_name']
        obj=user_entry_details()
        obj.name=name
        obj.department=department
        obj.college_name=college_name
        obj.year=year
        obj.team_name=team_name
        obj.save()
        return redirect('/home')
    return render(request,'index.html')

def home(request):
    return render (request,'home.html')

def department(request):
    return render (request,'department.html')

def symposium(request):
    return render (request,'symposium.html')

def domain(request):
    return render (request,'domain.html')
    
def agriculture(request):
    return render (request,'agriculture.html')

def healthcare(request):
    return render (request,'healthcare.html')

def transport(request):
    return render (request,'transport.html')

def space(request):
    return render (request,'space.html')

def disaster(request):
    return render (request,'disaster.html')

def data_privacy(request):
    return render (request,'data_privacy.html')

def education(request):
    return render (request,'education.html')

def resource(request):
    return render (request,'resource.html')

def problem(request):
    if request.method ==  'POST':
        team_name=request.POST['team_name']
        problem_domain=request.POST['problem_domain']
        problem_statement_number=request.POST['problem_statement_number']
        obj=problem_selection()
        obj.team_name=team_name
        obj.problem_domain=problem_domain
        obj.problem_statement_number=problem_statement_number
        obj.save()
        return redirect('/home')
    return render(request,'problem_selection.html')


