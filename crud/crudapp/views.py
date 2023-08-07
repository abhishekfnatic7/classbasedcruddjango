
from django.views.generic.edit import FormView,DeleteView,UpdateView
from django.views.generic.list import ListView

from django.shortcuts import redirect
from django.urls import reverse
from .models import Student
from django.contrib.messages.views import SuccessMessageMixin
from .forms import StudentForm
# Create your views here.

class Studentformview(FormView):
    form_class=StudentForm
    template_name="student.html"

    def form_valid(self, form):
        form.save()
        return redirect(reverse('studentlist'))

class Studentlist(ListView):
    model=Student
    template_name="studentlist.html"
    context_object_name='cat'


class StudentUpdateview(SuccessMessageMixin,UpdateView):
    model=Student
    form_class=StudentForm
    pk_url_kwarg='id'
    template_name="studentdetail.html"
    success_url='/studentlist'
    success_message="Form Updated successfully"

class StudentDeleteView(SuccessMessageMixin,DeleteView):
    model=Student
    pk_url_kwarg='id'
    success_url='/studentlist'
    context_object_name='cat'
    template_name='student_confirm_delete.html'
    success_message="Student Information Deleted Successfully"



