from django.shortcuts import render


def index(request):
    return render(request, 'adminn/index.html')


def employee(request):
    return render(request, 'adminn/employee.html')


def login(request):
    return render(request, 'login.html')



def add_user(request):
    return render(request, 'adminn/add_user.html')



def user_profil(request):
    return render(request, 'adminn/user_profil.html')


def yes_no(request):
    return render(request, 'adminn/yes_no.html')


def work_text(request):
    return render(request, 'adminn/work_text.html')



def works(request):
    return render(request, 'adminn/works.html')


def work_user(request):
    return render(request, 'adminn/work_user.html')


def work_progres(request):
    return render(request, 'adminn/work_progres.html')


def add_work(request):
    return render(request, 'adminn/add_work.html')


def report(request):
    return render(request, 'adminn/report.html')


def report_user(request):
    return render(request, 'adminn/report_user.html')




def user(request):
    return render(request, 'user/user_d.html')


# Create your views here.
