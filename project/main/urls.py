from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'), 
    path('employee', views.employee, name='employee'), 
    path('add_user', views.add_user, name='add_user'), 
    path('user_profil', views.user_profil, name='user_profil'), 
    path('yes_no', views.yes_no, name='yes_no'), 
    path('works', views.works, name='works'), 
    path('work_user', views.work_user, name='work_user'), 
    path('work_text', views.work_text, name='work_text'), 
    path('work_progres', views.work_progres, name='work_progres'), 
    path('add_work', views.add_work, name='add_work'), 
    path('report', views.report, name='report'), 
    path('report_user', views.report_user, name='report_user'), 



    
    path('user', views.user, name='user'), 
    path('user_works', views.user_works, name='user_works'), 
    path('work_profil', views.work_profil, name='work_profil'), 
]