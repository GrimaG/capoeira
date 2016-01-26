"""capoeira URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns,include, url
from . import views


urlpatterns = [
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^lista/$', views.list_post.as_view(), name='list_post'),
    url(r'^lista/corda/$', views.list_cor.as_view(), name='list_cor'),
    url(r'^lista/exame/$', views.list_exam.as_view(), name='list_exam'),
    url(r'^lista/grupo/$', views.list_group.as_view (), name='list_group'),
    url(r'^lista/aluno/$', views.list_studant.as_view (), name='list_studant'),
    url(r'^lista/turma/$', views.list_grade.as_view (), name='list_grade'),
    url(r'^lista/professor/$', views.list_professor.as_view (), name='list_professor'),
    url(r'^register_color.html$', views.color_new),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^register_studant.html$', views.studant_new, name='studant_new'),
    url(r'^register_group.html$', views.group_new, name='group_new'),
    url(r'^register_professor.html$', views.professor_new, name='professor_new'),
    url(r'^register_grade.html$', views.grade_new, name='grade_new'),
    url(r'^register_exam.html$', views.exam_new, name='exam_new'),
]
