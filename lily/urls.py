"""
URL configuration for lily project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from kelly import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'), 
    path('staff/', views.staff, name='staff'),
     path('', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('assignment_list', views.assignment_list, name='assignment_list'),
    path('assignmentst_list', views.assignmentst_list, name='assignmentst_list'),
    path('assignment/create/', views.create_assignment, name='create_assignment'),
    path('assignment/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('assignment/<int:assignment_id>/de', views.assignment_de, name='assignment_de'),
    path('assignment/<int:assignment_id>/submit/', views.submit_assignment, name='submit_assignment'),
    path('assignment/<int:assignment_id>/submissions/', views.view_submissions, name='view_submissions'),
    path('assignment/<int:assignment_id>/submissi/', views.viewst_submissi, name='viewst_submissi'),
    path('submission/<int:submission_id>/feedback/', views.leave_feedback, name='leave_feedback'),
    path('submission/<int:submission_id>/view_feedback/', views.view_feedback, name='view_feedback'),
    path('submission/<int:submission_id>/delete/', views.delete_submission, name='delete_submission'), 
    path('assignment/<int:assignment_id>/delete/', views.delete_assignment, name='delete_assignment'),
    path('send_email/', views.send_email, name='send_email'),
    path('failure/',views.failure,name='failure'),
      path('check_face/', views.check_face, name='check_face'),
      path('index/', views.index, name='index'),
      path('about/', views.about, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)