from django import forms
from .models import Posts
from .models import Aluno
from .models import Corda
from .models import Grupo
from .models import Professor
from .models import Turma
from .models import Exame
from django.views.generic import CreateView, ListView
class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('title', 'text',)


class StudantForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'

class CordaForm(forms.ModelForm):

    class Meta:
        model = Corda
        fields = '__all__'

class GroupForm(forms.ModelForm):

    class Meta:
        model = Grupo
        fields = '__all__'

class ProfessorForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = '__all__'

class GradeForm(forms.ModelForm):

    class Meta:
        model = Turma
        fields = '__all__'

class ExamForm(forms.ModelForm):

    class Meta:
        model = Exame
        fields = '__all__'
