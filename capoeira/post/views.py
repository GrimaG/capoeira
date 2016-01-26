from django.shortcuts import render
from .models import *
from django.utils import timezone
from .forms import PostForm
from django.views.generic import CreateView, ListView, DeleteView
from .forms import StudantForm
from .forms import CordaForm
from .forms import GroupForm
from .forms import ProfessorForm
from .forms import GradeForm
from django.core.urlresolvers import reverse_lazy
from .forms import ExamForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
# Create your views here.
def post_list(request):
    posts = Posts.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post/list_post.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if post.published_date== None:
                post.published_date = post.created_date
            post.save()
            return redirect('post.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/post_edit.html', {'form': form})



def studant_new(request):
    if request.method == "POST":
        form = StudantForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            posts = Posts.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return redirect('post_list.html', {'posts': posts})
    else:
        form = StudantForm()
    return render(request, 'register/register_studant.html', {'form': form})

def color_new(request):
    if request.method == "POST":
        form = CordaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            posts = Posts.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return redirect('post.views.post_list')
    else:
        form = CordaForm()
    return render(request, 'register/register_color.html', {'form': form})

def group_new(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            posts = Posts.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return redirect('post.views.post_list')
    else:
        form = GroupForm()
    return render(request, 'register/register_group.html', {'form': form})

def professor_new(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            posts = Posts.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return redirect('post.views.post_list')
    else:
        form = ProfessorForm()
    return render(request, 'register/register_professor.html', {'form': form})

def grade_new(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            posts = Posts.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return redirect('post.views.post_list')
    else:
        form = GradeForm()
    return render(request, 'register/register_grade.html', {'form': form})

def exam_new(request):
    if request.method == "POST":
        form = ExamForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            posts = Posts.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return redirect('post.views.post_list')
    else:
        form = ExamForm()
    return render(request, 'register/register_exam.html', {'form': form})


class list_post(ListView):
        template_name = 'post/post_list.html'
        model = Posts
        def get_success_url(self):
            return reverse('list_post')

class list_cor(ListView):
        template_name = 'list/color_list.html'
        model = Corda
        def get_success_url(self):
            return reverse('list_cor')

class list_exam(ListView):
        template_name = 'list/exam_list.html'
        model = Exame
        def get_success_url(self):
            return reverse('list_exam')
class list_group(ListView):
        template_name = 'list/group_list.html'
        model = Grupo
        def get_success_url(self):
            return reverse('list_group')
class list_studant(ListView):
        template_name = 'list/studant_list.html'
        model = Aluno
        def get_success_url(self):
            return reverse('list_studant')

class list_professor(ListView):
        template_name = 'list/professor_list.html'
        model = Professor
        def get_success_url(self):
            return reverse('list_professor')

class postDelete(DeleteView):
    model = Posts
    success_url = reverse_lazy('list_post')

#template method para criar relatorios
class relatorio(models.Model):
    def titulo(self):  pass
    def page_head(self):  pass
    def page_end(self):  pass
    def conteudo(self): pass
    def eat(self):  pass

    def gerar(self):
        relatorio=''
        relatorio +=self.page_head()
        relatorio +=self.titulo()
        relatorio +=self.conteudo()
        relatorio +=self.page_end()
        return HttpResponse(relatorio)

class relatorioClasse(relatorio):
    lista_grupos = factory.retornar_objeto("grupo").objects.all()
    def page_head(self):
        return "{% extends 'post/base.html' %}{% block content %}"
    def titulo(self):
        return "<h1>Relatorio por Alunos</h1>"
    def conteudo(self):
        conteudo = ''
        for grupos in lista_grupos:
            lista_turma = factory.retornar_objeto("turma").objects.filter(grupo=grupos)
            for turmas in lista_turma:
                
        return "<h1>Relatorio por Alunos</h1>"
